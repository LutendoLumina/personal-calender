from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDeleteView

urlpatterns = [
    path("events/", EventListCreateView.as_view(), name="event-list-create"),
    path("events/<int:pk>/", EventRetrieveUpdateDeleteView.as_view(), name="event-detail"),
]

