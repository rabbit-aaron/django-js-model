from __future__ import unicode_literals
from django.apps import AppConfig
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import QuerySet

def _to_dict(qs):
    for i in qs:
        if hasattr(i, 'json_dict') and callable(i.json_dict):
            yield i.json_dict()

def _json(self, Encoder=None):
    if Encoder is None:
        Encoder = self.model.encoder if hasattr(self.model,'encoder') else DjangoJSONEncoder
    return Encoder().encode(list(_to_dict(self)))

QuerySet.json = _json

class JsModelConfig(AppConfig):
    name = 'js_model'
