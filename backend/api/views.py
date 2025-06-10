#api/views.py
from rest_framework import viewsets
from rest_framework.response import Response


from rest_framework.views import APIView


from .models import Message
from .serializers import MessageSerializer
from .models import Profile
from .serializers import ProfileSerializer
from .models import Profile
from .serializers import ProfileSerializer
from .models import Comment
from .serializers import CommentSerializer




class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer




class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-id')  # Show newest first
    serializer_class = CommentSerializer




class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if self.queryset.exists():
            response.data.append({"city_choices": Profile.CITY_CHOICES})
        return response






class ImageCaptionView(APIView):

    def post(self, request):
        return Response({"caption": "hello world"})





from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer