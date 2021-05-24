from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TimezoneSerializer
from .models import Timezone
from .permissions import IsOwnerOrAdmin


class TimezoneViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)
    serializer_class = TimezoneSerializer

    def get_queryset(self):
        queryset = None
        if self.request.user.is_staff:
            queryset = Timezone.objects.all()
        else:
            queryset = Timezone.objects.filter(owner=self.request.user)

        return queryset.order_by("gmt_diff")

    def create(self, request):
        tz = request.data.get("timezone")
        if not tz:
            return Response({"response": "error", "message": "Timezone not found"})

        tz["owner"] = request.user.id

        serializer = TimezoneSerializer(data=tz)

        if serializer.is_valid():
            saved_tz = serializer.save()
        else:
            return Response({"response": "error", "message": serializer.errors})

        return Response(
            {
                "response": "success",
                "message": f"Timezone {saved_tz} created successfully",
            }
        )
