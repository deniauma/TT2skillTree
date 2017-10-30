# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Skill

def index(request):
    red_skills = Skill.objects.filter(branch="Red")
    yellow_skills = Skill.objects.filter(branch="Yellow")
    blue_skills = Skill.objects.filter(branch="Blue")
    green_skills = Skill.objects.filter(branch="Green")
    skills = {"red": red_skills, "yellow": yellow_skills, "blue": blue_skills, "green": green_skills}
    return render(request, 'skills/index.html', skills)

def getskills(request):
    data = serializers.serialize("json", Skill.objects.all())
    return JsonResponse({'skills': data})

def getredskills(request):
    data = serializers.serialize("json", Skill.objects.filter(branch="Red"))
    return JsonResponse({'skills': data})

def getyellowskills(request):
    data = serializers.serialize("json", Skill.objects.filter(branch="Yellow"))
    return JsonResponse({'skills': data})

def getblueskills(request):
    data = serializers.serialize("json", Skill.objects.filter(branch="Blue"))
    return JsonResponse({'skills': data})

def getgreenskills(request):
    data = serializers.serialize("json", Skill.objects.filter(branch="Green"))
    return JsonResponse({'skills': data})