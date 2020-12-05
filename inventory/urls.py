from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^inventory', index, name='index'),
    url(r'^foods$', display_foods, name="display_foods"),
    url(r'^drinks$', display_drinks, name="display_drinks"),
    url(r'^others$', display_others, name="display_others"),

    url(r'^add_food$', add_food, name="add_food"),
    url(r'^add_drink$', add_drink, name="add_drink"),
    url(r'^add_other$', add_other, name="add_other"),

    url(r'^foods/edit_item/(?P<pk>\d+)$', edit_food, name="edit_food"),
    url(r'^drinks/edit_item/(?P<pk>\d+)$', edit_drink, name="edit_drink"),
    url(r'^others/edit_item/(?P<pk>\d+)$', edit_other, name="edit_other"),

    url(r'^foods/delete/(?P<pk>\d+)$', delete_food, name="delete_food"),
    url(r'^drinks/delete/(?P<pk>\d+)$', delete_drink, name="delete_drink"),
    url(r'^others/delete/(?P<pk>\d+)$', delete_other, name="delete_other")

]
