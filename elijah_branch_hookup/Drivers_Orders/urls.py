from django.urls import path
from . import views

urlpatterns = [

            path("", views.Drivers_Orders_index, name="Drivers_Orders_index"),
            path("<int:pk>/", views.Drivers_Orders_detail, name="Drivers_Orders_detail")

]