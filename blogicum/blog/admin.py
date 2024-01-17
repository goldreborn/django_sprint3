from django.contrib import admin

from .models import Location
from .models import Post
from .models import Category


admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Category)
