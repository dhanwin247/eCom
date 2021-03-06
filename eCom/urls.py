"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from accounts import views as account_views
from merchant import views as merchant_views
from products import urls as produrls
from merchant import urls as mercurls
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mdb/',views.mdb_home_page_view,name="mdb_home_page"),
    path('',include('accounts.urls',namespace='accounts')),
    path('logout/',account_views.user_logout,name='user_logout'),
    path('products/',include(produrls,namespace='products')),
    path('merchant/',include(mercurls,namespace='merchant')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
