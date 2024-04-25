from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post,Tag
from .serializers import PostSerializer,TagSerializer
from utils.helper import response_data
import cloudinary.uploader




@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'URLS': 'List of all urls',
        
        'post-list' : 'To List all posts....',
        
        'post-detail' : 'To view post detail by ID',
        
        'post-create' : 'To create a post',
        
        'post-update' : 'To update post by ID',
        
        'post-delete' : 'To delete post by ID '
    }
    
    return Response(api_urls)


@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        post_data = request.data
        post_tags_data = post_data.pop('post_tags', [])  # Remove post_tags from data and set to empty list if not provided
        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            # Upload image to Cloudinary
            image = request.data.get('image')
            if image:
                result = cloudinary.uploader.upload(image)
                serializer.validated_data['image'] = result['secure_url']
            post = serializer.save()
             # Create or get tags and associate them with the post
            for tag_data in post_tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data)
                post.post_tags.add(tag) 

            return Response(response_data(status_code=status.HTTP_201_CREATED, message="Post created successfully", data=serializer.data))
        return Response(response_data(status_code=status.HTTP_400_BAD_REQUEST, message=serializer.errors, success=False), status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(response_data(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, message="Method not allowed", success=False), status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serialized_data = []
        for post in posts:
            post_data = PostSerializer(post).data
            # tags_data = [{'name': tag.name} for tag in post.post_tags.all()]  # get it as array of object
            tags_data = [tag.name for tag in post.post_tags.all()]  # As Array of String
            post_data['post_tags'] = tags_data
            serialized_data.append(post_data)
        return Response(response_data(status_code=status.HTTP_200_OK, message="Posts retrieved successfully", data=serialized_data))
    else:
        return Response(response_data(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, message="Method not allowed", success=False), status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def post_detail(request, pk):
    if request.method == 'GET':
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(response_data(status_code=status.HTTP_404_NOT_FOUND, message="Post not found", success=False), status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post)
        return Response(response_data(status_code=status.HTTP_200_OK, message="Post retrieved successfully", data=serializer.data))
    else:
        return Response(response_data(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, message="Method not allowed", success=False), status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def update_post(request, pk):
    if request.method == 'PUT':
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(response_data(status_code=status.HTTP_404_NOT_FOUND, message="Post not found", success=False), status=status.HTTP_404_NOT_FOUND)
        post_data = request.data
        post_tags_data = post_data.pop('post_tags', [])  # Remove post_tags from data and set to empty list if not provided
        serializer = PostSerializer(post, data=post_data)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            # Upload image to Cloudinary if new image is provided
            new_image = request.data.get('image')
            if new_image:
                result = cloudinary.uploader.upload(new_image)
                serializer.validated_data['image'] = result['secure_url']
            post =  serializer.save()

              # Clear existing tags and associate new ones with the post
            post.post_tags.clear()
            for tag_data in post_tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data)
                post.post_tags.add(tag)
            return Response(response_data(status_code=status.HTTP_200_OK, message="Post updated successfully", data=serializer.data))
        return Response(response_data(status_code=status.HTTP_400_BAD_REQUEST, message=serializer.errors, success=False), status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(response_data(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, message="Method not allowed", success=False), status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_post(request, pk):
    if request.method == 'DELETE':
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(response_data(status_code=status.HTTP_404_NOT_FOUND, message="Post not found", success=False), status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(response_data(status_code=status.HTTP_204_NO_CONTENT, message="Post deleted successfully"))
    else:
        return Response(response_data(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, message="Method not allowed", success=False), status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET'])
def get_tags(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serialized_data = TagSerializer(tags, many=True)
        return Response(response_data(status_code=status.HTTP_200_OK, message="Tags retrieved successfully", data=serialized_data.data))
    else:
        return Response(response_data(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, message="Method not allowed", success=False), status=status.HTTP_405_METHOD_NOT_ALLOWED)

