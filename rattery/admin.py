from django.contrib import admin
from rattery.models.Litter import Litter
from rattery.models.Location import Location
from rattery.models.Person import Person
from rattery.models.Photo import Photo
from rattery.models.Prefix import Prefix
from rattery.models.Questionnaire import Questionnaire
from rattery.models.Rat import Rat
from romashka.services.photo import get_image_to_admin


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0
    fields = ('name', 'picture', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return get_image_to_admin(obj)

    get_image.short_description = 'изображение'


@admin.register(Rat)
class RatAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'gender', 'variety', 'date_of_birth', 'owner')
    list_display_links = ('full_name',)
    list_filter = ('alive', 'gender', 'in_rattery', 'status', 'title', 'castrate')
    search_fields = ('name', 'variety', 'owner__last_name')
    readonly_fields = ('date_of_add',)
    inlines = [PhotoInline]
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
                ('gender',),
                ('date_of_birth',),
                ('date_of_death',),
                ('mother',),
                ('father',),
                ('owner',),
                ('breeder',),
                ('information',),
            )
        }
        ),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "mother":
            kwargs["queryset"] = Rat.objects.filter(gender='female')
        if db_field.name == "father":
            kwargs["queryset"] = Rat.objects.filter(gender='male')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class RatInline(admin.TabularInline):
    model = Rat
    extra = 0
    fields = ('status', 'name', 'gender', 'variety', 'owner')


@admin.register(Litter)
class LitterAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'number', 'date_of_birth', 'mother', 'father')
    list_display_links = ('full_name',)
    list_filter = ('year', 'breeder')
    search_fields = ('name', 'number', 'mother__name', 'father__name')
    inlines = [RatInline]
    save_on_top = True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "mother":
            kwargs["queryset"] = Rat.objects.filter(gender='female')
        if db_field.name == "father":
            kwargs["queryset"] = Rat.objects.filter(gender='male')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'location')
    list_display_links = ('full_name',)
    search_fields = ('first_name', 'second_name', 'last_name')
    save_on_top = True


@admin.register(Photo)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rat', 'date', 'picture')
    list_display_links = ('name',)
    search_fields = ('name', 'rat__name',)
    save_on_top = True
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return get_image_to_admin(obj)

    get_image.short_description = 'изображение'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'region', 'country')
    list_display_links = ('city',)
    save_on_top = True


@admin.register(Prefix)
class PrefixAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    save_on_top = True


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'location', 'email', 'date', 'read', 'approved',)
    list_display_links = ('name',)
    list_filter = ('read', 'approved')
    search_fields = ('name',)
    save_on_top = True
    list_editable = ('read', 'approved',)
    readonly_fields = ('date', 'name', 'email', 'age', 'location', 'which_baby_rat', 'allergy', 'know_how',
                       'pet_or_breed', 'friend', 'contract', 'recommendation', 'additionally')
    fieldsets = (
        (None, {
            'fields': (
                ('read', 'approved'),
                ('date',),
            )
        }
         ),
        ('личные данные', {
            'fields': (
                ('name',),
                ('age',),
                ('location',),
                ('email',),
            )
        }
         ),
        ('ответы', {
            'fields': (
                ('which_baby_rat',),
                ('allergy',),
                ('know_how',),
                ('pet_or_breed',),
                ('friend',),
                ('contract',),
                ('recommendation',),
                ('additionally',),
            )
        }
         ),
    )
