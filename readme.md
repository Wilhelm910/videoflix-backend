env starten: "env/scripts/activate"
backend starten: python manage.py runserver


env-lin starten: source env-lin/bin/activate
rq worker starten: python manage.py rqworker default