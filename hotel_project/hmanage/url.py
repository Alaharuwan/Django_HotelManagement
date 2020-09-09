from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hmanage-home'),
    path('addResPackage', views.addrespackage, name='hmanage-addrespackage'),
    path('viewResPackage', views.listpackage, name='hmanage-listpackage'),
    path('addres', views.addres, name='hmanage-addres'),
    path('editResPackage', views.editResPackage, name='hmanage-addres'),
    path('viewres',views.listres, name='hmanage-listres'),
    path('editres',views.editres, name='hmanage-editres')

    
    
    
]
