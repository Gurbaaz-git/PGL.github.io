from django.shortcuts import render
from django import forms
area = [""]
perimeter = [""]
class NewTaskForm(forms.Form):
    side = forms.DecimalField(label="Side", min_value=0.000000000000000001)
# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
    })

def square(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            side = form.cleaned_data["side"]
            perimeter.pop(0)
            perimeter.append(side * 4)
            area.pop(0)
            area.append(side * side)
        else:
            return render(request, "tasks/square.html", {
                "form": form,
            })
    return render(request, "tasks/square.html", {
         "form": NewTaskForm(),
         "area": area,
         "perimeter": perimeter,
     })