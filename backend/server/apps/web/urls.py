from rest_framework.routers import SimpleRouter

from .views import WebBookmarkViewSet

app_name = 'web'

router = SimpleRouter()
router.register('web-bookmarks', WebBookmarkViewSet)

urlpatterns = router.urls
