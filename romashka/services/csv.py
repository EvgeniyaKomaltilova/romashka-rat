import csv
from django.http import HttpResponse


def get_csv_pedigree(litter):
    response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = f'attachment; filename="pedigree-{litter_id}.csv"'
    response['Content-Disposition'] = f'filename="pedigree-{litter.id}.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)

    writer.writerow(['Питомник декоративных крыс "Ромашка", г.Санкт-Петербург'])
    writer.writerow(['Родословная декоративной крысы'])

    try:
        writer.writerow([
            f'Литера {litter.name} {litter.prefix}',
            f'Дата рождения: {litter.date_of_birth}',
            f'Заводчик: {litter.breeder}'
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
                        f'Fem.: {litter.mother.mother.mother.full_name}',
                        '',
                    ])
                    writer.writerow([
                        '',
                        '',
                        f'{litter.mother.mother.mother.variety}',
                        'нет данных',
                    ])
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
                    writer.writerow([
                        '',
                        f'Fem.: {litter.mother.mother.full_name}',
                        f'Зав.: {litter.mother.mother.mother.breeder} '
                        f'({litter.mother.mother.mother.breeder.location.city})',
                        f'Male: {litter.mother.mother.mother.father.full_name}',
                    ])
                    writer.writerow([
                        '',
                        f'{litter.mother.mother.variety}',
                        f'Д.р.: {litter.mother.mother.mother.date_of_birth}',
                        f'{litter.mother.mother.mother.father.variety}',
                    ])
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
                        f'Fem.: {litter.mother.mother.full_name}',
                        f'Зав.: {litter.mother.mother.mother.breeder} '
                        f'({litter.mother.mother.mother.breeder.location.city})',
                        '',
                    ])
                    writer.writerow([
                        '',
                        f'{litter.mother.mother.variety}',
                        f'Д.р.: {litter.mother.mother.mother.date_of_birth}',
                        'нет данных',
                    ])
                    writer.writerow([
                        '',
                        f'Вл.: {litter.mother.mother.owner} ({litter.mother.mother.owner.location.city})',
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
                    writer.writerow([
                        '',
                        f'Зав.: {litter.mother.mother.breeder} ({litter.mother.mother.breeder.location.city})',
                        f'Male: {litter.mother.mother.father.full_name}',
                        f'Fem.: {litter.mother.mother.father.mother.full_name}',
                    ])
                    writer.writerow([
                        '',
                        f'Д.р.: {litter.mother.mother.date_of_birth})',
                        f'{litter.mother.mother.father.variety}',
                        f'{litter.mother.mother.father.mother.variety}',
                    ])
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
                        f'Зав.: {litter.mother.mother.breeder} ({litter.mother.mother.breeder.location.city})',
                        f'Male: {litter.mother.mother.father.full_name}',
                        '',
                    ])
                    writer.writerow([
                        '',
                        f'Д.р.: {litter.mother.mother.date_of_birth})',
                        f'{litter.mother.mother.father.variety}',
                        'нет данных',
                    ])
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
                    writer.writerow([
                        f'Fem.: {litter.mother.full_name}',
                        '',
                        f'Зав.: {litter.mother.mother.father.breeder} '
                        f'({litter.mother.mother.father.breeder.location.city})',
                        f'Male: {litter.mother.mother.father.father.full_name}',
                    ])
                    writer.writerow([
                        f'{litter.mother.variety}',
                        '',
                        f'Д.р.: {litter.mother.mother.father.date_of_birth}',
                        f'{litter.mother.mother.father.father.variety}',
                    ])
                    writer.writerow([
                        f'Вл.: {litter.mother.owner} ({litter.mother.owner.location.city})',
                        '',
                        '',
                        f'Вл.: {litter.mother.mother.father.father.owner} '
                        f'({litter.mother.mother.father.father.owner.location.city})',
                    ])
                else:
                    writer.writerow([
                        f'Fem.: {litter.mother.full_name}',
                        '',
                        f'Зав.: {litter.mother.mother.father.breeder} '
                        f'({litter.mother.mother.father.breeder.location.city})',
                        '',
                    ])
                    writer.writerow([
                        f'{litter.mother.variety}',
                        '',
                        f'Д.р.: {litter.mother.mother.father.date_of_birth}',
                        'нет данных',
                    ])
                    writer.writerow([
                        f'Вл.: {litter.mother.owner} ({litter.mother.owner.location.city})',
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

        # 5 мать - отец матери - М O М - М М О М
        if litter.mother.father:
            if litter.mother.father.mother:
                if litter.mother.father.mother.mother:
                    writer.writerow([
                        f'Зав.: {litter.mother.breeder} ({litter.mother.breeder.location.city})'
                        '',
                        f'Fem.: {litter.mother.father.mother.full_name}',
                        f'Fem.: {litter.mother.father.mother.mother.full_name}',
                    ])
                    writer.writerow([
                        f'Д.р.: {litter.mother.date_of_birth})'
                        '',
                        f'{litter.mother.father.mother.variety}',
                        f'{litter.mother.father.mother.mother.variety}',
                    ])
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
                        f'Зав.: {litter.mother.breeder} ({litter.mother.breeder.location.city})'
                        '',
                        f'Fem.: {litter.mother.father.mother.full_name}',
                        '',
                    ])
                    writer.writerow([
                        f'Д.р.: {litter.mother.date_of_birth})'
                        '',
                        f'{litter.mother.father.mother.variety}',
                        'нет данных',
                    ])
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

        # 6 мать - отец матери - M O М - О M O М
        if litter.mother.father:
            if litter.mother.father.mother:
                if litter.mother.father.mother.father:
                    writer.writerow([
                        '',
                        f'Male: {litter.mother.father.full_name}'
                        f'Зав.: {litter.mother.father.mother.breeder} '
                        f'({litter.mother.father.mother.breeder.location.city})',
                        f'Male: {litter.mother.father.mother.father.full_name}',
                    ])
                    writer.writerow([
                        '',
                        f'{litter.mother.father.variety}'
                        f'{litter.mother.father.mother.date_of_birth}',
                        f'{litter.mother.father.mother.father.variety}',
                    ])
                    writer.writerow([
                        '',
                        f'Вл.: {litter.mother.father.owner} ({litter.mother.father.owner.location.city})'
                        '',
                        f'Вл.: {litter.mother.father.mother.father.owner} '
                        f'({litter.mother.father.mother.father.owner.location.city})',
                    ])
                else:
                    writer.writerow([
                        '',
                        f'Male: {litter.mother.father.full_name}'
                        f'Зав.: {litter.mother.father.mother.breeder} '
                        f'({litter.mother.father.mother.breeder.location.city})',
                        '',
                    ])
                    writer.writerow([
                        '',
                        f'{litter.mother.father.variety}'
                        f'{litter.mother.father.mother.date_of_birth}',
                        'нет данных',
                    ])
                    writer.writerow([
                        '',
                        f'Вл.: {litter.mother.father.owner} ({litter.mother.father.owner.location.city})'
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
                    writer.writerow([
                        '',
                        f'Зав.: {litter.mother.father.breeder} ({litter.mother.father.breeder.location.city})',
                        f'Male: {litter.mother.father.father.full_name}',
                        f'Fem.: {litter.mother.father.father.mother.full_name}',
                    ])
                    writer.writerow([
                        '',
                        f'Д.р.: {litter.mother.father.date_of_birth}',
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
                    writer.writerow([
                        '',
                        f'Зав.: {litter.mother.father.breeder} ({litter.mother.father.breeder.location.city})',
                        f'Male: {litter.mother.father.father.full_name}',
                        '',
                    ])
                    writer.writerow([
                        '',
                        f'Д.р.: {litter.mother.father.date_of_birth})',
                        f'{litter.mother.father.father.variety}',
                        'нет данных',
                    ])
                    writer.writerow([
                        '',
                        '',
                        f'{litter.mother.father.father.owner} '
                        f'({litter.mother.father.father.owner.location.city})',
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
                writer.writerow([
                    '',
                    '',
                    f'Зав.: {litter.mother.father.father.breeder} '
                    f'({litter.mother.father.father.breeder.location.city})',
                    f'Male: {litter.mother.father.father.father.full_name}',
                ])
                writer.writerow([
                    '',
                    '',
                    f'{litter.mother.father.father.date_of_birth}',
                    f'{litter.mother.father.father.father.variety}',
                ])
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
                    f'{litter.mother.father.father.breeder} '
                    f'({litter.mother.father.father.breeder.location.city})',
                    '',
                ])
                writer.writerow([
                    '',
                    '',
                    f'{litter.mother.father.father.date_of_birth}',
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