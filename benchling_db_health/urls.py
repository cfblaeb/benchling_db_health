from django.contrib import admin
from django.urls import path
from backend.views import ChartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ChartView.as_view(team_name="CHO Cell Line Engineering & Design")),
]
