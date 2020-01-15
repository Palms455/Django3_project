from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actors)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)

# Register your models here.
