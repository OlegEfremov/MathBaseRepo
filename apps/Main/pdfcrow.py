import pdfcrowd
from django.http import HttpResponse
from django.template.loader import get_template


# Конверсия кода рисунка
from django.urls import reverse

from LBBASE_v_0_40.settings import PROJECT_ROOT


class Pdfcrow:

# работает но не выводит рисунки а таблицы выводит без линий
    @staticmethod
    def render(request, path: str, params: dict):
        template = get_template(path)
        html = template.render(params, request)

        try:
            # create the API client instance
            client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

            # set HTTP response headers
            response = HttpResponse(content_type='application/pdf')
            response['Cache-Control'] = 'max-age=0'
            response['Accept-Ranges'] = 'none'
            response['Content-Disposition'] = 'attachment; filename="result.pdf"'

            # run the conversion and write the result into the output stream
            client.convertStringToStream(html, response)
            return response
        except pdfcrowd.Error as why:
            # send the error in the HTTP response
            return HttpResponse(why.getMessage(),
                                status=why.getCode(),
                                content_type='text/plain')

# не работает ошибка navigate filed. Обычный рендеринг страницы на экран (не пдф) работает полностью
    @staticmethod
    def convert(request):
        try:
            # create the API client instance
            client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

            # set HTTP response headers
            response = HttpResponse(content_type='application/pdf')
            response['Cache-Control'] = 'max-age=0'
            response['Accept-Ranges'] = 'none'
            response['Content-Disposition'] = 'attachment; filename="result.pdf"'

            # run the conversion and write the result into the output stream
            client.convertUrlToStream(request.build_absolute_uri(reverse('show_tasks_for_pdf')), response)
            return response
        except pdfcrowd.Error as why:
            # send the error in the HTTP response
            return HttpResponse(why.getMessage(),
                                status=why.getCode(),
                                content_type='text/plain')