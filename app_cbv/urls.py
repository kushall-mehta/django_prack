from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_book',views.BookCreate.as_view(),name='create_book'),
    path('book/<int:pk>',views.BookDetail.as_view(),name='book_details'),
    path('login/', LoginView.as_view(template_name='app_cbv/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my_view',views.my_view,name='my_view'),
]