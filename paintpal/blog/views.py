from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import BlogPage
from .serializers import BlogPageSerializer
from wagtail.api.v2.views import PagesAPIViewSet

# class BlogPageAPIViewSet(viewsets.ModelViewSet):
class BlogPageAPIViewSet(PagesAPIViewSet):
    # queryset = BlogPage.objects.all()
    # serializer_class = BlogPageSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    model = BlogPage
