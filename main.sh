pip install -r requirements.txt
cd www
python manage.py migrate
python manage.py runserver 0.0.0.0:3000