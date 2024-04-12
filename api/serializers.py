from rest_framework import serializers
from .models import Post,Tag

# Serialiser Class-------------------------


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class PostSerializer(serializers.ModelSerializer):
    post_tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'post_title', 'post_sub_title', 'post_description', 'live_url', 'code_url', 'date_created', 'image', 'post_tags']



    def get_post_tags(self, obj):
            return [tag.name for tag in obj.post_tags.all()]