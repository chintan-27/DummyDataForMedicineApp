from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Medicine
from .serializers import MedicineSerializer

class MedicineList(APIView):
    def get(self,request):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer(medicine,many=True)
        return Response(serializer.data)

class MedicineListByManufacturer(APIView):
    def get(self,request,**kwargs):
        medicine = Medicine.objects.filter(manufacturer=self.kwargs['manufacturer'])
        serializer = MedicineSerializer(medicine,many=True)
        return Response(serializer.data)

class MedicineListByType(APIView):
    def get(self,request,**kwargs):
        medicine = Medicine.objects.filter(type=self.kwargs['type'])
        serializer = MedicineSerializer(medicine,many=True)
        return Response(serializer.data)
