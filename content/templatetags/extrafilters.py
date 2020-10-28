from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def showimg(context, imgTitle):
    images = context['images']
    for i in images:
        if i.title == imgTitle:
            image = i
            break
    return '<img src="' + image.photo.name + '" alt="' + imgTitle + '">'