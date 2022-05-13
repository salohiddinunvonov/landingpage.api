from rest_framework import serializers
from .models import *

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class PracticesAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticesAreas
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class OthersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Others
        fields = "__all__"


class ContactUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUS
        fields = "__all__"


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"


class OurExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurExpertise
        fields = "__all__"


class FlaticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flatication
        fields = "__all__"
