# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
from random import randint

import md5

def index(request):
	context = {
		"red": House.objects.get(id=1).students.all(),
		"blue": House.objects.get(id=2).students.all(),
		"green": House.objects.get(id=3).students.all(),
		"purple": House.objects.get(id=4).students.all()
	}

	return render(request, "index.html", context)

def sort(request):
	if request.method == "POST":
		name = request.POST["name"]

		# Sorts based on student's name's md5 hash
		# converted to base 10, then modulus 4
		house_id = (int(md5.new(name).hexdigest(), 16) % 4) + 1
		new_house = House.objects.get(id=house_id)

		Student.objects.create(name=name, house=new_house)

		return redirect("/")