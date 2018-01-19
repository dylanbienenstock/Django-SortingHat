# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from random import randint
from models import *

def index(request):
	context = {
		"red": House.objects.get(id=1).students.all(),
		"blue": House.objects.get(id=2).students.all(),
		"green": House.objects.get(id=3).students.all(),
		"purple": House.objects.get(id=4).students.all()
	}

	print(context["red"])

	return render(request, "index.html", context)

def sort(request):
	if request.method == "POST":
		name = request.POST["name"]
		new_house = House.objects.get(id=randint(1, 4))

		Student.objects.create(name=name, house=new_house)

		return redirect("/")