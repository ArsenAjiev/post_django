from rest_framework import viewsets
from post.serializers import PostSerializer
from post.models import Post
from django.http import HttpResponseRedirect


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


# redirect to https://postdjangobackend.herokuapp.com/swagger/
def index(request):
    return HttpResponseRedirect('https://postdjangobackend.herokuapp.com/swagger/')