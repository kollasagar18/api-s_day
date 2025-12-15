from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
file_name="api/static/emps.json"

def read_data():
    with open(file_name,"r") as f:
        return json.load(f)
        
def write_data(data):
    with open(file_name,"w") as f:
        json.dump(data,f)
def home(request):
    return render(request, "home.html")

@api_view(["POST"])
def creating_emp(request):
    data = request.POST.dict()
    data_fram=read_data()
    data_fram["employess"].append(data)
    write_data(data_fram)
    # check data in terminal
    return HttpResponse("Form submitted successfully")
@api_view(["GET"])
def get_all(request):
    data_fram=read_data()
    return Response(data_fram)
@api_view(["GET"])
def get_alldata(request):
  if request.method == "GET":
      data_fram=read_data()
      #return (request,"data_all.html")
      return JsonResponse(data_fram)
    



    