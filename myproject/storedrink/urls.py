from django.urls import path, include

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('login/', views.login, name="login"),
	path('product/', views.product, name="product"),
	path('productdetail', views.productdetail, name="productdetail"),
	path('located/', views.located, name="located"),
	path('cart/', views.cart, name="cart"),
	path('submitorder/', views.submitorder, name="submitorder"),
	path('checkout/', views.checkout, name="checkout"),
    path('oauth/', include('social_django.urls', namespace='social')),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]