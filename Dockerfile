# FROM python:3.8.1-alpine
# RUN pip install --upgrade pip

# RUN mkdir /app

# WORKDIR /app/

# ADD . /app/

# RUN pip install -r requirements.txt

# CMD ["python", "/app/app.py"]


# init a base image (Alpine is small Linux distro)
FROM python:3.8.1-alpine
# update pip to minimize dependency errors 
RUN pip install --upgrade pip
# define the present working directory
WORKDIR /app
# copy the contents into the working dir
ADD . /app/
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["flask", "run","--host", "0.0.0.0"]
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]