from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('articles/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('',views.homepage),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
