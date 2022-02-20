from django.urls import (
    include,
    path,
)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

app_name = 'api'

urlpatterns = router.urls


urlpatterns += [
    path('web/', include('web.urls')),
]
