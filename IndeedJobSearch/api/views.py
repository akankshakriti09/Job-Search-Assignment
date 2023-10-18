from django.shortcuts import render

# Create your views here.









































# from django.http.response import JsonResponse
# import json
# from rest_framework.parsers import JSONParser
# from bson import json_util
# from bson.objectid import ObjectId
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework import status

# from api.models import Job
# from api.serializers import JobSerializer



# @csrf_exempt
# @api_view(["POST"])
# def JobList(request):
#     response = {}
#     if request.method == "POST":
#         try:
#             userdata = JSONParser().parse(request)
#             serialize = JobSerializer(data=userdata)
#             if serialize.is_valid():
#                 serialize.save()
#                 response["status"] = "Success"
#                 response["data"] = serialize.data
#                 return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
#             response["status"] = "Failed"
#             response["data"] = serialize.errors
#             return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)

#         except:
#             response["status"] = "Failed"
#             response["data"] = "Data Not Saved"
#             return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
