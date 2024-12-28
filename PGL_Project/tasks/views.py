# Stuff I imported from the python library:

from django.shortcuts import render
from django import forms
from math import sqrt, pi
from decimal import *

# The lists to tell the area and perimeter of shapes:

SquareArea = [""]
SquarePerimeter = [""]
RectArea = [""]
RectPerimeter = [""]
TriArea = [""]
TriPerimeter = [""]
CirArea = [""]
CirPerimeter = [""]
base = 0
side_1 = 0
side_2 =0
 
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

class CircleForm(forms.Form):
    radius = forms.FloatField(label="Radius", min_value=0.000000000000000001, max_value=99999999999999, required=False)

# My functions that run the pages:

def start(request):
    return render(request, "tasks/start.html")
    # Shapes page:

def index(request):
    return render(request, "tasks/index.html", {
    })

    # Square page:

def square(request):
    SquareArea = [""]
    SquarePerimeter = [""]
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
    RectArea = [""]
    RectPerimeter = [""]
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

    # Triangle page:

def triangle(request):
    TriArea = [""]
    TriPerimeter = [""]
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
                z = base
                y = side_1
                x = side_2
                a = 0.25 * sqrt((z + y + x) * (-z + y + x) * (z - y + x) * (z + y - x))
                if a != 0:
                    TriPerimeter.pop(0)
                    TriPerimeter.append(b)
                    TriArea.pop(0)
                    TriArea.append(a)
                else:
                    TriPerimeter.pop(0)
                    TriPerimeter.append("nothing! Make sure one side plus another side is greater than the third side. Invalid")
                    TriArea.pop(0)
                    TriArea.append("nothing! Make sure one side plus another side is greater than the third side. Invalid")
            except ValueError:
                TriPerimeter.pop(0)
                TriPerimeter.append("nothing! Make sure one side plus another side is greater than the third side. Invalid")
                TriArea.pop(0)
                TriArea.append("nothing! Make sure one side plus another side is greater than the third side. Invalid")
        else:
            return render(request, "tasks/triangle.html", {
                "form" : form
            })
    return render(request, "tasks/triangle.html", {
        "form" : TriangleForm(),
        "TriArea" : TriArea,
        "TriPerimeter" : TriPerimeter,
    })

def circle(request):
    CirArea = [""]
    CirPerimeter = [""]
    if request.method == "POST":
        form = CircleForm(request.POST)
        if form.is_valid():
            radius = form.cleaned_data["radius"]
            CirPerimeter.pop(0)
            CirPerimeter.append(radius * radius * 3.141259)
            CirArea.pop(0)
            CirArea.append(radius * 2 * 3.141259)
        else:
            return render(request, "tasks/circle.html", {
                "form" : form
            })
    return render(request, "tasks/circle.html", {
        "form" : CircleForm(),
        "CirArea" : CirArea,
        "CirPerimeter" : CirPerimeter
    })
