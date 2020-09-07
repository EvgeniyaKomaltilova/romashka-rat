def get_status_based_on_gender(obj):
    """Добавляет окончание 'а' к статусу крысенка женского пола"""

    if obj.gender == 'female':
        if obj.status == 'available':
            return 'свободна'
        elif obj.status == 'reserved':
            return 'зарезервирована'
    else:
        return obj.status
