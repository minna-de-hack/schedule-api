web: gunicorn project.wsgi:application --worker-class=uvicorn.workers.UvicornWorker --bind :8000 --workers 3 --threads 2

web: gunicorn main:app --workers=4 --worker-class=uvicorn.workers.UvicornWorker