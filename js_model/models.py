from __future__ import unicode_literals
from django.core.serializers.json import DjangoJSONEncoder
from collections import OrderedDict
from django.db import models

def _camelize(str):
    splitted = str.split('_')
    result = [splitted[0]]
    for i in splitted[1:]:
        result.append(i.capitalize())
    return ''.join(result)

class JsModel(models.Model):
    class Meta:
        abstract = True

    methods = []
    json_properties = []
    camelize = True
    encoder = DjangoJSONEncoder

    def json_dict(self):
        if self.camelize:
            ret = OrderedDict([(_camelize(p), self.__dict__[p]) for p in self.json_properties])
            ret.update(OrderedDict([(_camelize(p),type(self).__dict__[p](self)) for p in self.methods]))
        else:
            ret = OrderedDict([(p, self.__dict__[p]) for p in self.json_properties])
            ret.update(OrderedDict([(p,type(self).__dict__[p](self)) for p in self.methods]))
        return ret

    def json(self, Encoder=None):
        if Encoder is None:
            Encoder = self.encoder
        return Encoder().encode(self.json_dict())