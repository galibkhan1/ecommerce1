from email.headerregistry import Address
from msilib.schema import Registry
from unicodedata import category
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from itsdangerous import Serializer
from more_itertools import quantify
from ecommerce.models import  Category , upload_product , order,registeration,demodb
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import routers , serializers,viewsets

from .serializers import demo_rest

from django.core.mail import send_mail
# Create your views here.


def index(request):
    if request.method == "POST":
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus')
        cart_id = request.session.get('cart')
        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:
                    cart_id[product_id] = quantity + 1
            else:
                cart_id[product_id] = 1
        else:
            cart_id = {}
            cart_id[product_id] = 1
        request.session['product_id'] = product_id
        request.session['cart'] = cart_id
        

    path = upload_product.objects.all()
    cat = Category.objects.all()
    cate_id = request.GET.get('category')
    if cate_id:
        path =upload_product.objects.filter(category_id = cate_id)
    else:
        path = upload_product.objects.all()

    return render(request, 'home.html',{'path':path, 'cat':cat})


def contact(request):
    path = upload_product.objects.all()
    cat = Category.objects.all()
    cate_id = request.GET.get('category')
    if cate_id:
        path =upload_product.objects.filter(category_id = cate_id)
    else:
        path = upload_product.objects.all()
    return render(request, 'contact.html',{'path':path, 'cat':cat})


def signup(request):
    if request.method == "POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        userdata = registeration(firstname=firstname, lastname=lastname, username=username, email= email, password=make_password(password), gender=gender, phone=phone)
        userdata.save()

        return redirect('home')


def login_info(request):
    error_msg = None

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = registeration.objects.get(email =email)
        if data:
            request.session['email'] = email
            request.session['cust_id'] = data.id
            request.session['gender'] = data.gender
            request.session['username'] = data.username
            request.session['lastname'] = data.lastname
            request.session['firstname'] = data.firstname
            request.session['phone'] = data.phone

            
            return redirect('home')
        return redirect('home.html')
        # try:
        #     fetch_email = register.objects.get(email=email)
        #     if (fetch_email.email == email):
        #         flag = check_password(password, fetch_email.password)
        #         if flag:
        #             request.session['email'] = fetch_email.email
        #             print(request.session.email)
        #             request.session['customer_id'] = fetch_email.id
        #             return redirect('home')
        #         else:
        #             error_msg = "Please Enter valid password"
        #             return render(request, 'home.html', {'error_msg': error_msg})
        # except:
        #     error_msg = "Please Enter valid  Email"
        #     return render(request, 'home.html', {'error_msg': error_msg})

        # return HttpResponse(fetch_email.email, fetch_email.password)

def cart(request):
    x = list(request.session.get('cart').keys())
    cart_pro = upload_product.objects.filter(id__in = x)
    return render(request,'cart.html',{'cart_pro':cart_pro,'x':x})

    
def checkout(request):
    if request.method=="POST":
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        customer_id=request.session.get("cust_id")
        cart=request.session.get("cart")
        product=upload_product.objects.filter(id__in=list(cart.keys()))
        for pro in product:
            orderdtls=order(
                customer=registeration(id=customer_id),
                product=pro,
                price=pro.price,
                quantity=cart.get(str(pro.id)),
                address=address,
                phone=phone
            ) 
            orderdtls.save()
        request.session['cart']={}  
    return redirect('cart')



def logout(request):
    request.session.clear()
    return redirect('contact')

def ordersdtls(request):
    customer=request.session.get('cust_id')
    orders=order.objects.filter(customer=customer).order_by('-date')
    return render(request,'order.html',{'order':orders})    
class demo_REST(viewsets.ModelViewSet):
    queryset = demodb.objects.all()
    serializer_class =demo_rest

# send_mail{
#     'subject here'
# }