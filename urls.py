
#from django.conf.urls import url
#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path(r'admin/', admin.site.urls),
      path('',views.homepage,name='home'),
    path('contact/',views.contact),
    path('count',views.count,name='count')
]
