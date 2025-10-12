from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import SimpleUserSerializer
from posts.models import Post


User = get_user_model()

class FollowToggleAPIView(APIView):
    """
    POST to follow, DELETE to unfollow. URL: /api/accounts/follow/{user_id}/
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, pk=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({"detail": f"You are now following {target.username}."}, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        target = get_object_or_404(User, pk=user_id)
        request.user.following.remove(target)
        return Response({"detail": f"You have unfollowed {target.username}."}, status=status.HTTP_200_OK)


class FollowingListView(generics.ListAPIView):
    """List users the current user is following"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SimpleUserSerializer

    def get_queryset(self):
        return self.request.user.following.all()


class FollowersListView(generics.ListAPIView):
    """List users who follow the current user"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SimpleUserSerializer

    def get_queryset(self):
        return self.request.user.followers.all()


class FeedView(generics.ListAPIView):
    """
    Return posts from users the current user follows, ordered newest first.
    Endpoint: /api/posts/feed/
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = None  # set dynamically
    pagination_class = None  # can use default DRF pagination

    def get_serializer_class(self):
        # import here to avoid circular imports issues
        from posts.serializers import PostSerializer
        return PostSerializer

    def get_queryset(self):
        # Get posts authored by users the current user follows, include own posts optionally
        following_qs = self.request.user.following.all()
        # Optionally include own posts:
        # following_qs = list(following_qs) + [self.request.user]
        return Post.objects.filter(author__in=following_qs).order_by('-created_at')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")
