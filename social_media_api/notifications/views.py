from django.shortcuts import render

# Create your views here.
class LikeCreateView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            return Response({"detail": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)

        # create notification for post author (don't notify self)
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_ct=ContentType.objects.get_for_model(post),
                target_id=post.id
            )

        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LikeRemoveView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(post=post, user=request.user)
            like.delete()
            return Response({"detail": "Unliked"}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "Like not found"}, status=status.HTTP_404_NOT_FOUND)