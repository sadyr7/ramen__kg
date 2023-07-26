from rest_framework import permissions
from rest_framework import viewsets
from history_orders.models import History
from history_orders.serializers import HistorySerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


