from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('dashboard/', views.dashboard, name="dashboard"),
#	path('<int:id>/', views.product_detail_view, name='product-detail'),
    path('<int:id>/', views.dynamic_lookup_view, name='product'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path("test/", views.test, name="test"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
	path('create_order/', views.createOrder, name="create_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

]



###test