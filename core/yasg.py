from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema


class CustomSwaggerViewSetTag(SwaggerAutoSchema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args[-1][2] in ['read', 'update', 'partial_update', 'delete', 'list', 'create', ]:
            self.tag_name = args[-1][1].title()
        else:
            self.tag_name = args[-1][2].title()

    def get_tags(self, operation_keys=None):
        tags = super().get_tags()
        tags[0] = self.tag_name
        return tags


schema_view = get_schema_view(
    openapi.Info(
        title="Title API",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
