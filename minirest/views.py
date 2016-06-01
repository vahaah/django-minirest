from django.apps import apps
from .utils import dynamic_serializer


def model_view(request, app, model):
    model = apps.get_model(app, model)
    serializer = dynamic_serializer(model)
