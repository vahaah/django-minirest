from importlib import import_module

from django.apps import apps
from django.apps.config import MODELS_MODULE_NAME
from django.core.exceptions import AppRegistryNotReady


def get_model(app_label, model_name):
    try:
        return apps.get_model(app_label, model_name)
    except AppRegistryNotReady:
        if apps.apps_ready and not apps.models_ready:
            app_config = apps.get_app_config(app_label)
            import_module('%s.%s' % (app_config.name, MODELS_MODULE_NAME))
            return apps.get_registered_model(app_label, model_name)
        else:
            raise
