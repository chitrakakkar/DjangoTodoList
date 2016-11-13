from django.contrib import admin
from .models import todo

# Register model with the admin
# To make our model visible on the admin page,
# we need to register the model with:
admin.site.register(todo)
