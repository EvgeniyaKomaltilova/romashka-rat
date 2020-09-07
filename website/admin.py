from django.contrib import admin
from website.models import Image, Rat, Prefix, Person, Location, Litter, Entry

admin.site.register(Image.Image)
admin.site.register(Rat.Rat)
admin.site.register(Prefix.Prefix)
admin.site.register(Person.Person)
admin.site.register(Location.Location)
admin.site.register(Litter.Litter)
admin.site.register(Entry.Entry)
