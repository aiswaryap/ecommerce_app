from django.contrib import messages
from django.shortcuts import render, redirect
# from . models import User
from django.contrib.auth.models import User, auth

# Create your views here.
def registration(request):
    return render(request, 'registration.html')

def register(request):
    print("hello")
    if request.method == "POST":
        first_name=request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1= request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        # user=User.objects.create(username=username,first_name=first_name,last_name=last_name,password1=password1,email=email)
        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, password=password1, email=email)
        user.save();

        print("user created")
        print("hello reg")
        return redirect('ecommerceapp:allProdCat')
    else:
        return render(request,'registration.html')


def login(request):
    print("hello")
    if request.method == "POST":
        username = request.POST['username']
        password1= request.POST['password1']
        # user=User.objects.create(username=username,first_name=first_name,last_name=last_name,password1=password1,email=email)
        # user.save();
        # if User.objects.filter(username=username, password1=password1).exists():
        #     print("successfully loggedin!!")
        #     return redirect('ecommerceapp:allProdCat')
        # else:
        #     print("invalid login credentials")
        #     return render(request,'login.html')
        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('ecommerceapp:allProdCat')
        else:
            messages.info(request, 'invalid details')
            # return redirect('login', user="username")
            return render(request, 'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('ecommerceapp:allProdCat')
