from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Allow us to access the admin page
    url(r'^admin/', admin.site.urls),
    # Our main page
    url(r'^$', views.index, name='index'),
    # Delete items
    url(r'^delete_todo/', views.delete_todo, name='delete_todo')
]
