In this project I created a system adding discounts and viewing reports only for users with the status is_staff
They may be
added via site admin (url host/admin with login dmiv and password 123456 or run ./manage.py createsuperuser
and create it

for the system to work correctly, the database must contain a discount with name "default" and a value of 0, which
corresponds to a purchase without a discount
