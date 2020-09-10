from django.contrib import admin
from website.models import Image, Rat, Prefix, Person, Location, Litter, Entry, Questionnaire
from website.services.photo import get_image_to_admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

admin.site.site_title = 'Панель администратора'
admin.site.site_header = 'Панель администратора'


class ImageInline(admin.TabularInline):
    model = Image.Image
    extra = 0
    fields = ('name', 'picture', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return get_image_to_admin(obj)

    get_image.short_description = 'изображение'


@admin.register(Rat.Rat)
class RatAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'gender', 'variety', 'date_of_birth', 'owner')
    list_display_links = ('full_name',)
    list_filter = ('alive', 'gender', 'in_rattery', 'status', 'title', 'castrate')
    search_fields = ('name', 'variety', 'owner__last_name')
    readonly_fields = ('date_of_add',)
    inlines = [ImageInline]
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


class EntryAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Entry.Entry
        fields = '__all__'


@admin.register(Entry.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'topic', 'date', 'public')
    list_display_links = ('title',)
    search_fields = ('title',)
    form = EntryAdminForm
    save_on_top = True
    save_as = True
    list_editable = ('public',)


@admin.register(Image.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rat', 'date', 'picture')
    list_display_links = ('name',)
    search_fields = ('name', 'rat__name',)
    save_on_top = True
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return get_image_to_admin(obj)

    get_image.short_description = 'изображение'


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


@admin.register(Questionnaire.Questionnaire)
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






