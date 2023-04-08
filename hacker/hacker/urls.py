"""hacker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from quiz import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router.register("api/v1/categories",views.CategoriesView,basename="categories")
router.register("api/v1/questions",views.QuestionsView,basename="questions")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/token/",TokenObtainPairView.as_view()),
    path("api/v1/token/refresh/",TokenRefreshView.as_view()),
    path("web/",include("quizweb.urls"))
    #path("api/v1/token/",ObtainAuthToken.as_view()),
]+router.urls