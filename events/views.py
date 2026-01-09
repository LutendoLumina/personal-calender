from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer

# Create your views here.


class EventListCreateView(generics.ListCreateAPIView):
    """
    GET: List all events for the authenticated user
    POST: Create a new event for the authenticated user
    """

    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EventRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single event
    PUT: Update an event
    DELETE: Delete an event
    """

    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)
