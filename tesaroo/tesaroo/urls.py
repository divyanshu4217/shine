
from django.contrib import admin
from django.urls import path,include
from .views import tweek_view,homepage_view,about_view,anti_view,form_view
app_name = 'tesaroo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweek/',tweek_view,name='tweek'),
    path('/',homepage_view),
    path('about/',about_view),
    path('anti/',anti_view),
    path('signup/',form_view)
]
