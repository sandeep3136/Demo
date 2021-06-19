from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("addpost", views.addPosts, name='add'),
    path("visitpost", views.visitpost, name='visitpost')

]