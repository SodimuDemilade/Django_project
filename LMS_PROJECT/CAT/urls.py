from django.urls import path
from CAT import views

urlpatterns = [
    #path('CAT/', views.CAT_CourseViewSet.list),
    #path('CAT/', views.CAT_CourseListView.as_view()),
    #path('CAT/<uuid:id>/', views.CAT_CourseViewSet.retrieve),
    #path('CAT/create', views.CAT_Course_TeamViewSet.create),

    path('I/CourList', views.CAT_CourseListCreateView.get),
    path('I/Cour/create', views.CAT_CourseListCreateView.post),
    path('I/Cour/edit/<uuid:id>/', views.CAT_CourseListCreateView.put),
    path('I/Cour/<uuid:id>/', views.CAT_CourseDetailEditView.get),
    path('I/Grad/<uuid:id>/', views.CAT_GradingEditView.post),
    path('I/Team/<uuid:id>/', views.CAT_TeamEditView.post),
    path('I/Grou/create', views.CAT_GroupEditView.post),
    path('I/Grou/edit/<uuid:id>/', views.CAT_GroupEditView.put),
    path('I/Grou/<uuid:id>/', views.CAT_GroupEditView.get),
    path('I/Resou/create', views.CAT_ResourceEditView.post),
    path('I/Resou/<uuid:id>/', views.CAT_ResourceEditView.put),
    path('I/Cont/<uuid:id>/', views.CAT_ContentEditView.retrieve_content),
    path('Courselist', views.CAT_CourseListCreateView.get_all_courses_with_instructor),
    path('choices', views.LookupAndChoiceView.choices),
]
