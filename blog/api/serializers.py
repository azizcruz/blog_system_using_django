from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from blog.models import Post

class PostAllSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='single_post')
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = "id", "user", "image", "title", "content", "publish_date", "url"

    def get_user(self, obj):
        return str(obj.user.username)


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "title", "content", "publish_date"

class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "title", "content", "publish_date", "update_date"
