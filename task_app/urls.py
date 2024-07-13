from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="The Task Manager is a web application designed to help users \
        efficiently manage their tasks and to-dos. It provides a user-friendly interface \
        for creating, viewing, updating, and deleting tasks, ensuring that users can keep track\
        of their responsibilities with ease. The application leverages modern web technologies and \
        follows RESTful principles to offer a seamless and interactive experience.",
        terms_of_service="https://www.example.com/terms/",
        # contact=openapi.Contact(email="contact@example.com"),
        # license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
