import six
from django.http import HttpResponseForbidden
from django.utils.module_loading import import_string
from funcy import decorator, merge

from .conf import MINIREST, MINIREST_DEFAULT_PERMS

APPS = MINIREST.keys()


def model_perms(app, model_name):
    for guess in ('%s.%s' % (app, model_name), '%s.*' % app, '*.*'):
        if guess in APPS:
            return True
    else:
        return False


def check_perms(view, request, app, model_name):
    for guess in ('%s.%s' % (app, model_name), '%s.*' % app, '*.*'):
        if guess in APPS:
            perms = merge(MINIREST_DEFAULT_PERMS, MINIREST[guess]['perms'])
            if isinstance(perms[view], six.types.FunctionType):
                return perms[view](request)
            elif isinstance(perms[view], six.string_types):
                return import_string(perms[view])(request)
            return False
    else:
        return False


@decorator
def check_model_perms(call):
    perms = model_perms(call.app_label, call.model_name)
    if not perms:
        return HttpResponseForbidden()
    return call()


@decorator
def check_view_perms(call, view='list'):
    perms = check_perms(view, call.request, call.app_label, call.model_name)
    if not perms:
        return HttpResponseForbidden()
    return call()
