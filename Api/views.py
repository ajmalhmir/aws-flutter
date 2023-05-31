from .models import Books
from .serializers import BooksSerializers
from rest_framework.generics import ListAPIView

class BooksList(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
