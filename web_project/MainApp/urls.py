from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home , name="home"),
    path('services', views.services , name="services"),
    path('works', views.works , name="works"),
    path('about', views.about , name="about"),
    path('contact' ,views.contact , name="contact")
  
    
]  + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)