from itertools import count

from django.shortcuts import render

from maain_app.models import Customer


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
    data = Customer.objects.all()
    return render(request, 'show.html', {"data": data})