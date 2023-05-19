from django.urls import path
from .views import home, contacto, profesionales

urlpatterns = [
    path('home/', home,name="home"),
    path('', home,name="home"),
    path('contacto/', contacto, name= "contacto"),
    path('profesionales/', profesionales, name= "profesionales")
    
]