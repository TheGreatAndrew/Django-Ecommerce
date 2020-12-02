from django.urls import path
from . import views

urlpatterns = [

            path("", views.Coupons_Ads_index, name="Coupons_Ads_index")

]