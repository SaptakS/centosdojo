# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render

def homepage(request):
    return JsonResponse({"message": "Hello World where CentOS Dojo in World"})
