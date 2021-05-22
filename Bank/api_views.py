from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from .serializers import BankSerializer
from .models import Bank

class BanksPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class BankList(ListAPIView):
    queryset = Bank.objects.all().order_by('ifsc')
    serializer_class = BankSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('branch','city','district','ifsc','bank_id','state','address',)
    pagination_class = BanksPagination

class BankBranchList(ListAPIView):
    queryset = Bank.objects.all().order_by('ifsc')
    serializer_class = BankSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('branch',)
    pagination_class = BanksPagination

