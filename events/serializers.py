from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "date",
            "start_time",
            "end_time",
            "created_at",
            "updated_at"
        ]

    def validate(self, attrs):
        """
        Validate time logic and prevent overlapping events
        """

        request = self.context.get("request")
        user = request.user if request else None

        start_time = attrs["start_time"]
        end_time = attrs["end_time"]
        date = attrs["date"]
        
        # Time validation
        if end_time <= start_time:
            raise serializers.ValidationError(
                "End time must be after start time."
            )

        # Conflict detection
        conflicts = Event.objects.filter(
            user=user,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        if conflicts.exists():
            raise serializers.ValidationError(
                "This event overlaps with an existing event."
            )

        return attrs
