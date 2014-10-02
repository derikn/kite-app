kite-app
========

Requirements.txt Pasteout
========
Django==1.6.2
dj-database-url==0.2.2
dj-static==0.0.5
django-toolbelt==0.0.1
gunicorn==18.0
psycopg2==2.5.2
pystache==0.5.3
static==1.0.2
wsgiref==0.1.2
yolk==0.4.3

Application Structure
========
kite
	manage.py
	requirements.txt
	Procfile
	kite
		settings.py
		urls.py
		wsgi.py
		__init__.py
	subscription
		admin.py
		models.py
		tests.py
		views.py
		
