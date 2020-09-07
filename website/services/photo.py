def get_main_photo(self):
    try:
        return self.photos.all().last().picture.url
    except AttributeError:
        return None
