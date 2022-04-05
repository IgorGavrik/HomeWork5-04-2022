from rest_framework.views import APIView
from django.shortcuts import HttpResponse


def post(request):
    print(request.body)
    print("Query", request.GET)
    print("Body", request.POST)
    return  HttpResponse()


class TestView(APIView):
    def post(self, request):
        return HttpResponse()