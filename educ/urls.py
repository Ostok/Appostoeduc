from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="inicio"),
    path('bio1',views.bio1, name="bio1"),
    path('bio2',views.bio2, name="bio2"),
    path('bio3',views.bio3, name="bio3"),
    path('eco4',views.eco4, name="eco4"),
    path('bio1eje1',views.bio1eje1, name='bio1eje1'),
    path('bio1eje2',views.bio1eje2, name='bio1eje2'),
    path('bio1eje3',views.bio1eje3, name='bio1eje3'),
    path('contacto',views.contacto, name='contacto'),
]
