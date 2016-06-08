from rest_framework import serializers


def dynamic_serializer(model):
    """
    :param model:
    :return serializer object:
    """
    name = "{0}Serializer".format(model.__name__)

    class Meta:
        pass

    setattr(Meta, 'model', model)
    attrs = {'Meta': Meta}

    return type(name, (serializers.ModelSerializer,), attrs)


def parse_qs(qstring, model):
    """
    :param qstring:
    :return dict:
    """
    fl = {}
    for f in qstring.split('|'):
        key, val = f.split(':')
        fl[key] = model._meta.get_field(key).to_python(val)
    return fl
