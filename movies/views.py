from django.shortcuts import render


def index(req):
    return render(req, 'index.html')


def topten(req):
    return render(req, 'topten.html')
