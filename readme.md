#To-do:
User.query.filter(User.birthday >= '1990-01-01').all()

#To get this working on local machine:

#Install python 3.7
#Create venv:
py -m venv venv

#If you have several versions of python, create a venv with python version 3.7:
C:\Users\Visar\AppData\Local\Programs\Python\Python37\python.exe -m venv venv

#Activate venv manually:
venv/scripts/activate

#Pipenv takes care of pip, .env, and venv at the same time.
#Install pipenv:
pip install pipenv

#Install all packages from pipfile:
pipenv install

#Then apply database migrations:
cd migrations
alembic upgrade head

#For production, remember to add .env to .gitignore.

#For Development, add formatters and other settings:
#On VSCode press Ctrl+Shift+P to select interpreter, in this case the venv one:

venv/scripts/python.exe

#Now everytime you click new terminal, the venv will be automatically activated.
#Adding formatters:
pip install flake8 black
