from django.urls import path
from CER import views

urlpatterns = [
    path('Cour/<str:new>/<str:top>/<str:featured>/<str:subcategory_id>/<str:learning_style>/<str:price>/<str:institution_id>/<str:search_text>/', views.coursedetail.as_view()),
]
