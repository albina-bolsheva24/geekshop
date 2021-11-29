from django.urls import path
from adminapp import views as admin_views


app_name = 'adminapp'

urlpatterns = [
    path('user/create/', admin_views.user_create, name='user_create'),
    path('user/', admin_views.UserListView.as_view(), name='users_list'),
    path('user/update/<ink:pk>/', admin_views.user_update, name='user_update'),
    path('user/delete/<ink:pk>/', admin_views.user_delete, name='user_delete'),

    path('categories/create/', admin_views.category_create, name='category_create'),
    path('categories/', admin_views.categories, name='category_list'),
    path('categories/update/<ink:pk>/', admin_views.category_update, name='category_update'),
    path('categories/delete/<ink:pk>/', admin_views.category_delete, name='category_delete'),

    path('products/create/<int:pk>/', admin_views.ProductCreateView.as_view(), name='product_create'),
    path('products/', admin_views.ProductsListView.as_view(), name='products_list'),
    path('products/update/<ink:pk>/', admin_views.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<ink:pk>/', admin_views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/detail/<ink:pk>/', admin_views.ProductDetailView.as_view(), name='product_detail'),
]
