from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Userdetails,Products
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage


# Create your views here.



#********USER REGIDTRATION***************************************
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
def user_signin(request):
    if request.method == "POST":
        uemail=request.POST['user_email']
        upassword=request.POST['user_password']
        user=Userdetails.objects.filter(user_email=uemail,user_password=upassword)
        if user is not None:
            return render(request,'shop-list-left-books.html')
        else:
            return HttpResponse('PASSWORD INCORRECT')
    else:
        print('sigin')
        return render(request,'admin_productslist.html')

def admin_login(request):
    if request.method == 'POST':
        aemail = request.POST.get('admin_email')
        apassword = request.POST.get('admin_password')
        user = authenticate(request,password = apassword,email = aemail)
        if user is  None:
            return redirect('admin_userlist')
        else:
            return HttpResponse('invalid pass or uname')
    return render(request,'admin_login.html')


def admin_userlist(request):
    userlist = Userdetails.objects.all()
    return render(request,'admin_userlist.html',{'tablelist' : userlist})


def admin_products(request):
    return render(request,'admin_productslist.html')


def admin_addproducts(request):
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


def admin_productslist(request):
    print('hii nprinttttttt')
    list =Products.objects.all()
    return render(request,'admin_productslist.html',{'list' : list})
    