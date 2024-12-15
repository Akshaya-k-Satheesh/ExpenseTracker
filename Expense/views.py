from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Expense.models import Category

from Expense.models import Expense

from Expense.models import users


# Create your views here.
def home(request):
    return render(request,'home.html')


# def add_category(request):
#     if(request.method=="POST"):
#         n=request.POST.get('n')
#         d=request.POST.get('d')
#         context={'categories':p}
#         c=Category.objects.create(name=n,description=d)
#         c.save()
#
#
#
#     return render(request,'add category.html',context)

 # Assuming you have a CategoryForm to handle category input

def add_category(request):
    # Initialize the context variable before using it
    context = {}

    if request.method == 'POST':
        form=Category(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            context['message'] = "Category added successfully!"
            return render(request, 'add category.html', context)
    else:
        form = Category()

    context['form'] = form
    return render(request, 'add category.html', context)



class ExpenseForm:
    pass


def addexpense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new page (for example, a page showing the expense list)
            return redirect('Expense:viewexpense')  # Make sure this view exists
    else:
        form = ExpenseForm()

    return render(request, 'addexpense.html', {'form': form})
#
#
# def add_expense(request):
#     if (request.method=="POST"):
#         a=request.POST.get('a')
#         d=request.POST.get('d')
#         da=request.POST.get('da')
#         ca=request.POST.get('ca')
#         cat=Category.objects.get(name=ca)
#         e=Expense.objects.create(amount=a,description=d,date=da,category=cat)
#         e.save()
#         return render(request,'viewexpense.html')

# def viewexpense(request):
#     if(request.method=="POST"):
#         k=Expense.objects.all()
#         context= {'expense':k}
#         return render(request,'viewexpense.html',context)
def viewexpense(request):
    e=Expense.objects.all()
    if not e:
        return redirect('shop:viewexpense')
    return render(request, 'viewexpense.html', {'expenses': e})



def viewusers(request):
    k=users.objects.all()
    context={'user':k}
    return render(request,'viewuserdetail.html',context)

def register(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        if(p==cp):
           u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
           u.save()

    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('Expense:home')
        else:
            messages.error(request,"invalid credentials")
    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect('Expense:login')



