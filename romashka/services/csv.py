import csv
from django.http import HttpResponse


def get_csv_pedigree(litter):
    """Составляет родословную помета"""
    response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = f'attachment; filename="pedigree-{litter_id}.csv"'
    response['Content-Disposition'] = f'filename="pedigree-{litter.id}.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)

    try:
        writer.writerow([
            f'Литера {litter.name} {litter.prefix}',
            f'Дата рождения: {litter.date_of_birth.strftime("%d.%m.%Y")}',
            f'Заводчик: {litter.breeder}',
            f'№ родословной: {litter.number}'
        ])
    except:
        writer.writerow(['не выбрана литера'])

    writer.writerow([
        'Родители/Parents',
        'Прародители/Grandparents',
        'Пра-прародители/Grand-grandparents',
        'Пра-пра-прародители/Grand-grand-grandparents'
    ])

    if litter.mother:

        # 1 мать - мать матери - М М М - М М М М
        if litter.mother.mother:
            if litter.mother.mother.mother:
                if litter.mother.mother.mother.mother:
                    writer.writerow([
                        '',
                        '',
                        f'Fem.: {litter.mother.mother.mother.full_name}',
                        f'Fem.: {litter.mother.mother.mother.mother.full_name}',
                    ])
                    writer.writerow([
                        '',
                        '',
                        f'{litter.mother.mother.mother.variety}',
                        f'{litter.mother.mother.mother.mother.variety}',
                    ])
                    if litter.mother.mother.mother.owner:
                        if litter.mother.mother.mother.mother.owner:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.mother.mother.mother.owner} '
                                f'({litter.mother.mother.mother.owner.location.city})',
                                f'Вл.: {litter.mother.mother.mother.mother.owner} '
                                f'({litter.mother.mother.mother.mother.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.mother.mother.mother.owner} '
                                f'({litter.mother.mother.mother.owner.location.city})',
                                f'Вл.:',
                            ])
                    elif litter.mother.mother.mother.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.: {litter.mother.mother.mother.mother.owner} '
                            f'({litter.mother.mother.mother.mother.owner.location.city})',
                        ])

                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.:',
                        ])
                else:
                    writer.writerow([
                        '',
                        '',
                        f'Fem.: {litter.mother.mother.mother.full_name}',
                        '',
                    ])
                    writer.writerow([
                        '',
                        '',
                        f'{litter.mother.mother.mother.variety}',
                        'нет данных',
                    ])
                    if litter.mother.mother.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.: {litter.mother.mother.mother.owner} '
                            f'({litter.mother.mother.mother.owner.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            '',
                        ])
        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                'нет данных',
                '',
            ])

        # 2 мать - мать матери - М М М - О М М М
        if litter.mother.mother:
            if litter.mother.mother.mother:
                if litter.mother.mother.mother.father:
                    if litter.mother.mother.mother.breeder:
                        writer.writerow([
                            '',
                            f'Fem.: {litter.mother.mother.full_name}',
                            f'Зав.: {litter.mother.mother.mother.breeder} '
                            f'({litter.mother.mother.mother.breeder.location.city})',
                            f'Male: {litter.mother.mother.mother.father.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Fem.: {litter.mother.mother.full_name}',
                            f'Зав.: нет данных',
                            f'Male: {litter.mother.mother.mother.father.full_name}',
                        ])
                    writer.writerow([
                        '',
                        f'{litter.mother.mother.variety}',
                        f'Д.р.: {litter.mother.mother.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.mother.mother.mother.father.variety}',
                    ])
                    if litter.mother.mother.owner:
                        if litter.mother.mother.mother.father.owner:
                            writer.writerow([
                                '',
                                f'Вл.: {litter.mother.mother.owner} ({litter.mother.mother.owner.location.city})',
                                '',
                                f'Вл.: {litter.mother.mother.mother.father.owner} '
                                f'({litter.mother.mother.mother.father.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                f'Вл.: {litter.mother.mother.owner} ({litter.mother.mother.owner.location.city})',
                                '',
                                f'Вл.:',
                            ])
                    elif litter.mother.mother.mother.father.owner:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            f'Вл.: {litter.mother.mother.mother.father.owner} '
                            f'({litter.mother.mother.mother.father.owner.location.city})',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            f'Вл.:',
                        ])

                else:
                    if litter.mother.mother.mother.breeder:
                        writer.writerow([
                            '',
                            f'Fem.: {litter.mother.mother.full_name}',
                            f'Зав.: {litter.mother.mother.mother.breeder} '
                            f'({litter.mother.mother.mother.breeder.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Fem.: {litter.mother.mother.full_name}',
                            f'Зав.: нет данных',
                            '',
                        ])
                    writer.writerow([
                        '',
                        f'{litter.mother.mother.variety}',
                        f'Д.р.: {litter.mother.mother.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        'нет данных',
                    ])
                    if litter.mother.mother.owner:
                        writer.writerow([
                            '',
                            f'Вл.: {litter.mother.mother.owner} ({litter.mother.mother.owner.location.city})',
                            '',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            '',
                        ])
        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                'нет данных',
                '',
                '',
            ])

        # 3 мать - мать матери - О М М - М О М М
        if litter.mother.mother:
            if litter.mother.mother.father:
                if litter.mother.mother.father.mother:
                    if litter.mother.mother.breeder:
                        writer.writerow([
                            '',
                            f'Зав.: {litter.mother.mother.breeder} ({litter.mother.mother.breeder.location.city})',
                            f'Male: {litter.mother.mother.father.full_name}',
                            f'Fem.: {litter.mother.mother.father.mother.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.mother.mother.father.full_name}',
                            f'Fem.: {litter.mother.mother.father.mother.full_name}',
                        ])
                    writer.writerow([
                        '',
                        f'Д.р.: {litter.mother.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.mother.mother.father.variety}',
                        f'{litter.mother.mother.father.mother.variety}',
                    ])
                    if litter.mother.mother.father.owner:
                        if litter.mother.mother.father.mother.owner:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.mother.mother.father.owner} '
                                f'({litter.mother.mother.father.owner.location.city})',
                                f'Вл.: {litter.mother.mother.father.mother.owner} '
                                f'({litter.mother.mother.father.mother.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.mother.mother.father.owner} '
                                f'({litter.mother.mother.father.owner.location.city})',
                                f'Вл.:',
                            ])
                    elif litter.mother.mother.father.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.: {litter.mother.mother.father.mother.owner} '
                            f'({litter.mother.mother.father.mother.owner.location.city})',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.:',
                        ])
                else:
                    if litter.mother.mother.breeder:
                        writer.writerow([
                            '',
                            f'Зав.: {litter.mother.mother.breeder} ({litter.mother.mother.breeder.location.city})',
                            f'Male: {litter.mother.mother.father.full_name}',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.mother.mother.father.full_name}',
                            '',
                        ])
                    writer.writerow([
                        '',
                        f'Д.р.: {litter.mother.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.mother.mother.father.variety}',
                        'нет данных',
                    ])
                    if litter.mother.mother.father.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.: {litter.mother.mother.father.owner} '
                            f'({litter.mother.mother.father.owner.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            '',
                        ])
        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                'нет данных',
                '',
            ])

        # 4 мать - мать матери - O М М - О O М М
        if litter.mother.mother:
            if litter.mother.mother.father:
                if litter.mother.mother.father.father:
                    if litter.mother.mother.father.breeder:
                        writer.writerow([
                            f'Fem.: {litter.mother.full_name}',
                            '',
                            f'Зав.: {litter.mother.mother.father.breeder} '
                            f'({litter.mother.mother.father.breeder.location.city})',
                            f'Male: {litter.mother.mother.father.father.full_name}',
                        ])
                    else:
                        writer.writerow([
                            f'Fem.: {litter.mother.full_name}',
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.mother.mother.father.father.full_name}',
                        ])
                    writer.writerow([
                        f'{litter.mother.variety}',
                        '',
                        f'Д.р.: {litter.mother.mother.father.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.mother.mother.father.father.variety}',
                    ])
                    if litter.mother.owner:
                        if litter.mother.mother.father.father.owner:
                            writer.writerow([
                                f'Вл.: {litter.mother.owner} ({litter.mother.owner.location.city})',
                                '',
                                '',
                                f'Вл.: {litter.mother.mother.father.father.owner} '
                                f'({litter.mother.mother.father.father.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                f'Вл.: {litter.mother.owner} ({litter.mother.owner.location.city})',
                                '',
                                '',
                                f'Вл.:',
                            ])
                    elif litter.mother.mother.father.father.owner:
                        writer.writerow([
                            f'Вл.:',
                            '',
                            '',
                            f'Вл.: {litter.mother.mother.father.father.owner} '
                            f'({litter.mother.mother.father.father.owner.location.city})',
                        ])
                    else:
                        writer.writerow([
                            f'Вл.:',
                            '',
                            '',
                            f'Вл.:',
                        ])

                else:
                    if litter.mother.mother.father.breeder:
                        writer.writerow([
                            f'Fem.: {litter.mother.full_name}',
                            '',
                            f'Зав.: {litter.mother.mother.father.breeder} '
                            f'({litter.mother.mother.father.breeder.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            f'Fem.: {litter.mother.full_name}',
                            '',
                            f'Зав.: нет данных',
                            '',
                        ])
                    writer.writerow([
                        f'{litter.mother.variety}',
                        '',
                        f'Д.р.: {litter.mother.mother.father.date_of_birth.strftime("%d.%m.%Y")}',
                        'нет данных',
                    ])
                    if litter.mother.owner:
                        writer.writerow([
                            f'Вл.: {litter.mother.owner} ({litter.mother.owner.location.city})',
                            '',
                            '',
                            '',
                        ])
                    else:
                        writer.writerow([
                            f'Вл.:',
                            '',
                            '',
                            '',
                        ])
        else:
            writer.writerow([
                f'Fem.: {litter.mother.full_name}',
                '',
                '',
                '',
            ])
            writer.writerow([
                f'{litter.mother.variety}',
                '',
                '',
                'нет данных',
            ])
            if litter.mother.owner:
                writer.writerow([
                    f'Вл.: {litter.mother.owner} ({litter.mother.owner.location.city})',
                    '',
                    '',
                    '',
                ])
            else:
                writer.writerow([
                    f'Вл.:',
                    '',
                    '',
                    '',
                ])

        # 5 мать - отец матери - М O М - М М О М
        if litter.mother.father:
            if litter.mother.father.mother:
                if litter.mother.father.mother.mother:
                    if litter.mother.breeder:
                        writer.writerow([
                            f'Зав.: {litter.mother.breeder} ({litter.mother.breeder.location.city})',
                            '',
                            f'Fem.: {litter.mother.father.mother.full_name}',
                            f'Fem.: {litter.mother.father.mother.mother.full_name}',
                        ])
                    else:
                        writer.writerow([
                            f'Зав.: нет данных',
                            '',
                            f'Fem.: {litter.mother.father.mother.full_name}',
                            f'Fem.: {litter.mother.father.mother.mother.full_name}',
                        ])
                    writer.writerow([
                        f'Д.р.: {litter.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        '',
                        f'{litter.mother.father.mother.variety}',
                        f'{litter.mother.father.mother.mother.variety}',
                    ])
                    if litter.mother.father.mother.owner:
                        if litter.mother.father.mother.mother.owner:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.mother.father.mother.owner} '
                                f'({litter.mother.father.mother.owner.location.city})',
                                f'Вл.: {litter.mother.father.mother.mother.owner} '
                                f'({litter.mother.father.mother.mother.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.mother.father.mother.owner} '
                                f'({litter.mother.father.mother.owner.location.city})',
                                f'Вл.:',
                            ])
                    elif litter.mother.father.mother.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.: {litter.mother.father.mother.mother.owner} '
                            f'({litter.mother.father.mother.mother.owner.location.city})',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.:',
                        ])
                else:
                    if litter.mother.breeder:
                        writer.writerow([
                            f'Зав.: {litter.mother.breeder} ({litter.mother.breeder.location.city})',
                            '',
                            f'Fem.: {litter.mother.father.mother.full_name}',
                            '',
                        ])
                    else:
                        writer.writerow([
                            f'Зав.: нет данных',
                            '',
                            f'Fem.: {litter.mother.father.mother.full_name}',
                            '',
                        ])
                    writer.writerow([
                        f'Д.р.: {litter.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        '',
                        f'{litter.mother.father.mother.variety}',
                        'нет данных',
                    ])
                    if litter.mother.father.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.: {litter.mother.father.mother.owner} '
                            f'({litter.mother.father.mother.owner.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            '',
                        ])
            else:
                if litter.mother.breeder:
                    writer.writerow([
                        f'Зав.: {litter.mother.breeder} ({litter.mother.breeder.location.city})',
                        '',
                        f'Fem.: {litter.mother.father.mother.full_name}',
                        '',
                    ])
                else:
                    writer.writerow([
                        f'Зав.: нет данных',
                        '',
                        f'Fem.: {litter.mother.father.mother.full_name}',
                        '',
                    ])
                writer.writerow([
                    f'Д.р.: {litter.mother.date_of_birth.strftime("%d.%m.%Y")}',
                    '',
                    f'{litter.mother.father.mother.variety}',
                    'нет данных',
                ])
                writer.writerow([
                        '',
                        '',
                        f'Вл.:',
                        '',
                    ])

        else:
            if litter.mother.breeder:
                writer.writerow([
                    f'Зав.: {litter.mother.breeder} ({litter.mother.breeder.location.city})',
                    '',
                    '',
                    '',
                ])
            else:
                writer.writerow([
                    f'Зав.: нет данных',
                    '',
                    '',
                    '',
                ])
            writer.writerow([
                f'Д.р.: {litter.mother.date_of_birth.strftime("%d.%m.%Y")}',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                'нет данных',
                '',
            ])

        # 6 мать - отец матери - M O М - О M O М
        if litter.mother.father:
            if litter.mother.father.mother:
                if litter.mother.father.mother.father:
                    if litter.mother.father.mother.breeder:
                        writer.writerow([
                            '',
                            f'Male: {litter.mother.father.full_name}',
                            f'Зав.: {litter.mother.father.mother.breeder} '
                            f'({litter.mother.father.mother.breeder.location.city})',
                            f'Male: {litter.mother.father.mother.father.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Male: {litter.mother.father.full_name}',
                            f'Зав.: нет данных',
                            f'Male: {litter.mother.father.mother.father.full_name}',
                        ])
                    writer.writerow([
                        '',
                        f'{litter.mother.father.variety}',
                        f'Д.р.: {litter.mother.father.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.mother.father.mother.father.variety}',
                    ])

                    if litter.mother.father.owner:
                        if litter.mother.father.mother.father.owner:
                            writer.writerow([
                                '',
                                f'Вл.: {litter.mother.father.owner} ({litter.mother.father.owner.location.city})',
                                '',
                                f'Вл.: {litter.mother.father.mother.father.owner} '
                                f'({litter.mother.father.mother.father.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                f'Вл.: {litter.mother.father.owner} ({litter.mother.father.owner.location.city})',
                                '',
                                f'Вл.:',
                            ])

                    elif litter.mother.father.mother.father.owner:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            f'Вл.: {litter.mother.father.mother.father.owner} '
                            f'({litter.mother.father.mother.father.owner.location.city})',
                        ])

                    else:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            f'Вл.:',
                        ])

                else:
                    if litter.mother.father.mother.breeder:
                        writer.writerow([
                            '',
                            f'Male: {litter.mother.father.full_name}',
                            f'Зав.: {litter.mother.father.mother.breeder} '
                            f'({litter.mother.father.mother.breeder.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Male: {litter.mother.father.full_name}',
                            f'Зав.: нет данных',
                            '',
                        ])
                    writer.writerow([
                        '',
                        f'{litter.mother.father.variety}',
                        f'Д.р.: {litter.mother.father.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        'нет данных',
                    ])
                    if litter.mother.father.owner:
                        writer.writerow([
                            '',
                            f'Вл.: {litter.mother.father.owner} ({litter.mother.father.owner.location.city})',
                            '',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            '',
                        ])

        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                '',
                '',
            ])

        # 7 мать - отец матери - О O М - М О O М
        if litter.mother.father:
            if litter.mother.father.father:
                if litter.mother.father.father.mother:
                    if litter.mother.father.breeder:
                        writer.writerow([
                            '',
                            f'Зав.: {litter.mother.father.breeder} ({litter.mother.father.breeder.location.city})',
                            f'Male: {litter.mother.father.father.full_name}',
                            f'Fem.: {litter.mother.father.father.mother.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.mother.father.father.full_name}',
                            f'Fem.: {litter.mother.father.father.mother.full_name}',
                        ])

                    writer.writerow([
                        '',
                        f'Д.р.: {litter.mother.father.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.mother.father.father.variety}',
                        f'{litter.mother.father.father.mother.variety}',
                    ])
                    writer.writerow([
                        '',
                        '',
                        f'{litter.mother.father.father.owner} '
                        f'({litter.mother.father.father.owner.location.city})',
                        f'{litter.mother.father.father.mother.owner} '
                        f'({litter.mother.father.father.mother.owner.location.city})',
                    ])
                else:
                    if litter.mother.father.breeder:
                        writer.writerow([
                            '',
                            f'Зав.: {litter.mother.father.breeder} ({litter.mother.father.breeder.location.city})',
                            f'Male: {litter.mother.father.father.full_name}',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.mother.father.father.full_name}',
                            '',
                        ])

                    writer.writerow([
                        '',
                        f'Д.р.: {litter.mother.father.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.mother.father.father.variety}',
                        'нет данных',
                    ])
                    if litter.mother.father.father.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.: {litter.mother.father.father.owner} '
                            f'({litter.mother.father.father.owner.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.: ',
                            '',
                        ])

        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                'нет данных',
                '',
            ])

        # 8 мать - отец матери - O О М - О O О М
        if litter.mother.father:
            if litter.mother.father.father:
                if litter.mother.father.father.father:
                    if litter.mother.father.father.breeder:
                        writer.writerow([
                            '',
                            '',
                            f'Зав.: {litter.mother.father.father.breeder} '
                            f'({litter.mother.father.father.breeder.location.city})',
                            f'Male: {litter.mother.father.father.father.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.mother.father.father.father.full_name}',
                        ])
                    writer.writerow([
                        '',
                        '',
                        f'Д.р.: {litter.mother.father.father.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.mother.father.father.father.variety}',
                    ])
                    if litter.mother.father.father.father.owner:
                        writer.writerow([
                            '',
                            '',
                            '',
                            f'Вл.: {litter.mother.father.father.father.owner}'
                            f'({litter.mother.father.father.father.owner.location.city})',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            '',
                            f'Вл.:',
                        ])

                else:
                    if litter.mother.father.father.breeder:
                        writer.writerow([
                            '',
                            '',
                            f'Зав.: {litter.mother.father.father.breeder} '
                            f'({litter.mother.father.father.breeder.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Зав.: нет данных',
                            '',
                        ])
                    writer.writerow([
                        '',
                        '',
                        f'Д.р.: {litter.mother.father.father.date_of_birth.strftime("%d.%m.%Y")}',
                        'нет данных',
                    ])
                    writer.writerow([
                        '',
                        '',
                        '',
                        '',
                    ])
        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                '',
                '',
            ])

    if litter.father:

        # 9 отец - мать отца - М М О - М М М О
        if litter.father.mother:
            if litter.father.mother.mother:
                if litter.father.mother.mother.mother:
                    writer.writerow([
                        '',
                        '',
                        f'Fem.: {litter.father.mother.mother.full_name}',
                        f'Fem.: {litter.father.mother.mother.mother.full_name}',
                    ])
                    writer.writerow([
                        '',
                        '',
                        f'{litter.father.mother.mother.variety}',
                        f'{litter.father.mother.mother.mother.variety}',
                    ])
                    if litter.father.mother.mother.owner:
                        if litter.father.mother.mother.mother.owner:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.father.mother.mother.owner} '
                                f'({litter.father.mother.mother.owner.location.city})',
                                f'Вл.: {litter.father.mother.mother.mother.owner} '
                                f'({litter.father.mother.mother.mother.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.father.mother.mother.owner} '
                                f'({litter.father.mother.mother.owner.location.city})',
                                f'Вл.:',
                            ])

                    elif litter.father.mother.mother.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.: {litter.father.mother.mother.mother.owner} '
                            f'({litter.father.mother.mother.mother.owner.location.city})',
                        ])

                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.:',
                        ])

                else:
                    writer.writerow([
                        '',
                        '',
                        f'Fem.: {litter.father.mother.mother.full_name}',
                        '',
                    ])
                    writer.writerow([
                        '',
                        '',
                        f'{litter.father.mother.mother.variety}',
                        'нет данных',
                    ])
                    if litter.father.mother.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.: {litter.father.mother.mother.owner} '
                            f'({litter.father.mother.mother.owner.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            '',
                        ])

        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                'нет данных',
                '',
            ])

        # 10 отец - мать отца - М М О - О М М О
        if litter.father.mother:
            if litter.father.mother.mother:
                if litter.father.mother.mother.father:
                    if litter.father.mother.mother.breeder:
                        writer.writerow([
                            '',
                            f'Fem.: {litter.father.mother.full_name}',
                            f'Зав.: {litter.father.mother.mother.breeder} '
                            f'({litter.father.mother.mother.breeder.location.city})',
                            f'Male: {litter.father.mother.mother.father.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Fem.: {litter.father.mother.full_name}',
                            f'Зав.: нет данных',
                            f'Male: {litter.father.mother.mother.father.full_name}',
                        ])
                    writer.writerow([
                        '',
                        f'{litter.father.mother.variety}',
                        f'Д.р.: {litter.father.mother.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.father.mother.mother.father.variety}',
                    ])

                    if litter.father.mother.owner:
                        if litter.father.mother.mother.father.owner:
                            writer.writerow([
                                '',
                                f'Вл.: {litter.father.mother.owner} ({litter.father.mother.owner.location.city})',
                                '',
                                f'Вл.: {litter.father.mother.mother.father.owner} '
                                f'({litter.father.mother.mother.father.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                f'Вл.: {litter.father.mother.owner} ({litter.father.mother.owner.location.city})',
                                '',
                                f'Вл.:',
                            ])

                    elif litter.father.mother.mother.father.owner:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            f'Вл.: {litter.father.mother.mother.father.owner} '
                            f'({litter.father.mother.mother.father.owner.location.city})',
                        ])

                    else:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            f'Вл.:',
                        ])
                else:
                    if litter.father.mother.mother.breeder:
                        writer.writerow([
                            '',
                            f'Fem.: {litter.father.mother.full_name}',
                            f'Зав.: {litter.father.mother.mother.breeder} '
                            f'({litter.father.mother.mother.breeder.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Fem.: {litter.father.mother.full_name}',
                            f'Зав.: нет данных',
                            '',
                        ])
                    writer.writerow([
                        '',
                        f'{litter.father.mother.variety}',
                        f'Д.р.: {litter.father.mother.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        'нет данных',
                    ])
                    if litter.father.mother.owner:
                        writer.writerow([
                            '',
                            f'Вл.: {litter.father.mother.owner} ({litter.father.mother.owner.location.city})',
                            '',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            '',
                        ])

        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                'нет данных',
                '',
                '',
            ])

        # 11 отец - мать отца - О М О - М О М О
        if litter.father.mother:
            if litter.father.mother.father:
                if litter.father.mother.father.mother:
                    if litter.father.mother.breeder:
                        writer.writerow([
                            '',
                            f'Зав.: {litter.father.mother.breeder} ({litter.father.mother.breeder.location.city})',
                            f'Male: {litter.father.mother.father.full_name}',
                            f'Fem.: {litter.father.mother.father.mother.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.father.mother.father.full_name}',
                            f'Fem.: {litter.father.mother.father.mother.full_name}',
                        ])
                    writer.writerow([
                        '',
                        f'Д.р.: {litter.father.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.father.mother.father.variety}',
                        f'{litter.father.mother.father.mother.variety}',
                    ])
                    if litter.father.mother.father.owner:
                        if litter.father.mother.father.mother.owner:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.father.mother.father.owner} '
                                f'({litter.father.mother.father.owner.location.city})',
                                f'Вл.: {litter.father.mother.father.mother.owner} '
                                f'({litter.father.mother.father.mother.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.father.mother.father.owner} '
                                f'({litter.father.mother.father.owner.location.city})',
                                f'Вл.:',
                            ])
                    elif litter.father.mother.father.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.: {litter.father.mother.father.mother.owner} '
                            f'({litter.father.mother.father.mother.owner.location.city})',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.:',
                        ])
                else:
                    if litter.father.mother.breeder:
                        writer.writerow([
                            '',
                            f'Зав.: {litter.father.mother.breeder} ({litter.father.mother.breeder.location.city})',
                            f'Male: {litter.father.mother.father.full_name}',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.father.mother.father.full_name}',
                            '',
                        ])
                    writer.writerow([
                        '',
                        f'Д.р.: {litter.father.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.father.mother.father.variety}',
                        'нет данных',
                    ])
                    if litter.father.mother.father.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.: {litter.father.mother.father.owner} '
                            f'({litter.father.mother.father.owner.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            '',
                        ])
        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                'нет данных',
                '',
            ])

        # 12 отец - мать отца - O М О - О O М О
        if litter.father.mother:
            if litter.father.mother.father:
                if litter.father.mother.father.father:
                    if litter.father.mother.father.breeder:
                        writer.writerow([
                            f'Male: {litter.father.full_name}',
                            '',
                            f'Зав.: {litter.father.mother.father.breeder} '
                            f'({litter.father.mother.father.breeder.location.city})',
                            f'Male: {litter.father.mother.father.father.full_name}',
                        ])
                    else:
                        writer.writerow([
                            f'Male: {litter.father.full_name}',
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.father.mother.father.father.full_name}',
                        ])
                    writer.writerow([
                        f'{litter.father.variety}',
                        '',
                        f'Д.р.: {litter.father.mother.father.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.father.mother.father.father.variety}',
                    ])
                    if litter.father.owner:
                        if litter.father.mother.father.father.owner:
                            writer.writerow([
                                f'Вл.: {litter.father.owner} ({litter.father.owner.location.city})',
                                '',
                                '',
                                f'Вл.: {litter.father.mother.father.father.owner} '
                                f'({litter.father.mother.father.father.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                f'Вл.: {litter.father.owner} ({litter.father.owner.location.city})',
                                '',
                                '',
                                f'Вл.:',
                            ])
                    elif litter.father.mother.father.father.owner:
                        writer.writerow([
                            f'Вл.:',
                            '',
                            '',
                            f'Вл.: {litter.father.mother.father.father.owner} '
                            f'({litter.father.mother.father.father.owner.location.city})',
                        ])
                    else:
                        writer.writerow([
                            f'Вл.:',
                            '',
                            '',
                            f'Вл.:',
                        ])
                else:
                    if litter.father.mother.father.breeder:
                        writer.writerow([
                            f'Male: {litter.father.full_name}',
                            '',
                            f'Зав.: {litter.father.mother.father.breeder} '
                            f'({litter.father.mother.father.breeder.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            f'Male: {litter.father.full_name}',
                            '',
                            f'Зав.: нет данных',
                            '',
                        ])
                    writer.writerow([
                        f'{litter.father.variety}',
                        '',
                        f'Д.р.: {litter.father.mother.father.date_of_birth.strftime("%d.%m.%Y")}',
                        'нет данных',
                    ])
                    if litter.father.owner:
                        writer.writerow([
                            f'Вл.: {litter.father.owner} ({litter.father.owner.location.city})',
                            '',
                            '',
                            '',
                        ])
                    else:
                        writer.writerow([
                            f'Вл.:',
                            '',
                            '',
                            '',
                        ])
        else:
            writer.writerow([
                f'Male: {litter.father.full_name}',
                '',
                '',
                '',
            ])
            writer.writerow([
                f'{litter.father.variety}',
                '',
                '',
                'нет данных',
            ])
            if litter.father.owner:
                writer.writerow([
                    f'Вл.: {litter.father.owner} ({litter.father.owner.location.city})',
                    '',
                    '',
                    '',
                ])
            else:
                writer.writerow([
                    f'Вл.:',
                    '',
                    '',
                    '',
                ])

        # 13 отец - отец отца - М O О - М М О О
        if litter.father.father:
            if litter.father.father.mother:
                if litter.father.father.mother.mother:
                    if litter.father.breeder:
                        writer.writerow([
                            f'Зав.: {litter.father.breeder} ({litter.father.breeder.location.city})',
                            '',
                            f'Fem.: {litter.father.father.mother.full_name}',
                            f'Fem.: {litter.father.father.mother.mother.full_name}',
                        ])
                    else:
                        writer.writerow([
                            f'Зав.: нет данных',
                            '',
                            f'Fem.: {litter.father.father.mother.full_name}',
                            f'Fem.: {litter.father.father.mother.mother.full_name}',
                        ])
                    writer.writerow([
                        f'Д.р.: {litter.father.date_of_birth.strftime("%d.%m.%Y")}',
                        '',
                        f'{litter.father.father.mother.variety}',
                        f'{litter.father.father.mother.mother.variety}',
                    ])
                    if litter.father.father.mother.owner:
                        if litter.father.father.mother.mother.owner:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.father.father.mother.owner} '
                                f'({litter.father.father.mother.owner.location.city})',
                                f'Вл.: {litter.father.father.mother.mother.owner} '
                                f'({litter.father.father.mother.mother.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                '',
                                f'Вл.: {litter.father.father.mother.owner} '
                                f'({litter.father.father.mother.owner.location.city})',
                                f'Вл.:',
                            ])
                    elif litter.father.father.mother.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.: {litter.father.father.mother.mother.owner} '
                            f'({litter.father.father.mother.mother.owner.location.city})',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            f'Вл.:',
                        ])
                else:
                    if litter.father.breeder:
                        writer.writerow([
                            f'Зав.: {litter.father.breeder} ({litter.father.breeder.location.city})',
                            '',
                            f'Fem.: {litter.father.father.mother.full_name}',
                            '',
                        ])
                    else:
                        writer.writerow([
                            f'Зав.: нет данных',
                            '',
                            f'Fem.: {litter.father.father.mother.full_name}',
                            '',
                        ])
                    writer.writerow([
                        f'Д.р.: {litter.father.date_of_birth.strftime("%d.%m.%Y")}',
                        '',
                        f'{litter.father.father.mother.variety}',
                        'нет данных',
                    ])
                    if litter.father.father.mother.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.: {litter.father.father.mother.owner} '
                            f'({litter.father.father.mother.owner.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            '',
                        ])
            else:
                if litter.father.breeder:
                    writer.writerow([
                        f'Зав.: {litter.father.breeder} ({litter.father.breeder.location.city})',
                        '',
                        '',
                        '',
                    ])
                else:
                    writer.writerow([
                        f'Зав.: нет данных',
                        '',
                        '',
                        '',
                    ])
                writer.writerow([
                    f'Д.р.: {litter.father.date_of_birth.strftime("%d.%m.%Y")}',
                    '',
                    '',
                    'нет данных',
                ])
                writer.writerow([
                    '',
                    '',
                    f'нет данных',
                    '',
                ])

        else:
            if litter.father.breeder:
                writer.writerow([
                    f'Зав.: {litter.father.breeder} ({litter.father.breeder.location.city})',
                    '',
                    '',
                    '',
                ])
            else:
                writer.writerow([
                    f'Зав.: нет данных',
                    '',
                    '',
                    '',
                ])
            writer.writerow([
                f'Д.р.: {litter.father.date_of_birth.strftime("%d.%m.%Y")}',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                'нет данных',
                '',
            ])

        # 14 отец - отец отца - M O О - О M O О
        if litter.father.father:
            if litter.father.father.mother:
                if litter.father.father.mother.father:
                    if litter.father.father.mother.breeder:
                        writer.writerow([
                            '',
                            f'Male: {litter.father.father.full_name}',
                            f'Зав.: {litter.father.father.mother.breeder} '
                            f'({litter.father.father.mother.breeder.location.city})',
                            f'Male: {litter.father.father.mother.father.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Male: {litter.father.father.full_name}',
                            f'Зав.: нет данных',
                            f'Male: {litter.father.father.mother.father.full_name}',
                        ])

                    writer.writerow([
                        '',
                        f'{litter.father.father.variety}',
                        f'Д.р.: {litter.father.father.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.father.father.mother.father.variety}',
                    ])
                    if litter.father.father.owner:
                        if litter.father.father.mother.father.owner:
                            writer.writerow([
                                '',
                                f'Вл.: {litter.father.father.owner} ({litter.father.father.owner.location.city})',
                                '',
                                f'Вл.: {litter.father.father.mother.father.owner} '
                                f'({litter.father.father.mother.father.owner.location.city})',
                            ])
                        else:
                            writer.writerow([
                                '',
                                f'Вл.: {litter.father.father.owner} ({litter.father.father.owner.location.city})',
                                '',
                                f'Вл.:',
                            ])

                    elif litter.father.father.mother.father.owner:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            f'Вл.: {litter.father.father.mother.father.owner} '
                            f'({litter.father.father.mother.father.owner.location.city})',
                        ])

                    else:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            f'Вл.:',
                        ])

                else:
                    if litter.father.father.mother.breeder:
                        writer.writerow([
                            '',
                            f'Male: {litter.father.father.full_name}',
                            f'Зав.: {litter.father.father.mother.breeder} '
                            f'({litter.father.father.mother.breeder.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Male: {litter.father.father.full_name}',
                            f'Зав.: нет данных',
                            '',
                        ])

                    writer.writerow([
                        '',
                        f'{litter.father.father.variety}',
                        f'Д.р.: {litter.father.father.mother.date_of_birth.strftime("%d.%m.%Y")}',
                        'нет данных',
                    ])
                    if litter.father.father.owner:
                        writer.writerow([
                            '',
                            f'Вл.: {litter.father.father.owner} ({litter.father.father.owner.location.city})',
                            '',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Вл.:',
                            '',
                            '',
                        ])
        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                'нет данных',
                '',
                '',
            ])

        # 15 отец - отец отца - О O О - М О O О
        if litter.father.father:
            if litter.father.father.father:
                if litter.father.father.father.mother:
                    if litter.father.father.breeder:
                        writer.writerow([
                            '',
                            f'Зав.: {litter.father.father.breeder} ({litter.father.father.breeder.location.city})',
                            f'Male: {litter.father.father.father.full_name}',
                            f'Fem.: {litter.father.father.father.mother.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.father.father.father.full_name}',
                            f'Fem.: {litter.father.father.father.mother.full_name}',
                        ])

                    writer.writerow([
                        '',
                        f'Д.р.: {litter.father.father.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.father.father.father.variety}',
                        f'{litter.father.father.father.mother.variety}',
                    ])
                    writer.writerow([
                        '',
                        '',
                        f'{litter.father.father.father.owner} '
                        f'({litter.father.father.father.owner.location.city})',
                        f'{litter.father.father.father.mother.owner} '
                        f'({litter.father.father.father.mother.owner.location.city})',
                    ])
                else:
                    if litter.father.father.breeder:
                        writer.writerow([
                            '',
                            f'Зав.: {litter.father.father.breeder} ({litter.father.father.breeder.location.city})',
                            f'Male: {litter.father.father.father.full_name}',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.father.father.father.full_name}',
                            '',
                        ])

                    writer.writerow([
                        '',
                        f'Д.р.: {litter.father.father.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.father.father.father.variety}',
                        'нет данных',
                    ])
                    if litter.father.father.father.owner:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.: {litter.father.father.father.owner} '
                            f'({litter.father.father.father.owner.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Вл.:',
                            '',
                        ])
        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                'нет данных',
                '',
            ])

        # 16 отец - отец отца - O О О - О O О О
        if litter.father.father:
            if litter.father.father.father:
                if litter.father.father.father.father:
                    if litter.father.father.father.breeder:
                        writer.writerow([
                            '',
                            '',
                            f'Зав.: {litter.father.father.father.breeder} '
                            f'({litter.father.father.father.breeder.location.city})',
                            f'Male: {litter.father.father.father.father.full_name}',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Зав.: нет данных',
                            f'Male: {litter.father.father.father.father.full_name}',
                        ])
                    writer.writerow([
                        '',
                        '',
                        f'Д.р.: {litter.father.father.father.date_of_birth.strftime("%d.%m.%Y")}',
                        f'{litter.father.father.father.father.variety}',
                    ])
                    if litter.father.father.father.father.owner:
                        writer.writerow([
                            '',
                            '',
                            '',
                            f'Вл.: {litter.father.father.father.father.owner}'
                            f'({litter.father.father.father.father.owner.location.city})',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            '',
                            f'Вл.:',
                        ])

                else:
                    if litter.father.father.father.breeder:
                        writer.writerow([
                            '',
                            '',
                            f'Зав.: {litter.father.father.father.breeder} '
                            f'({litter.father.father.father.breeder.location.city})',
                            '',
                        ])
                    else:
                        writer.writerow([
                            '',
                            '',
                            f'Зав.: нет данных',
                            '',
                        ])
                    writer.writerow([
                        '',
                        '',
                        f'Д.р.: {litter.father.father.father.date_of_birth.strftime("%d.%m.%Y")}',
                        'нет данных',
                    ])
                    writer.writerow([
                        '',
                        '',
                        '',
                        '',
                    ])
        else:
            writer.writerow([
                '',
                '',
                '',
                '',
            ])
            writer.writerow([
                '',
                '',
                '',
                'нет данных',
            ])
            writer.writerow([
                '',
                '',
                '',
                '',
            ])

    return response
