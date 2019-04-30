from django.shortcuts import render, get_object_or_404
from .models import TechType, Product, Review

# Create your views here.
def index (request):
    return render(request, 'techreviewapp/index.html')

def gettypes(request):
    types_list=TechType.objects.all()
    context={'types_list' : types_list }
    return render(request, 'techreviewapp/types.html', context=context)    

def getproducts(request):
    product_list=Product.objects.all()
    return render(request, 'techreviewapp/products.html', {'product_list': product_list})

def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)   
    reviews=Review.objects.filter(product=id)
    reviewcount=Review.objects.filter(product=id).count()
    context={
        'prod' : prod,
        'reviewcount' : reviewcount,
        'reviews' : reviews,
    }
    return render(request, 'techreviewapp/productdetails.html', context=context)