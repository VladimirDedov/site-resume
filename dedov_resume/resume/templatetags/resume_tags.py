from django import template
from resume.models import Education, Experience

register=template.Library()

@register.simple_tag()
def get_education():
    """Возврат образования"""
    return Education.objects.all()

@register.simple_tag()
def get_experience():
    return Experience.objects.all().order_by('-id')