from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for API views
router = DefaultRouter()
router.register(r'api/students', views.StudentViewSet)

urlpatterns = [

    path('api/', include(router.urls)),
    path('api/token/', views.token_obtain_pair, name='api_token_obtain_pair'),

    
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
]
