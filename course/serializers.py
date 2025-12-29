from rest_framework import serializers
from .models import Branch, Infaration, Burning


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

class BurningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burning
        fields = "__all__"

class InfarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infaration
        fields = "__all__"
