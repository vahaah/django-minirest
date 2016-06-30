from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from rest_framework.parsers import JSONParser

from .loading import get_model
from .perms import check_model_perms, check_view_perms
from .utils import dynamic_serializer, parse_qs


@csrf_protect
@require_http_methods(["GET"])
@check_model_perms
@check_view_perms('list')
def list_view(request, app_label, model_name):
    model = get_model(app_label, model_name)
    queryset = model.objects.all()
    qfilter = request.GET.get('filter', None)

    if qfilter:
        fl = parse_qs(qfilter, model)
        queryset = queryset.filter(**fl)

    limit = request.GET.get('limit', 100)
    page = request.GET.get('page', 1)

    count = queryset.count()
    p = Paginator(queryset, limit)
    queryset = p.page(page).object_list

    serializer = dynamic_serializer(model)(instance=queryset, many=True)
    resp = {
        'count': count,
        'num_pages': p.num_pages,
        'result': serializer.data
    }
    return JsonResponse(resp)


@csrf_protect
@require_http_methods(["GET", "POST", "PUT"])
@check_model_perms
def detail_view(request, app_label, model_name, pk):
    model = get_model(app_label, model_name)
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'GET':
        serializer = dynamic_serializer(model)(instance=obj)
        return JsonResponse(serializer.data)
    elif request.method in ['POST', 'PUT']:
        data = JSONParser().parse(request)
        serializer = dynamic_serializer(model)(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
