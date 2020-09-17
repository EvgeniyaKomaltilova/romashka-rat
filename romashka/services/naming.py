def get_full_rat_name(obj):
    """Возвращает имя крысы с приставкой питомника"""
    result = obj.name

    if obj.prefix:
        if obj.gender == 'male':
            result = f'{obj.name} {obj.prefix.male_name}'
            if not obj.prefix.suffix:
                result = f'{obj.prefix.male_name} {obj.name}'

        else:
            result = f'{obj.name} {obj.prefix.female_name}'
            if not obj.prefix.suffix:
                result = f'{obj.prefix.female_name} {obj.name}'

    return result


def get_full_litter_name(obj):
    """Возвращает название литеры с приставкой питомника"""
    result = obj.name

    if obj.prefix:
        result = f'{obj.name} {obj.prefix.male_name}'
        if not obj.prefix.suffix:
            result = f'{obj.prefix.male_name} {obj.name}'

    return result


def get_litter_name_for_admin(obj):
    """Возвращает название литеры с указанием отца и матери"""
    if obj.father:
        father_name = obj.father.name
    else:
        father_name = 'мать неизвестна'

    if obj.mother:
        mother_name = obj.mother.name
    else:
        mother_name = 'отец неизвестен'

    return f'{obj.name} ({father_name} x {mother_name})'


def get_person_full_name(self):
    """Возвращает фамилию, имя и отчество (если есть)"""
    if self.second_name:
        result = f'{self.last_name} {self.first_name} {self.second_name}'
    else:
        result = f'{self.last_name} {self.first_name}'

    return result


def get_person_short_name(self):
    """Возвращает фамилию и инициалы"""
    if self.second_name:
        result = f'{self.last_name} {self.first_name[0]}. {self.second_name[0]}.'
    else:
        result = f'{self.last_name} {self.first_name[0]}.'

    return result


def get_prefix_name(obj):
    """Возвращает название префикса для отображение в админке"""
    if obj.male_name == obj.female_name:
        return obj.male_name
    else:
        return f'{obj.male_name}/{obj.female_name}'


def get_entry_name(obj):
    """Возвращает название записи для отображения в админке"""
    if obj.topic == 'news':
        return f'Новости: {obj.title}'
    elif obj.topic == 'about':
        return f'О питомнике: {obj.title}'
    elif obj.topic == 'contract':
        return f'Договор: {obj.title}'
    elif obj.topic == 'varieties':
        return f'Разновидности: {obj.title}'
    elif obj.topic == 'colors':
        return f'Окрасы: {obj.title}'
    elif obj.topic == 'markings':
        return f'Маркировки: {obj.title}'
