def get_timedelta_as_string(seconds):
    years = _count_years(seconds)
    months = _count_months(seconds)

    if years == 0 and months == 0:
        return 'меньше месяца'
    elif years == 0 and months != 0:
        return _get_months_as_string(months)
    else:
        return _get_years_as_string(years) + ' ' + _get_months_as_string(months)


def _count_years(seconds):
    seconds_in_year = 31_518_720
    return int(seconds // seconds_in_year)


def _count_months(seconds):
    seconds_in_month = 2_626_560
    seconds_in_year = 31_518_720
    years = _count_years(seconds)
    return int((seconds - int(years) * seconds_in_year) // seconds_in_month)


def _get_years_as_string(years):
    if years == 1:
        return f'{years} год'
    elif 2 <= years <= 4:
        return f'{years} года'
    else:
        return f'{years} лет'


def _get_months_as_string(months):
    if months == 1:
        return f'{months} месяц'
    elif 2 <= months <= 4:
        return f'{months} месяца'
    else:
        return f'{months} месяцев'
