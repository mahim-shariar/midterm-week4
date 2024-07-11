from django.db import models
from brand_app.models import Brand
from django.contrib.auth.models import User

# Create your models here.

class CarModel(models.Model):
    car_name = models.CharField(max_length=50)
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to='car_app/media/car_images')
    car_discription = models.TextField()
    car_price = models.IntegerField()
    car_quantity = models.IntegerField()
    


    def __str__(self):
        return self.car_name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    

class Comment(models.Model):
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'Comments by {self.name}'