from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import *

admin.site.register(Blogs)
admin.site.register(Reply)
