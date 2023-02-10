from django.urls import path,include
from .import views

urlpatterns =[
    path('user_signup/',views.user_signup,name = "user_signup"),
    path('',views.user_signin,name = 'user_signin'),
    path('admin_login/',views.admin_login,name = 'admin_login'),
    path('admin_userlist/',views.admin_userlist,name = 'admin_userlist'),
   # path('accounts/', include('allauth.urls')),
   path('admin_addproducts/',views.admin_addproducts,name = 'admin_addproducts'),
   path('admin_productslist/',views.admin_productslist,name = 'admin_productslist'),
   path('shop_list_left_books/',views.shop_list_left_books,name = 'shop_list_left_books'),
   path('product_detail',views.product_detail,name = 'product_detail'),
   path("index_3_home/",views.index_3_home,name = "index_3_home"),
   path('admin_logout/',views.admin_logout,name = 'admin_logout')
  
]