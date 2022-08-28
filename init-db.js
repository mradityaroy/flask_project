db = db.getSiblingDB("user_login_system");
db.animal_tb.drop();

db.animal_tb.insertMany([
    {
        "_id": 1,
        "name": "aditya",
        "email": "test@email.com",
        "password": "password"
    },

]);