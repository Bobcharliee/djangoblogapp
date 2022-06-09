from django.urls import path
from .views import Bloglist, Blogdetail

urlpatterns = [
    path('<int:pk>/', Blogdetail.as_view(), name='Blogdetail'),
    path('', Bloglist.as_view(), name= 'Bloglist'),
]