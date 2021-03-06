# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from app import views

urlpatterns = [
    # path('', admin.site.urls),          # Django admin route
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files
    # path('artikel',include('artikel.urls')), 
    path("layanan/kuesioner/pertanyaan/", include("pertanyaan.urls")), 
    path("layanan/kuesioner/jawaban/", include("jawaban.urls")), 


]
