from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username)
		new_user.set_password(password)
		new_user.save()
		return validated_data

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['item', 'user',]

class UserSerlializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']


class WishListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id"
		)

	Favourite_No = serializers.SerializerMethodField()

	def get_Favourite_No(self,obj):
		no_of_likes = FavoriteItem.objects.filter(item=obj)
		return no_of_likes.count()

	class Meta:
		model = Item
		fields = ['name', 'detail', 'added_by', 'Favourite_No']


class WishDetailSerializer(serializers.ModelSerializer):

	Fav_Users = serializers.SerializerMethodField()

	def get_Fav_Users(self,obj):
		no_of_favs = FavoriteItem.objects.filter(item=obj)
		no_of_favs_list = ItemSerializer(no_of_favs, many=True).data
		return no_of_favs_list

	class Meta:
		model = Item
		fields= ['name', 'description', 'added_by', 'Fav_Users'] 

