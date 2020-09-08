from django.contrib import admin
from website.models import Image, Rat, Prefix, Person, Location, Litter, Entry


@admin.register(Rat.Rat)
class RatAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'gender', 'variety', 'date_of_birth', 'owner')
    list_display_links = ('full_name',)
    list_filter = ('alive', 'gender', 'in_rattery', 'status', 'title', 'castrate')
    search_fields = ('name', 'variety', 'owner__last_name')
    readonly_fields = ('date_of_add',)
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': (
                ('alive', 'castrate', 'in_rattery', 'public',),
                ('status',),
                ('title',),
                ('name',),
                ('litter',),
                ('prefix',),
                ('variety',),
                ('date_of_birth',),
                ('date_of_death',),
                ('father', 'breeder',),
                ('mother', 'owner',),
                ('information',),

            )
        }

        ),
    )


class RatInline(admin.TabularInline):
    model = Rat.Rat
    extra = 0
    fields = ('status', 'name', 'variety', 'owner')


@admin.register(Litter.Litter)
class LitterAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'number', 'date_of_birth', 'father', 'mother')
    list_display_links = ('full_name',)
    list_filter = ('year', 'breeder')
    search_fields = ('name', 'number', 'father__name', 'mother__name')
    inlines = [RatInline]
    save_on_top = True


@admin.register(Person.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'location')
    list_display_links = ('full_name',)
    search_fields = ('first_name', 'second_name', 'last_name')
    save_on_top = True


@admin.register(Entry.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'topic', 'date', 'public')
    list_display_links = ('title',)
    search_fields = ('title',)
    save_on_top = True
    save_as = True
    list_editable = ('public',)


@admin.register(Image.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rat', 'date', 'picture')
    list_display_links = ('name',)
    search_fields = ('name', 'rat__name',)
    save_on_top = True


@admin.register(Location.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'region', 'country')
    list_display_links = ('city',)
    save_on_top = True


@admin.register(Prefix.Prefix)
class PrefixAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    save_on_top = True



