from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.category.views import CategoryViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="SHOP API",
      default_version='v1',
   ),
   public=True,
)

router = SimpleRouter()
router.register('category', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('api/account/', include('apps.account.urls')),
    path('api/', include(router.urls)),
    path('api/cars/', include('apps.car.urls'))
]
