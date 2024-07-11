from django.shortcuts import render, redirect
from car_app.models import CarModel, Order
from brand_app.models import Brand
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.




def home(request,brand_slug = None):
    data = CarModel.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug= brand_slug)
        data = CarModel.objects.filter(car_brand = brand)
    brand = Brand.objects.all()
    return render(request, 'home.html', {'car': data, 'brand': brand})



@login_required
def buy_car(request, id):
    car = CarModel.objects.get(id=id)
    if car.car_quantity > 0:
        order = Order.objects.create(user=request.user, car=car, quantity=1)
        car.car_quantity -= 1
        car.save()
        messages.success(
            request, f"You have successfully purchased {car.car_name}.")
    else:
        messages.error(request, f"Sorry, {car.car_name} is out of stock.")

    return redirect('home')


