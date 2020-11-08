from django import template
from django.conf import settings
import os

register = template.Library()

@register.simple_tag(takes_context=True)
def showimg(context, imgTitle):
    images = context['images']
    for i in images:
        if i.title == imgTitle:
            image = i
            break
    return '<img src="' + os.path.join(settings.MEDIA_ROOT, image.content.name) + '" alt="' + imgTitle + '">'
