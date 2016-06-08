from django.http import HttpResponseForbidden
from funcy import decorator

from .conf import MINIREST

APPS = MINIREST.keys()


def model_perms(app, model_name):
    for guess in ('%s.%s' % (app, model_name), '%s.*' % app, '*.*'):
        if guess in APPS:
            return True
    else:
        return False


def edit_perms(request, app, model_name):
    for guess in ('%s.%s' % (app, model_name), '%s.*' % app, '*.*'):
        if guess in APPS:
            return True
    else:
        return False


@decorator
def check_model_perms(call):
    perms = model_perms(call.app_label, call.model_name)
    if not perms:
        return HttpResponseForbidden()
    return call()
