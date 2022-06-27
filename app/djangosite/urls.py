"""djangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from hagelandse101 import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show_deelnemers, name="homepage"),
    path('controlpoints/', views.show_controlpoints,name="show-controlpoints"),
    path('search_deelnemers/', views.search_deelnemers,name="search-deelnemers"),
    
    path('deelnemers/<person_id>', views.show_deelnemer, name='show-deelnemer'),
    path('deelnemers/validate_persoon/', views.validate_persoon, name='validate_persoon'),
    path('deelnemers/delete_persoon/', views.delete_persoon, name='deletes_persoon'),
    path('tracking/', views.track, name='track'),
    
]

urlpatterns += staticfiles_urlpatterns()
