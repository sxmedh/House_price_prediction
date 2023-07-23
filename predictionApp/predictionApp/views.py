# created
from predictionApp.prediction import *
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def result(request):

    place = request.GET.get('place', 'default')
    bhk = int(request.GET.get('bhk', 'default'))
    bath = int(request.GET.get('bath', 'default'))
    balcony = int(request.GET.get('balcony', 'default'))
    sqft = int(request.GET.get('sqft', 'default'))
    area_type = request.GET.get('area_type', 'default')
    availability = request.GET.get('availability', 'default')
    num = predict(place, bhk, bath, balcony, sqft,
                  area_type, availability)

    if num < 0:
        params = {'result': "The data provided is not accurate."}
    else:
        params = {'result': num, 'place':
                  place, 'bhk': bhk, 'bath': bath, 'balcony': balcony, 'sqft': sqft,
                  'area_type': area_type, 'availability': availability}

    return render(request, 'result.html', params)
