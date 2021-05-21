from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import *
from .api_views import *

urlpatterns = [
    path('api/branches', BankList.as_view()),
    path('api/branches/autocomplete', BankBranchList.as_view()),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)