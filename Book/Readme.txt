Prerequisites
•	Python>=3.6
•	pip
•	virtualenv

Installation
•	virtualenv address_env
•	source address_env/bin/activate
•	pip install –r requirements.txt

Setup
•	python manage.py makemigrations
•	python manage.py migrate

Run Project
    python manage.py runserver
    #  To dump data from csv file to sqlite database)
    localhost:8000/address/loaddata
    # To display Address book
    localhost:8000/address/getdata
    # To add new record
    localhost:8000/address/getdata
    # To update record
    localhost:8000/address/updatedata/id
    # To delete record
    localhost:8000/address/deletedata/id


