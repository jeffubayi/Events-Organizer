from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (confirmAttendanceAPIView,EventListCreateAPIView, ReviewserializerAPIView,ReviewserializerDetailView)

router = DefaultRouter()

router.register("all-events", EventListCreateAPIView,base_name ='all-events')
router.register("confirm_attendance",confirmAttendanceAPIView)

urlpatterns =[
    path("",include(router.urls)),
    path("event/<int:event_pk>/reviews/",ReviewserializerAPIView.as_view(),name="event_reviews"),
    path('event/<int:event_pk>/',ReviewserializerDetailView.as_view(),name='review-details')
]