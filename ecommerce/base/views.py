from django.shortcuts import render,redirect
from category.models import *
from Staticpage.models import Slider
from product.models import Product

# Create your views here.

def index(request):
    categories = Category.objects.prefetch_related('sub_categories').all()
    slider = Slider.objects.all()
    #request.session['test'] = 10
    product = Product.objects.all()[:10]
    context = {
        'sliders':slider,
        'categories':categories,
        'pro':product,
    }
    return render(request,'index.html',context)


def add_to_wishlist(request,id):
    if request.method == "POST":
        if not request.session.get('wishlist'):
            request.session['wishlist'] = list()
        else:
            request.session['wishlist'] = list(request.session['wishlist'])

        items = next((item for item in request.session['wishlist'] if item['id']==id),False)


    add_data = {
        'id':id

    }
    if not items:
        request.session['wishlist'].append(add_data)
        request.session.modifier = True
    return redirect('index')    

def deletewishlist(request, id):
    customer=request.user.customer
    Wishlist.objects.filter(customer_id=customer.id, product=Product.objects.get(id=id)).delete()
    messages.success(request, 'Product Remove From Wishlist...')
    return redirect('/wishlist')