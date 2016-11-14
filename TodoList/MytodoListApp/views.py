from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.urls import reverse

from .models import todo


def index(request):
    # The `POST` has the data from the HTML form that was submitted.
    # ORM queries the database for all of the to-do entries.

    if request.method == 'POST':
        # Get the data from the form
        name = request.POST.get('name')
        description = request.POST.get('description')
        # if (str(name).strip(" ") != "Item name" or str(name).strip(" ") != "") and  (str(description).strip(" ") != "Description" or str(description).strip(" ") !=""):
        # add the data to the database
        items = todo.objects.create(task_name=name, task_description=description)

    # Gets the todos we need from the database
    items = todo.objects.all()
    # render the page with the todos list
    return render(request, 'MytodoListApp/index.html', {'items': items})


def delete_todo(request):
    id =[]
    if request.method == 'POST':
        id =request.POST.getlist("itemsCheckedForDelete")
        # delete an object and send a confirmation response
    for things in id:
        todo.objects.get(id=things).delete()

    items = todo.objects.all()
    return render(request, 'MytodoListApp/index.html', {'items': items})
    # return HttpResponseRedirect("/")
    # return render_to_response('MytodoListApp/index.html', {'items': items})
