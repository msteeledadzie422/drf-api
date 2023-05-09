from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Snack
from .serializer import SnackSerializer


class SnackList(ListAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
