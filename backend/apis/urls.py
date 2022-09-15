from django.urls import include, re_path
from rest_framework import routers
from .views import GroupViewset

router = routers.DefaultRouter()
router.register(r"groups", GroupViewset)

urlpatterns = [
    re_path(r"^apis/", include(router.urls))
]