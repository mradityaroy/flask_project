from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
import random
class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):

        secret_id = str(random.randint(101, 999))
        user = {
            # "_id": uuid.uuid4().hex,
            "_id": request.form.get('name')+secret_id,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }


        user['password'] = pbkdf2_sha256.encrypt(user['password'])


        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address is already in use"}), 400
        else:
            if db.users.insert_one(user):
                return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user["password"]):
            return self.start_session(user)

        return jsonify({"error": "Invaild login credential"}), 401

