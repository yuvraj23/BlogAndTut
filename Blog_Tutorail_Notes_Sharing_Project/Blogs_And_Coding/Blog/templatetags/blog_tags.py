from Blog.models import BlogPost
from django import template
from django.contrib.auth.models import User
register=template.Library()


@register.inclusion_tag('Blog/likes.html')
def Like_Post():
    pass
