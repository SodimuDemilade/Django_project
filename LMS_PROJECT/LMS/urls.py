from django.urls import path
from LMS import views

urlpatterns = [
    path('L/Cont/<uuid:course_id>/<str:page_id>/', views.LMS_Content.as_view()),
]
