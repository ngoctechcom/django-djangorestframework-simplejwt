from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import GetToken, Test
from .serializers import ProjectViewSet

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/custom', GetToken.as_view(), name="token_custom"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', Test.as_view(), name='hello'),
    path('project/', ProjectViewSet.as_view(), name='project')
]
