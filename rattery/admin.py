from django.contrib import admin
from rattery.models.Litter import Litter
from rattery.models.Location import Location
from rattery.models.Person import Person
from rattery.models.Photo import Photo
from rattery.models.Prefix import Prefix
from rattery.models.Questionnaire import Questionnaire
from rattery.models.Rat import Rat
from romashka.services.count import get_owned_rat_count
from romashka.services.naming import get_person_short_name
from romashka.services.photo import get_image_to_admin


class PhotoInline(admin.TabularInline):
    """Встроенная панель фотографий для отображения на странице крысы"""
    model = Photo
    extra = 0
    fields = ('name', 'picture', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        """Получение изображения для админки"""
        return get_image_to_admin(obj)

    get_image.short_description = 'изображение'


class RatToPersonInline(admin.TabularInline):
    """Встроенная панель крыс во владении для отображения на странице персоны"""
    model = Rat
    fk_name = 'owner'
    extra = 0
    fields = ('name', 'gender', 'variety', 'date_of_birth')
    readonly_fields = ('name', 'gender', 'variety', 'date_of_birth')


class RatToLitterInline(admin.TabularInline):
    """Встроенная панель крыс для отображения на странице помета"""
    model = Rat
    extra = 0
    fields = ('status', 'name', 'gender', 'variety', 'owner')


@admin.register(Rat)
class RatAdmin(admin.ModelAdmin):
    """Отображение крыс а вдминке"""
    list_display = ('id', 'full_name', 'gender', 'variety', 'date_of_birth', 'owner')
    list_display_links = ('full_name',)
    list_filter = ('alive', 'gender', 'in_rattery', 'status', 'title', 'castrate')
    search_fields = ('name', 'variety', 'owner__last_name')
    readonly_fields = ('date_of_add',)
    autocomplete_fields = ['litter', 'father', 'mother', 'breeder', 'owner']
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
        """Фильтр по полу при выборе отца и матери"""
        if db_field.name == "mother":
            kwargs["queryset"] = Rat.objects.filter(gender='female')
        if db_field.name == "father":
            kwargs["queryset"] = Rat.objects.filter(gender='male')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Litter)
class LitterAdmin(admin.ModelAdmin):
    """Отображение пометов в админке"""
    list_display = ('id', 'full_name', 'number', 'date_of_birth', 'mother', 'father')
    list_display_links = ('full_name',)
    list_filter = ('year',)
    search_fields = ('name', 'number', 'mother__name', 'father__name')
    autocomplete_fields = ['father', 'mother', 'breeder']
    inlines = [RatToLitterInline]
    save_on_top = True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Фильтр по полу при выборе отца и матери"""
        if db_field.name == "mother":
            kwargs["queryset"] = Rat.objects.filter(gender='female')
        if db_field.name == "father":
            kwargs["queryset"] = Rat.objects.filter(gender='male')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Отображение персон в админке"""
    list_display = ('id', 'short_name', 'location', 'owned_rats')
    list_display_links = ('short_name',)
    search_fields = ('first_name', 'second_name', 'last_name')
    autocomplete_fields = ['location']
    save_on_top = True
    inlines = [RatToPersonInline]

    def short_name(self, obj):
        """Фамилия и инициалы"""
        return get_person_short_name(obj)

    def owned_rats(self, obj):
        """Количество крыс во владении"""
        return get_owned_rat_count(obj)

    short_name.short_description = 'Имя'
    owned_rats.short_description = 'Крысы'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Отображение фотографий крыс в админке"""
    list_display = ('id', 'name', 'rat', 'date', 'picture')
    list_display_links = ('name',)
    search_fields = ('name', 'rat__name',)
    autocomplete_fields = ['rat']
    save_on_top = True
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        """Получение изображения"""
        return get_image_to_admin(obj)

    get_image.short_description = 'изображение'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Отображение локаций в админке"""
    list_display = ('id', 'city', 'region', 'country')
    list_display_links = ('city',)
    search_fields = ('city', 'country')
    save_on_top = True


@admin.register(Prefix)
class PrefixAdmin(admin.ModelAdmin):
    """Отображение приставок питомников в админке"""
    list_display = ('id', 'name')
    list_display_links = ('name',)
    save_on_top = True


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    """Отображение анкет в админке"""
    list_display = ('id', 'name', 'age', 'location', 'contact', 'date', 'read', 'approved',)
    list_display_links = ('name',)
    list_filter = ('read', 'approved')
    search_fields = ('name',)
    save_on_top = True
    list_editable = ('read', 'approved',)
    readonly_fields = ('date', 'name', 'contact', 'age', 'location', 'which_baby_rat', 'allergy', 'know_how',
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
