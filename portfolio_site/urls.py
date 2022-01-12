"""portfolio_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.index, name='index')
Class-based views
    1. Add an import:  from other_app.views import index
    2. Add a URL to urlpatterns:  path('', index.as_view(), name='index')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from quote_generator import views
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

#Added for exchange_rate app
#from exchange_rate import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #path('', views.index, name='index'),
    
    #Added for exchange_rate app
    #path('exchange_rate/', views.index, name='index'),
    
    #path('about/', views.about, name='about'),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)