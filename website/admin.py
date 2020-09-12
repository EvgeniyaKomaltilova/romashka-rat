from django.contrib import admin
from romashka.services.photo import get_image_to_admin
from ckeditor.widgets import CKEditorWidget
from django import forms

from website.models.Entry import Entry
from website.models.Image import Image

admin.site.site_title = 'Панель администратора'
admin.site.site_header = 'Панель администратора'


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    fields = ('name', 'picture', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return get_image_to_admin(obj)

    get_image.short_description = 'изображение'


class EntryAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Entry
        fields = '__all__'


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'topic', 'date', 'public')
    list_display_links = ('title',)
    inlines = [ImageInline]
    search_fields = ('title',)
    form = EntryAdminForm
    save_on_top = True
    save_as = True
    list_editable = ('public',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'entry', 'picture', 'main_page')
    list_display_links = ('name',)
    search_fields = ('name',)
    save_on_top = True
    readonly_fields = ('get_image',)
    list_editable = ('main_page',)


    def get_image(self, obj):
        return get_image_to_admin(obj)

    get_image.short_description = 'изображение'
