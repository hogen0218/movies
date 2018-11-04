from django.contrib import admin
from .models import Movie, Kind, HotKind


# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    pass

class KindAdmin(admin.ModelAdmin):
    pass

class HotKindAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)

admin.site.register(Kind, KindAdmin)

admin.site.register(HotKind, HotKindAdmin)