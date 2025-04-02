from django.contrib import admin
from django.urls import path, include
from core.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    # iki farklı şekilde de tanımlanabilir
    ##path("", include("core.urls"), name="index" ),  # 'core' uygulamanızın adını kullanın(
    path("", index, name="index"),
]

# def index(request):
#     return HttpResponse("Hoş Geldiniz!") 