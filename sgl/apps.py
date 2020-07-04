from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class SglConfig(AppConfig):
    name = 'sgl'


    def ready(self):
        import sgl.signals
