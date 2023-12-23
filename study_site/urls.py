"""
URL configuration for study_si project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from homepage.views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path("tutors", tutors, name="tutors"),
    path("tutors/<str:profes>", tutors, name="tutor"),
    path("customers", customers, name="customers"),
    path("timetable", timetable, name="timetable"),
    path("generate", generate, name="generate"),
    path("login", sign, name="login"),
    path("logout", logout_user, name="logout"),
    path("admin", admin.site.urls),
    path("appointment/<str:profes>/<int:id>", appointment, name='appointment'),
    path("dwlpdf", download_pdf, name="dwlpdf"),
    path("dwlcsv", download_csv, name="dwlcsv"),
    path("new_tut", new_tutor, name="new_tut"),
    path("change_homeworks/<int:id>", change_homeworks, name="change_homeworks")
]
