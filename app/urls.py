from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.PlotCreateView.as_view(), name='plot-create'),
    path('list/', views.PlotListAPIView.as_view(), name='plot-list'),
]
