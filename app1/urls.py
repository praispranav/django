from django.urls import path
from  .import views
from .import views2

urlpatterns = [
    path('',views.index, name="Home-Login"),
    path('signup/', views.signup, name="SignUp"),
    path('profile/', views.profile, name="Profile"),
    path('profilesetup/', views.profilesetup, name="ProfileSetup"),
    path('insprofile/', views.instructorprofilesetup, name="Ins Profile"),
    path('logout/', views.logout_user, name="Logout"),

    path('courses/', views2.courses,name="Courses"),
    path('courses/<int:course_id>/', views2.lesson_view, name="Lesson"),
    path('courses/<int:course_id>/<int:lesson_id>/', views2.questionlist, name="Lesson"),
    path('courses/<int:course_id>/<int:lesson_id>/<int:question_id>/', views2.question_view, name="questions"),

]