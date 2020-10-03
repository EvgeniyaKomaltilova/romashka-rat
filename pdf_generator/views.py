from io import BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from rattery.models.Litter import Litter


def litter_pedigree_view(request, data):
    """Генерация PDF родословной помета"""
    pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))

    litter = Litter.objects.get(id=data)

    response = HttpResponse(content_type='application/pdf')

    # файл для скачивания
    # response['Content-Disposition'] = 'attachment; filename="rat_pedigree.pdf"'

    # файл для чтения
    response['Content-Disposition'] = 'filename="rat_pedigree.pdf"'

    buffer = BytesIO()

    pdf = canvas.Canvas(response)
    pdf.setFont("Verdana", 8)
    pdf.drawString(10, 820, f'Имя: {litter.name} {litter.prefix}')
    pdf.drawString(10, 810, f'Дата рождения: {litter.date_of_birth}')
    if litter.father:
        pdf.drawString(10, 780, f'Отец: {litter.father.name} {litter.father.prefix} ({litter.father.variety})')
    if litter.mother:
        pdf.drawString(10, 770, f'Мать: {litter.mother.name} {litter.mother.prefix} ({litter.mother.variety})')
    pdf.showPage()
    pdf.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response