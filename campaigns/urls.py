from django.urls import include, path
from rest_framework import routers

from campaigns import views

router = routers.DefaultRouter()
router.register(r'', views.CampaignView, 'campaigns')

urlpatterns = [
    path('', include(router.urls)),
]
