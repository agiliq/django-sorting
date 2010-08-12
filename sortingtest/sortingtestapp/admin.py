from django.contrib import admin

from sortingtestapp.models import SortableThingy, SortableThingy2
admin.site.register(SortableThingy)
admin.site.register(SortableThingy2)

