import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','website.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'Shivadom'
email = ''
password = 'Shivadom'
if User.objects.filter(username=username).exists():
    print('User already exists')
    sys.exit(0)
User.objects.create_superuser(username=username, email=email, password=password)
print('Superuser created')
