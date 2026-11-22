from rest_framework.routers import DefaultRouter
from .api_views import PostViewSet

router = DefaultRouter()

router.register(
    r'posts',
    PostViewSet,
    basename='post'
)

urlpatterns = router.urls
'''
What is DefaultRouter?

Normally, you would have to manually define URLs for every CRUD operation.

But DRF's router automatically generates URLs for your ViewSet.

For example:
HTTP method	URL	Action
GET	/api/posts/	-> List all posts
POST	/api/posts/	-> Create a post

router.register does the following:
r'posts': URL prefix.
PostViewSet: ViewSet handling the requests.
basename='post': Base name for automatically generated URL names.

'''