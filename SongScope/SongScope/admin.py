from django.contrib import admin

from .models import User
from .models import Song
from .models import Composer
from .models import Artist
from .models import Album


admin.site.register(User)
admin.site.register(Song)
admin.site.register(Composer)
admin.site.register(Artist)
admin.site.register(Album)
# Register your models here.
