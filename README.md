# django-webserver
The quickest and dirtiest django webserver you've ever seen

Simple steps to get this baby running, also with these things # to explain what it does:

# Clone this baby
1. git clone https://github.com/ChillBroYo/django-webserver.git
# Get in this thing
2. cd django-webserver
# Get in the tutorial
3. cd tutorial
# Make a swagilicious virtual enviroment called swag
4. virtualenv swag
# Install Django
5. pip install django
# Install the one and only REST API
6. pip install djangorestframework
# Fire this baby up (run the damn server)
7. python manage.py runserver
# Curl request the server for users to the site located at http://127.0.0.1:8000/ in a new terminal window
# (I guess this step is optional in case you wanted to just leave this on forever for no reason)
8. curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/

9. Gloat, you did it
