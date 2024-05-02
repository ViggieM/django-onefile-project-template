import sys

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.urls import path
from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, "index.html")


settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="don't look me",
    ALLOWED_HOSTS=["*"],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["."],
        },
    ],
)

urlpatterns = [
    path("", index),
]

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
