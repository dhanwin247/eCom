from django.urls import path
from merchant import views 
from accounts import views as account_views

#TEMPLATE URLS
app_name = 'merchant'

urlpatterns = [
    path('',views.merchant_login, name='merchant_login'),
    path('register',views.register_product, name='register_product'),
    path('merchant_login/',views.merchant_login, name='merchant_login'),
    path('logout/',views.merchant_logout,name='logout')
    # path('about/',account_views.about, name='about'),
]
