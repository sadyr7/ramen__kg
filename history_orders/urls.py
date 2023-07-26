from django.urls import path, include
from rest_framework.routers import DefaultRouter
from history_orders.views import HistoryViewSet

oppa = DefaultRouter()
oppa.register('', HistoryViewSet)

urlpatterns = [
    path('', include(oppa.urls)),
]
