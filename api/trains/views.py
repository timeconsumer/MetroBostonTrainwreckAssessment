from django.shortcuts import render
from django.http import HttpResponse
from .models import TrainLine
from rest_framework.decorators import api_view

def index(request):
    train_lines = TrainLine.objects.all()
    output = '<br>'.join([tl.__str__() for tl in train_lines])
    return HttpResponse(output)

@api_view(['GET'])
def detail(request, train_line_id):
    response = f'The train line {train_line_id} is this.'
    return HttpResponse(response)
