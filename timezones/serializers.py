from rest_framework import serializers

from .models import Timezone


class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = "__all__"
