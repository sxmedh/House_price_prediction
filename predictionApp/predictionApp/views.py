# created
from predictionApp.prediction import *
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def result(request):

    place = request.GET.get('place', 'default')
    bhk = request.GET.get('bhk', 'default')
    bath = request.GET.get('bath', 'default')
    balcony = request.GET.get('balcony', 'default')
    sqft = request.GET.get('sqft', 'default')
    area_type = request.GET.get('area_type', 'default')
    availability = request.GET.get('availability', 'default')
    num = predict(place, bhk, bath, balcony, sqft,
                  area_type, availability)
    params = {'result': num}

    return render(request, 'result.html', params)
