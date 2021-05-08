from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from .models import Pertanyaan
from rest_framework import compat
from django.views import View
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
from django.db.models import Q
import json
from django.contrib import messages
from .forms import PertanyaanModelForm

from .serializers import CreateSerializer
from django.http import *
from rest_framework.decorators import api_view

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls={
#         'List': 'pertanyaan-list',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def showAll(request):
#     query = Pertanyaan.objects.all()
#     serializer = CreateSerializer(query, many=True)
#     return Response(serializer.data)

class ApiView(APIView):
    def get(self, request):
        query = Pertanyaan.objects.all()
        serializer = CreateSerializer(query, many=True)
        return Response(serializer.data)


# @login_required(login_url="/login/")
# def delete_view(request , id_pertanyaan=None):
#     obj = get_object_or_404(Pertanyaan, id_pertanyaan=id_pertanyaan)
#     if request.method == 'POST':
#         obj.delete()
#         messages.success(request, "Data Deleted...!")
#         return HttpResponseRedirect("/list/")

#     context = {
#         "object": obj
#     }

#     template = "recipe/delete_view.html"
#     return render(request, template, context)



# # @login_required(login_url="/admin/")
# def update_view(request, id=None):
#     obj = get_object_or_404(Recipe, id=id)
#     form = RecipeModelForm(request.POST or None, instance=obj)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         obj = form.save(commit=False)
#         #print(obj.title)
#         obj.save()
#         messages.success(request, "Updated post!")
#         return HttpResponseRedirect("/recipe{num}".format(num=obj.id))
    
#     template = "recipe/update_view.html"
#     return render(request, template, context)

# # @login_required(login_url="/admin/")
# def create_view(request):
#     form = RecipeModelForm(request.POST or None)
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.save()
#         return HttpResponseRedirect("/list/")
#     context = {
#         "form": form
#     }

#     html_template = loader.get_template( 'index.html' )
#     return HttpResponse(html_template.render(context, request))

#     # template = "recipe/create_view.html"
#     # return render(request, template, context)

# # @login_required(login_url="/admin/")    
# def detail_view(request, id=None):
#     print(id)
#     qs = get_object_or_404(Recipe, id=id)
#     print(qs)
#     context = {
#         "object" : qs
#     }

#     template = "recipe\detail_view.html"
#     return render(request, template, context)

# # @login_required(login_url="/admin/")
# def list_view(request):
#     query = request.GET.get("qury", None)
#     obj = Recipe.objects.all()
#     if query is not None:
#         obj = obj.filter(title__icontains=query)
    
#     context = {
#         "object_list" : obj
#     }

#     template = "recipe\list_view.html"    
#     return render(request, template, context)


# # @login_required(login_url="/admin/")
# def login_required(request):
#     print(request.user)
#     qs = Recipe.objects.all()
#     template = "recipe\list_view.html"
#     # print(qs)
#     context = {
#         "object_list" : qs
#     }
#     if request.user.is_authenticated:
#        template = "recipe\list_view.html"
#     else:
#         template = "recipe\list_view_public.html"
#         return HttpResponseRedirect("/admin")
#     return render(request, template, context)