from django.urls import path
from . import views

urlpatterns = [
    path('bars/all_features', views.allBarFeatures, name="all_bar_features"),

    path('bars/bars_suggest', views.bars_suggest, name="bars_suggest"),
    path('bars/bars_search', views.bars_search, name="bars_search"),

    path('bars/casts_suggest', views.casts_suggest, name="casts_suggest"),
    path('bars/casts_search', views.casts_search, name="casts_search"),

    path('bars/casts_checkimage_exist', views.casts_checkimage_exist, name="casts_checkimage_exist"),
    path('bars/casts_checkcastimage_exist', views.casts_checkcastimage_exist, name="casts_checkcastimage_exist"),

    # path('bars/set_currentStoreId', views.set_currentStoreId, name="set_currentStoreId"),
    # path('bars/get_currentStoreId', views.get_currentStoreId, name="get_currentStoreId"),

    path('bars/get_currentStoreRooms', views.get_currentStoreRooms, name="get_currentStoreRooms"),
    path('bars/get_roomimages', views.get_roomimages, name="get_roomimages"),
]