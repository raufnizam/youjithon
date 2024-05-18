from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('pages/rules', views.rules, name='rules'),
   path('pages/faq', views.faq, name="faq"),
   path('pages/grading', views.grading, name="grading"),

   # Hackathons
   path('hackathon', views.hackathon, name='hackathon'),
   path('hackathon/add/', views.hackathon_add, name='hackathon_add'),
   path('hackathon/history', views.hackathon_history, name='hackathon_history'),
   path('hackathon/<int:hackathon_id>/edit/', views.hackathon_edit, name='hackathon_edit'),
   path('hackathon/<int:hackathon_id>/remove/', views.hackathon_remove, name='hackathon_remove')
]