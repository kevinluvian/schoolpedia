# schoolpedia
Schoolpedia is an app to help students to find schools easier

## Project Description
The project language is python, and HTML for the frontend

This project timeline is managed using trello: https://trello.com/b/9lABibvH/ntu-4-u-project
This project is implemented by using django http://djangoproject.com/ and SemanticUI https://semantic-ui.com
This project is tested automatically using CircleCI https://circleci.com/gh/kevinluvian/schoolpedia/ you can take a look whether each commit passed the test or not from github: https://github.com/kevinluvian/schoolpedia/commits/master
This project is deployed automatically for every passed test commit to heroku. You can see this project live at http://schoolpedia.herokuapp.com/

The project source code can be found on src/ folder
The project deliverables can be found on deliverables/ folder

## How to start
1. You need to finish the django tutorial https://www.djangoproject.com/
2. Install a virtualenv for this project `virtualenv venv`
3. Use the virtualenv `source venv/bin/activate` for LINUX/MAC, for WINDOWS use `venv/Scripts/activate`
4. install the requirements: `pip install -r requirements.txt`
5. Go to src/ folder and do initial migration by using `python manage.py migrate`
6. Start the server using `python manage.py runserver`

## How to test
1. Use the virtualenv `source venv/bin/activate` for LINUX/MAC, for WINDOWS use `venv/Scripts/activate`
2. install the requirements: `pip install -r requirements.txt`
3. Go to src/ folder
4. to run functional test: python functional_tests.py
5. to run unit test: python manage.py test
