from django.urls import path
from blog.views import BlogList,BlogDetail

urlpatterns = [
    path('Blogs/', BlogList.as_view()),
    path('Blogs/<int:pk>/', BlogDetail.as_view()),
]