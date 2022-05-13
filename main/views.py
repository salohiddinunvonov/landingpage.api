from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.http import Http404
from rest_framework import status
from main.models import *
from main.serializer import *



class SliderView(APIView):

    def get(self, request):
        slider = Slider.objects.last()
        slidr = SliderSerializer(slider)
        return Response(slidr.data)

class InfoView(RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    def retrieve(self, request, pk):
        info = Info.objects.get(id=pk)
        ser = InfoSerializer(info)
        return Response(ser.data)

class PracticesAreasView(APIView):

    def get(self, request):
        slider = PracticesAreas.objects.all().order_by("-id")[0:6]
        slid = PracticesAreasSerializer(slider, many=True)
        return Response(slid.data)

class OurExpertiseView(APIView):

    def get(self, request, pk):
        slider = OurExpertise.objects.get(id=pk)
        slid = OurExpertiseSerializer(slider)
        return Response(slid.data)


@api_view(['GET'])
def FlaticationGET(request):
    expertise = request.GET.get("expertise")
    flat = Flatication.objects.filter(expertise_id=expertise)
    ser = FlaticationSerializer(flat, many=True)
    return Response(ser.data)
    

class BlogView(APIView):

    def get(self, request):
        slider = Blog.objects.all().order_by("-id")[0:3]
        slid = BlogSerializer(slider, many=True)
        return Response(slid.data)



class OthersView(APIView):

    def get(self, request):
        slider = Others.objects.last()
        slid = OthersSerializer(slider)
        return Response(slid.data)

class ContactUSView(CreateAPIView):
    queryset = ContactUS.objects.all()
    serializer_class = ContactUSSerializer

class NewsletterView(CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer