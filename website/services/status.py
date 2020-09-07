def get_status_based_on_gender(obj):
    """Добавляет окончание 'а' к статусу крысенка женского пола"""

    if obj.gender == 'самка':
        if obj.status == 'свободен':
            return 'свободна'
        elif obj.status == 'зарезервирован':
            return 'зарезервирована'
    else:
        return obj.status
