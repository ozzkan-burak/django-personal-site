from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),  # 'core' uygulamanızın adını kullanın
]

# def index(request):
#     return HttpResponse("Hoş Geldiniz!") 