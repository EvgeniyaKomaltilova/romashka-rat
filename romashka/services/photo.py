from django.utils.safestring import mark_safe


def get_main_photo(obj):
    """Возвращает последнее добавленное фото в качестве 'главного'"""
    try:
        return obj.photos.all().last().picture.url
    except AttributeError:
        return None


def get_image_to_admin(obj):
    return mark_safe(f'<img src="/static/{obj.picture.url}" width="200">')
