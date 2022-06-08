from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('solutions', views.solutions, name='solutions'),
    path('contact', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogDetails/<blogs_id>', views.blogDetails, name='blogDetails'),
    path('comments/<blogs_id>', views.comments, name='comments'),
    path("addMailingList/<reverse>", views.addMailingList, name="addMailingList"),
    path("sendMails/", views.sendMails, name="sendMails"),
]
