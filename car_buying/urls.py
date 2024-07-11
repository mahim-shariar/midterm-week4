"""
URL configuration for car_buying project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('car_app.urls')),
    path('buyer/', include('buyer.urls')),
    path('', views.home,name='home'),
    path('buy_car/<int:id>/', views.buy_car, name='buy_car'),
    path('brand/<slug:brand_slug>/', views.home,name='brand_wise_car'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)