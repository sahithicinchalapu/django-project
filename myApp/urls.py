from . import views
from django.urls import HomePageView, path

urlpatterns = [
  path("", HomePageView.as_view(), name="home"),
]