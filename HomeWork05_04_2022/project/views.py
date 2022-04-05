from rest_framework.views import APIView
from django.shortcuts import HttpResponse


class TestView(APIView):
    def project(self, request):
        return HttpResponse()
    