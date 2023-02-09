from django.urls import path,include
from .import views

urlpatterns =[
    path('user_signup/',views.user_signup,name = "user_signup"),
    path('',views.user_signin,name = 'user_signin'),
    path('admin_login/',views.admin_login,name = 'admin_login'),
    path('admin_userlist',views.admin_userlist,name = 'admin_userlist'),
   # path('accounts/', include('allauth.urls')),
   path('admin_addproducts/',views.admin_addproducts,name = 'admin_addproducts'),
   path('admin_productslist',views.admin_productslist,name = 'admin_productslist'),
  
]