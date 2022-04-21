from rest_framework_swagger.views import get_swagger_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin

API_TITLE = "Blog API Project docs"
API_DESCRIPTION = "Blog API Project docs"
yasg_schema_view = get_schema_view(
    openapi.Info(
        title='Blog API',
        description="Oddiy blog project API",
        default_version="v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shahzodikromovich7680@gmail.com"),
        license=openapi.License(name="Blog Project licence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

schema_view = get_swagger_view(title=API_TITLE)

admin.site.site_header = "Blog Api adminstration"
admin.site.site_title = "Blog Api adminstration"
admin.site.index_title = "Blog Api adminstration"
