from itertools import count

from django.shortcuts import render, redirect

from maain_app.models import Customer
from maain_app.my_forms import CustomerForm


# Create your views here.
def home(request):
    if request.method == "POST":
        names= request.POST['names']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        weight = request.POST['weight']
        height = request.POST['height']
        gender = request.POST['gender']
        Customer.objects.create(names=names, email=email, phone=phone, password=password, weight=weight, height=height, gender=gender)
        count = Customer.objects.all().count()
        print(f"{count} Customers")
    return render(request, 'home.html')


def show(request):
    data = Customer.objects.all().order_by('-id')
    return render(request, 'show.html', {"data": data})


def delete(request, id):
    user = Customer.objects.get(id=id)
    user.delete()
    return redirect('show-page')


def details(request, id):
    user = Customer.objects.get(id=id)
    return render(request, 'Details.html', {"user": user})


def add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        pass
    else:
        form = CustomerForm()
    return render(request, 'forms.html', {"form": form})