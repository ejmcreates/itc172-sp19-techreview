from django.shortcuts import render, get_object_or_404
from .models import TechType, Product, Review
from .forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required

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

@login_required
def newProduct(request):
    form=ProductForm
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ProductForm()
    else:
        form=ProductForm()
    return render(request, 'techreviewapp/newproduct.html', {'form':form})    

@login_required
def newReview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'techreviewapp/newreview.html', {'form':form})

def loginmessage(request):
    return render(request, 'techreviewapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'techreviewapp/logoutmessage.html') 



