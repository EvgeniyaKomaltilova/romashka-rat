def get_litters_as_string(obj):
    result = ''

    if obj.gender == 'male' and obj.father_litters:
        for litter in obj.father_litters.all():
            result += f'{litter.name}, '
    elif obj.gender == 'female' and obj.mother_litters:
        for litter in obj.mother_litters.all():
            result += f'{litter.name}, '

    result = result[:-2]

    return result
