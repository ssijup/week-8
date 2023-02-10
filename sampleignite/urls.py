
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('user_signin/',TemplateView.as_view(template_name='products/user_signin.html'),name='user_signin'),
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('accounts/', include('allauth.urls')),
    

            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

