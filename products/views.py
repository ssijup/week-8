from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Userdetails,Products
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control


# Create your views here.



#********USER REGIDTRATION***************************************
@cache_control(no_cache=True)
def user_signup(request):
    if request.method == 'POST':
        uname = request.POST.get('user_name')
        uemail = request.POST.get('user_email')
        upassword1 = request.POST.get('user_password1')
        upassword2 = request.POST.get('user_password2')
        if upassword1 != upassword2:
            return HttpResponse('retype the password')
        else:
            my_user = Userdetails.objects.create(user_name=uname,user_email=uemail,user_password=upassword1)
            my_user.save()
            return redirect('user_signin')
    else:
        print('not post')
        return render(request,'user_signup.html')



#*****USER LOGIN**********************************************************
@cache_control(no_cache=True)
def user_signin(request):
    if request.method == "POST":
        uemail=request.POST['user_email']
        upassword=request.POST['user_password']
        user=Userdetails.objects.filter(user_email=uemail,user_password=upassword)
        if user is not None:
            return render(request,'index_3_home.html')
        else:
            return HttpResponse('PASSWORD INCORRECT')
    else:
        print('sigin')
        return render(request,'user_signin.html')


@cache_control(no_cache=True)
def admin_login(request):
    error_msg = None
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('admin_userlist')
        return render(request, 'admin_login.html')
    elif request.user.is_authenticated:
        return redirect('admin_userlist')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            password = request.POST.get('password')

            user = authenticate(request,username =name, password=password)

            if user is not None:
                login(request, user)
                return redirect('admin_userlist')
            else:
                error_msg = 'invalid Name or password..!'

    return render(request, 'admin_login.html', {'error': error_msg})
        



@cache_control(no_cache=True)
def admin_logout(request):
        logout(request)
        return redirect('admin_login')



@cache_control(no_cache=True)
def admin_userlist(request):
    if request.user.is_authenticated:
        userlist = Userdetails.objects.all()
        return render(request,'admin_userlist.html',{'tablelist' : userlist})



@cache_control(no_cache=True)
def admin_products(request):
    if 'email' in request.session:
        if 'email' in request.session:
            return render(request,'admin_productslist.html')



@cache_control(no_cache=True)
def admin_addproducts(request):
    if 'email' in request.session:
        if request.method == 'POST' :
            # myfile =request.FILES.get('myfile')
            # fs = FileSystemStorage()
            # filename = fs.save(myfile.book_title,myfile)
            # url = fs.url(filename)

            # book_title = request.POST.get('book_title')
            # author = request.POST.get('author')
            # description = request.POST.get('description')
            # image = request.FILES.get('myfile')
            # price = request.POST.get('price')
            new_product = Products(
                book_title = request.POST.get('book_title'),
                author = request.POST.get('author'),
                picture = request.FILES.get('myfile'),
                description = request.POST.get('description'),
                price = request.POST.get('price')
            )
            new_product.save()
            return redirect('admin_productslist')
        else:
            return render(request,'admin_addproducts.html')



@cache_control(no_cache=True)
def admin_productslist(request):
    if 'email' in request.session:
        list =Products.objects.all()
        return render(request,'admin_productslist.html',{'list' : list})

@cache_control(no_cache=True)
def shop_list_left_books(request):
    list =Products.objects.all()
    return render(request,'shop-list-left-books.html',{'list' : list})



@cache_control(no_cache=True)
def product_detail(request):
    list =Products.objects.all()
    return render(request,'product_details.html',{'list' : list})



@cache_control(no_cache=True)
def index_3_home(request):
    return render(request,"index_3_home.html")
