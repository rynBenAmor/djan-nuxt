from rest_framework import serializers


from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'




from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # Includes "text" and "sentiment"




from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    CITY_CHOICES = [(city[0], city[1]) for city in Profile.CITY_CHOICES]  # Extracting choices
    print(CITY_CHOICES)

    city_choices = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'name', 'city', 'city_choices']

    def get_city_choices(self, obj):
        return self.CITY_CHOICES




from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'