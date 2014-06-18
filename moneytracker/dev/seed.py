from django.contrib.auth.models import User

print('Creating Development User...')
dev = User(username=dev)
dev.set_password('1234')
dev.save()