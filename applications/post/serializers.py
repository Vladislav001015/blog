from rest_framework import serializers
from applications.post.models import Post, Category, Comment, Like, Rating, Image
from django.db.models import Avg


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__' 
    
    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        print(images_data)
        post = Post.objects.create(**validated_data)

        for image in images_data.getlist('images'):
            pass
        # TODO: сохранять картинки и в админке выводить количество лайков в каждому посту

        return post

    
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['likes'] = instance.likes.filter(like=True).count()
        rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
        return rep


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        if not instance.parent:
            rep.pop('parent')
        
        return rep


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField()
    rating = serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Rating
        fields = ['rating']