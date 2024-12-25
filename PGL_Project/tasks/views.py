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
base = 0;
side_1 = 0;
side_2 =0;
 
# My form data:

class NewTaskForm(forms.Form):
    side = forms.DecimalField(label="Side", min_value=0.000000000000000001, max_value=99999999999999)

class RectangleForm(forms.Form):
    length = forms.DecimalField(label="Length", min_value=0.000000000000000001, max_value=99999999999999)
    width = forms.DecimalField(label="Width", min_value=0.000000000000000001, max_value=99999999999999)

class TriangleForm(forms.Form):
    base = forms.FloatField(label="Base", min_value=0.000000000000000001, max_value=99999999999999)
    side_1 = forms.FloatField(label="Side A", min_value=0.000000000000000001, max_value=99999999999999)
    side_2 = forms.FloatField(label="Side B", min_value=0.000000000000000001, max_value=99999999999999)

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
            try:
                global base
                global side_1
                global side_2
                base = form.cleaned_data["base"]
                side_1 = form.cleaned_data["side_1"]
                side_2 = form.cleaned_data["side_2"]
                b = base + side_2 + side_1
                s = (b)/2
                a = sqrt(s*(s-base)*(s-side_1)*(s-side_2))*base
                if a != 0:
                    TriPerimeter.pop(0)
                    TriPerimeter.append(b)
                    TriArea.pop(0)
                    TriArea.append(a)
                else:
                    TriPerimeter.pop(0)
                    TriPerimeter.append("nothing! Make sure base plus side A is greater than side B. Invalid")
                    TriArea.pop(0)
                    TriArea.append("nothing! Make sure base plus side A is greater than side B. Invalid")
            except ValueError:
                TriPerimeter.pop(0)
                TriPerimeter.append("nothing! Make sure base plus side A is greater than side B. Invalid")
                TriArea.pop(0)
                TriArea.append("nothing! Make sure base plus side A is greater than side B. Invalid")
        else:
            return render(request, "tasks/triangle.html", {
                "form" : form
            })
    return render(request, "tasks/triangle.html", {
        "form" : TriangleForm(),
        "TriArea" : TriArea,
        "TriPerimeter" : TriPerimeter,
        "base" : (base + side_1) > side_2
    })
