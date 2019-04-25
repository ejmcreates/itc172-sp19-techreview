from django.shortcuts import render
from .models import TechType, Product, Review

# Create your views here.
def index (request):
    return render(request, 'techreviewapp/index.html')

def gettypes(request):
    types_list=TechType.objects.all()
    context={'types_list' : types_list }
    return render(request, 'techreviewapp/types.html', context=context)    
