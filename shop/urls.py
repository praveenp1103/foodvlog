from django.urls import path
from . import views
from .views import ProdDetails


urlpatterns = [
    path('', views.home, name='hm'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),
    # path('<slug:c_slug>/<slug:product_slug>', views.ProdDetails, name='details'),
    path('category/<str:c_slug>/<str:Product_slug>/', ProdDetails, name='details'),
    path('search',views.searching,name='search'),

]
