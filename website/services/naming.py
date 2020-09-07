def get_full_rat_name(obj):
    result = obj.name

    if obj.prefix:
        if obj.gender == 'самец':
            result = f'{obj.name} {obj.prefix.male_name}'
            if not obj.prefix.suffix:
                result = f'{obj.prefix.male_name} {obj.name}'

        else:
            result = f'{obj.name} {obj.prefix.female_name}'
            if not obj.prefix.suffix:
                result = f'{obj.prefix.female_name} {obj.name}'

    return result


def get_full_litter_name(obj):
    result = obj.name

    if obj.prefix:
        result = f'{obj.name} {obj.prefix.male_name}'
        if not obj.prefix.suffix:
            result = f'{obj.prefix.male_name} {obj.name}'

    return result


def get_litter_name_for_admin(obj):

    if obj.father:
        father_name = obj.father.name
    else:
        father_name = 'мать неизвестна'

    if obj.mother:
        mother_name = obj.mother.name
    else:
        mother_name = 'отец неизвестен'

    return f'{obj.name} ({father_name} x {mother_name})'


def get_person_short_name(self):

    if self.second_name:
        result = f'{self.last_name} {self.first_name[0]}. {self.second_name[0]}.'
    else:
        result = f'{self.last_name} {self.first_name[0]}.'

    return result
