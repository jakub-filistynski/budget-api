from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.finances.api.serializers import FinanceCreateSerializer
from apps.finances.models import Finance


class FinanceViewSet(CreateModelMixin, GenericViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceCreateSerializer
