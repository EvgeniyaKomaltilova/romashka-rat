def get_pedigree_pdf(litter, pdf):

    pdf.setFont("Verdana", 11)

    pdf.drawString(100, 820, 'Питомник Декоративных Крыс "Ромашка", г. Санкт-Петербург')
    pdf.drawString(200, 800, 'Родословная декоративной крысы')

    pdf.setFont("Verdana", 8)
    pdf.drawString(10, 770, f'Литера "{litter.name}" {litter.prefix}')
    pdf.drawString(160, 770, f'Дата рождения: {litter.date_of_birth}')
    pdf.drawString(310, 770, f'Заводчик: {litter.breeder}')
    pdf.drawString(460, 770, f'№ родословной: {litter.number}')

    pdf.setFont("Verdana", 7)
    pdf.drawString(10, 750, 'Родители/Parents')
    pdf.drawString(160, 750, 'Прародители/Grandparents')
    pdf.setFont("Verdana", 6)
    pdf.drawString(310, 750, 'Пра-прародители/Grand-grandparents')
    pdf.setFont("Verdana", 5)
    pdf.drawString(460, 750, 'Пра-пра-прародители/Grand-grand-grandparents')

    pdf.setFont("Verdana", 6)
    # мать
    if litter.mother:
        pdf.drawString(10, 730, f'Fem.: {litter.mother.name} {litter.mother.prefix}')
        pdf.drawString(10, 720, f'{litter.mother.variety}')
        pdf.drawString(10, 710, f'Вл.: {litter.mother.owner}'
                                f' ({litter.mother.owner.location.city})')
        pdf.drawString(10, 700, f'Зав.: {litter.mother.breeder}'
                                f' ({litter.mother.breeder.location.city})')
        pdf.drawString(10, 690, f'Д.р.: {litter.mother.date_of_birth}')

        # мать матери (м.м.)
        if litter.mother.mother:
            pdf.drawString(160, 730, f'Fem.: {litter.mother.mother.name}'
                                     f' {litter.mother.mother.prefix}')
            pdf.drawString(160, 720, f'{litter.mother.mother.variety}')
            pdf.drawString(160, 710, f'Вл.: {litter.mother.mother.owner}'
                                     f' ({litter.mother.mother.owner.location.city})')
            pdf.drawString(160, 700, f'Зав.: {litter.mother.mother.breeder}'
                                     f' ({litter.mother.mother.breeder.location.city})')
            pdf.drawString(160, 690, f'Д.р.: {litter.mother.mother.date_of_birth}')
            # м.м.м
            if litter.mother.mother.mother:
                pdf.drawString(310, 730, f'Fem.: {litter.mother.mother.mother.name}'
                                         f' {litter.mother.mother.mother.prefix}')
                pdf.drawString(310, 720, f'{litter.mother.mother.mother.variety}')
                pdf.drawString(310, 710, f'Вл.: {litter.mother.mother.mother.owner}'
                                         f' ({litter.mother.mother.mother.owner.location.city})')
                pdf.drawString(310, 700,
                               f'Зав.: {litter.mother.mother.mother.breeder}'
                               f' ({litter.mother.mother.mother.breeder.location.city})')
                pdf.drawString(310, 690, f'Д.р.: {litter.mother.mother.mother.date_of_birth}')
                # м.м.м.м.
                if litter.mother.mother.mother.mother:
                    pdf.drawString(460, 730,
                                   f'Fem.: {litter.mother.mother.mother.mother.name}'
                                   f' {litter.mother.mother.mother.mother.prefix}')
                    pdf.drawString(460, 720, f'{litter.mother.mother.mother.mother.variety}')
                    pdf.drawString(460, 710, f'Вл.: {litter.mother.mother.mother.mother.owner}'
                                             f' ({litter.mother.mother.mother.mother.owner.location.city})')
                # о.м.м.м.
                if litter.mother.mother.mother.father:
                    pdf.drawString(460, 700,
                                   f'Male: {litter.mother.mother.mother.father.name}'
                                   f' {litter.mother.mother.mother.father.prefix}')
                    pdf.drawString(460, 690, f'{litter.mother.mother.mother.father.variety}')
                    pdf.drawString(460, 680, f'Вл.: {litter.mother.mother.mother.father.owner}'
                                             f' ({litter.mother.mother.mother.father.owner.location.city})')
            # о.м.м.
            if litter.mother.mother.father:
                pdf.drawString(310, 670, f'Male: {litter.mother.mother.mother.name}'
                                         f' {litter.mother.mother.mother.prefix}')
                pdf.drawString(310, 660, f'{litter.mother.mother.mother.variety}')
                pdf.drawString(310, 650, f'Вл.: {litter.mother.mother.mother.owner}'
                                         f' ({litter.mother.mother.mother.owner.location.city})')
                pdf.drawString(310, 640,
                               f'Зав.: {litter.mother.mother.mother.breeder}'
                               f' ({litter.mother.mother.mother.breeder.location.city})')
                pdf.drawString(310, 630, f'Д.р.: {litter.mother.mother.mother.date_of_birth}')
                # м.о.м.м.
                if litter.mother.mother.father.mother:
                    pdf.drawString(460, 670,
                                   f'Fem.: {litter.mother.mother.father.mother.name}'
                                   f' {litter.mother.mother.father.mother.prefix}')
                    pdf.drawString(460, 660, f'{litter.mother.mother.father.mother.variety}')
                    pdf.drawString(460, 650, f'Вл.: {litter.mother.mother.father.mother.owner}'
                                             f' ({litter.mother.mother.father.mother.owner.location.city})')
                # о.о.м.м.
                if litter.mother.mother.father.father:
                    pdf.drawString(460, 640,
                                   f'Male: {litter.mother.mother.father.father.name}'
                                   f' {litter.mother.mother.father.father.prefix}')
                    pdf.drawString(460, 630, f'{litter.mother.mother.father.father.variety}')
                    pdf.drawString(460, 620, f'Вл.: {litter.mother.mother.father.father.owner}'
                                             f' ({litter.mother.mother.father.father.owner.location.city})')

        # отец матери (о.м.)
        if litter.mother.father:
            pdf.drawString(160, 610, f'Male: {litter.mother.father.name}'
                                     f' {litter.mother.father.prefix}')
            pdf.drawString(160, 600, f'{litter.mother.father.variety}')
            pdf.drawString(160, 590, f'Вл.: {litter.mother.father.owner}'
                                     f' ({litter.mother.father.owner.location.city})')
            pdf.drawString(160, 580, f'Зав.: {litter.mother.father.breeder}'
                                     f' ({litter.mother.father.breeder.location.city})')
            pdf.drawString(160, 570, f'Д.р.: {litter.mother.father.date_of_birth}')
            # м.о.м
            if litter.mother.father.mother:
                pdf.drawString(310, 610, f'Fem.: {litter.mother.father.mother.name}'
                                         f' {litter.mother.father.mother.prefix}')
                pdf.drawString(310, 600, f'{litter.mother.father.mother.variety}')
                pdf.drawString(310, 590, f'Вл.: {litter.mother.father.mother.owner}'
                                         f' ({litter.mother.father.mother.owner.location.city})')
                pdf.drawString(310, 580,
                               f'Зав.: {litter.mother.father.mother.breeder}'
                               f' ({litter.mother.father.mother.breeder.location.city})')
                pdf.drawString(310, 570, f'Д.р.: {litter.mother.father.mother.date_of_birth}')
                # м.м.o.м.
                if litter.mother.father.mother.mother:
                    pdf.drawString(460, 610,
                                   f'Fem.: {litter.mother.father.mother.mother.name}'
                                   f' {litter.mother.father.mother.mother.prefix}')
                    pdf.drawString(460, 600, f'{litter.mother.father.mother.mother.variety}')
                    pdf.drawString(460, 590, f'Вл.: {litter.mother.father.mother.mother.owner}'
                                             f' ({litter.mother.father.mother.mother.owner.location.city})')
                # о.м.o.м.
                if litter.mother.father.mother.father:
                    pdf.drawString(460, 580,
                                   f'Male: {litter.mother.father.mother.father.name}'
                                   f' {litter.mother.father.mother.father.prefix}')
                    pdf.drawString(460, 570, f'{litter.mother.father.mother.father.variety}')
                    pdf.drawString(460, 560, f'Вл.: {litter.mother.father.mother.father.owner}'
                                             f' ({litter.mother.father.mother.father.owner.location.city})')
            # о.o.м.
            if litter.mother.father.father:
                pdf.drawString(310, 550, f'Male: {litter.mother.father.father.name}'
                                         f' {litter.mother.father.father.prefix}')
                pdf.drawString(310, 540, f'{litter.mother.father.father.variety}')
                pdf.drawString(310, 530, f'Вл.: {litter.mother.father.father.owner}'
                                         f' ({litter.mother.father.father.owner.location.city})')
                pdf.drawString(310, 520,
                               f'Зав.: {litter.mother.father.father.breeder}'
                               f' ({litter.mother.father.father.breeder.location.city})')
                pdf.drawString(310, 510, f'Д.р.: {litter.mother.father.father.date_of_birth}')
                # м.о.o.м.
                if litter.mother.father.father.mother:
                    pdf.drawString(460, 550,
                                   f'Fem.: {litter.mother.father.father.mother.name}'
                                   f' {litter.mother.father.father.mother.prefix}')
                    pdf.drawString(460, 540, f'{litter.mother.father.father.mother.variety}')
                    pdf.drawString(460, 530, f'Вл.: {litter.mother.father.father.mother.owner}'
                                             f' ({litter.mother.father.father.mother.owner.location.city})')
                # о.о.o.м.
                if litter.mother.father.father.father:
                    pdf.drawString(460, 520,
                                   f'Male: {litter.mother.father.father.father.name}'
                                   f' {litter.mother.father.father.father.prefix}')
                    pdf.drawString(460, 510, f'{litter.mother.father.father.father.variety}')
                    pdf.drawString(460, 500, f'Вл.: {litter.mother.father.father.father.owner}'
                                             f' ({litter.mother.father.father.father.owner.location.city})')





    if litter.father:
        pdf.drawString(10, 340, f'Male: {litter.father.name} {litter.father.prefix}')
        pdf.drawString(10, 330, f'{litter.father.variety}')
        pdf.drawString(10, 320, f'Вл.: {litter.father.owner}')
        pdf.drawString(10, 310, f'Зав.: {litter.father.breeder}')
        pdf.drawString(10, 300, f'Д.р.: {litter.father.date_of_birth}')


    pdf.showPage()
    pdf.save()
