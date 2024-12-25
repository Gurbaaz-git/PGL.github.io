# Stuff I imported from the python library:

from django.shortcuts import render
from django import forms
from math import sqrt
from decimal import *

# The lists to tell the area and perimeter of shapes:

SquareArea = [""]
SquarePerimeter = [""]
RectArea = [""]
RectPerimeter = [""]
TriArea = [""]
TriPerimeter = [""]

# My form data:

class NewTaskForm(forms.Form):
    side = forms.DecimalField(label="Side", min_value=0.000000000000000001, max_value=99999999999999)

class RectangleForm(forms.Form):
    length = forms.DecimalField(label="Length", min_value=0.000000000000000001, max_value=99999999999999)
    width = forms.DecimalField(label="Width", min_value=0.000000000000000001, max_value=99999999999999)

class TriangleForm(forms.Form):
    base = forms.DecimalField(label="Base", min_value=0.000000000000000001, max_value=99999999999999)
    side_1 = forms.DecimalField(label="Side 1", min_value=0.000000000000000001, max_value=99999999999999)
    side_2 = forms.DecimalField(label="Side 2", min_value=0.000000000000000001, max_value=99999999999999)
    height = forms.DecimalField(label="Height", min_value=0.000000000000000001, max_value=99999999999999)

# My functions that run the pages:

    # Shapes page:

def index(request):
    return render(request, "tasks/index.html", {
    })

    # Square page:

def square(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            side = form.cleaned_data["side"]
            SquarePerimeter.pop(0)
            SquarePerimeter.append(side * 4)
            SquareArea.pop(0)
            SquareArea.append(side * side)
        else:
            return render(request, "tasks/square.html", {
                "form": form,
            })
    return render(request, "tasks/square.html", {
         "form": NewTaskForm(),
         "SquareArea": SquareArea,
         "SquarePerimeter": SquarePerimeter,
     })

    # Rectangle page:

def rectangle(request):
    if request.method == "POST":
        form = RectangleForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data["length"]
            width = form.cleaned_data["width"]
            RectPerimeter.pop(0)
            RectPerimeter.append(length * 2 + width * 2)
            RectArea.pop(0)
            RectArea.append(length * width)
        else:
            return render(request, "tasks/rectangle.html", {
                "form": form,
            })
    return render(request, "tasks/rectangle.html", {
         "form": RectangleForm(),
         "RectArea": RectArea,
         "RectPerimeter": RectPerimeter,
     })

def triangle(request):
    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            base = form.cleaned_data["base"]
            side_1 = form.cleaned_data["side_1"]
            side_2 = form.cleaned_data["side_2"]
            height = form.cleaned_data["height"]
            TriPerimeter.pop(0)
            TriPerimeter.append(base + side_1 + side_2)
            TriArea.pop(0)
            TriArea.append((height * base)/2)
        else:
            return render(request, "tasks/triangle.html", {
                "form" : form
            })
    return render(request, "tasks/triangle.html", {
        "form" : TriangleForm(),
        "TriArea" : TriArea,
        "TriPerimeter" : TriPerimeter
    })
