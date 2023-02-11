from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    CurrentUserDefault,
    ValidationError
)

from posts.models import Comment, Post, Follow, Group, User


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', )


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', read_only=True, default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise ValidationError(
                'You cannot to follow yourself')
        return value
