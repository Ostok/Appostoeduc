from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="inicio"),
    path('bio1',views.bio1, name="bio1"),
    path('bio2',views.bio2, name="bio2"),
    path('bio3',views.bio3, name="bio3"),
    path('eco4',views.eco4, name="eco4"),
]
