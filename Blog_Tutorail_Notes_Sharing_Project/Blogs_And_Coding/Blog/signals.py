from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from Blog.models import BlogPost
from django.conf import settings

@receiver(pre_save,sender=BlogPost)
def at_beg_save(sender,instance,**kwargs):
    old = BlogPost.objects.get(pk=instance.pk)
    return old
