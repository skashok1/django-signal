from django.db.models.signals import post_save
from django.db.models import signals
from django.dispatch import receiver
from .models import Hero, Content


def create_hero(sender, **kwargs):
	if kwargs['created']:
		heroes =Content.objects.create(content =kwargs['instance'])

post_save.connect(create_hero, sender =Hero)
