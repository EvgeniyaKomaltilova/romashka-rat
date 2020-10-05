from io import BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from rattery.models.Litter import Litter
from romashka.services.pdf import get_pedigree_pdf


def litter_pedigree_view(request, data):
    """Генерация PDF родословной помета"""
    pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))

    litter = Litter.objects.get(id=data)

    response = HttpResponse(content_type='application/pdf')

    # файл для скачивания
    # response['Content-Disposition'] = 'attachment; filename="pedigree.pdf"'

    # файл для чтения
    response['Content-Disposition'] = 'filename="pedigree"'

    buffer = BytesIO()
    pdf = canvas.Canvas(response)

    get_pedigree_pdf(litter, pdf)

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
