from datetime import date


def get_rat_current_age(obj):
    """Возвращает разницу между датой рождения и текущей датой"""
    current_age = date.today() - obj.date_of_birth
    seconds = current_age.total_seconds()
    return _get_timedelta_as_string(seconds)


def get_rat_lifespan(obj):
    """Возвращает разницу между датой рождения и датой смерти"""
    lifespan = obj.date_of_death - obj.date_of_birth
    seconds = lifespan.total_seconds()
    return _get_timedelta_as_string(seconds)


def _get_timedelta_as_string(seconds):
    """Возвращает строку, содержащую количество лет и месяцев в правильной форме"""
    years = _count_years(seconds)
    months = _count_months(seconds)

    if years == 0 and months == 0:
        return 'меньше месяца'
    elif years == 0 and months != 0:
        return _get_months_as_string(months)
    else:
        return _get_years_as_string(years) + ' ' + _get_months_as_string(months)


def _count_years(seconds):
    """Вычисляет количество полных лет из заданного количества секунд"""
    seconds_in_year = 31_518_720
    return int(seconds // seconds_in_year)


def _count_months(seconds):
    """Вычисляет количество месяцев в неполном году"""
    seconds_in_month = 2_626_560
    seconds_in_year = 31_518_720
    years = _count_years(seconds)
    return int((seconds - int(years) * seconds_in_year) // seconds_in_month)


def _get_years_as_string(years):
    """Возвращает строку с количеством лет в правильной форме"""
    if years == 1:
        return f'{years} год'
    elif 2 <= years <= 4:
        return f'{years} года'
    else:
        return f'{years} лет'


def _get_months_as_string(months):
    """Возвращает строку с количеством месяцев в правильной форме"""
    if months == 1:
        return f'{months} месяц'
    elif 2 <= months <= 4:
        return f'{months} месяца'
    else:
        return f'{months} месяцев'
