from io import BytesIO

from reportlab import rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from website.models.Rat import Rat


def some_view(request, data):
    pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))

    rat = Rat.objects.get(id=data)

    response = HttpResponse(content_type='application/pdf')
    # файл для скачивания
    # response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    # файл для чтения
    response['Content-Disposition'] = 'filename="somefilename.pdf"'

    buffer = BytesIO()

    pdf = canvas.Canvas(response)
    pdf.setFont("Verdana", 8)
    pdf.drawString(10, 820, f'Имя: {rat.name} {rat.prefix}')
    pdf.drawString(10, 810, f'Тип: {rat.variety}')
    pdf.drawString(10, 800, f'Дата рождения: {rat.date_of_birth}')
    pdf.drawString(10, 780, f'Отец: {rat.father.name} {rat.father.prefix} ({rat.father.variety})')
    pdf.drawString(10, 770, f'Мать: {rat.mother.name} {rat.mother.prefix} ({rat.mother.variety})')
    pdf.showPage()
    pdf.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
