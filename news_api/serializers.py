from rest_framework import serializers

from news_api.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
    upvotes_count = serializers.IntegerField(source="upvotes.count", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        exclude = ("post",)


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    upvotes_count = serializers.IntegerField(source="upvotes.count", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        depth = 1
