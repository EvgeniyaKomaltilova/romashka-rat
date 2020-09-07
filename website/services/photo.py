def get_main_photo(obj):
    """Возвращает последнее добавленное фото в качестве 'главного'"""
    try:
        return obj.photos.all().last().picture.url
    except AttributeError:
        return None
