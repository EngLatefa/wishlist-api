from items.models import Item, FavoriteItem
from rest_framework.generics import (
	 ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    )
from .serializers import UserCreateSerializer, WishListSerializer, WishDetailSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsStaff
from rest_framework.filters import SearchFilter, OrderingFilter

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class WishListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [OrderingFilter, SearchFilter,]
    search_fields = ['name', 'description']

class WishDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = WishDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsAuthenticated,IsStaff]

# Create your views here.
