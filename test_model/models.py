from __future__ import unicode_literals
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from js_model.models import JsModel

class MyEncoder(DjangoJSONEncoder):

    def encode(self, *args, **kwargs):
        return super(MyEncoder,self).encode(*args, **kwargs)

class TestModel(JsModel):

    methods = ['add_one','upper']
    json_properties = ['id','text','datetime','decimal','integer','charfield','filefield']
    #camelize = False
    #encoder = MyEncoder

    text = models.TextField(default="")
    datetime = models.DateTimeField(auto_now_add=True)
    boolean = models.BooleanField(default=True)
    decimal = models.DecimalField(default=0, max_digits=10, decimal_places=4)
    integer = models.IntegerField(default=0)
    charfield = models.CharField(default="", max_length=26)
    filefield = models.FileField(upload_to="uploads/")

    def add_one(self):
        return self.integer + 1

    def upper(self):
        return self.charfield.upper()
