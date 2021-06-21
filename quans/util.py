import string
import random
from django.utils.text import slugify

# Create your views here.
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=90) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image

def random_string_generator(size=10,chars = string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator_blog(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists :
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr=random_string_generator(size=4))
        return unique_slug_generator_blog(instance, new_slug=new_slug)
    return slug


def unique_slug_generator_Profile(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.user.username)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists :
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr=random_string_generator(size=4))
        return unique_slug_generator_Profile(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_accounts(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.user)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists :
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr=random_string_generator(size=4))
        return unique_slug_generator_accounts(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_question(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.question_heading)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists :
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr=random_string_generator(size=4))
        return unique_slug_generator_question(instance, new_slug=new_slug)
    return slug

def unique_slug_generator_college(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.college_name)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists :
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr=random_string_generator(size=4))
        return unique_slug_generator_college(instance, new_slug=new_slug)
    return slug

