from django.shortcuts import render
from django import forms
tasks = [""]
class NewTaskForm(forms.Form):
    task = forms.DecimalField(label="Side", min_value=0.000000000000000001)

# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.pop(0)
            tasks.append(task * task)
        else:
            return render(request, "tasks/add.html", {
                "form": form,
            })
    return render(request, "tasks/add.html", {
         "form": NewTaskForm(),
         "tasks": tasks
     })