#
# Класс-посредник преобразующий самописный код рисунка в html тег src
#
from django.utils.deprecation import MiddlewareMixin
from apps.Main.pdfcrow import img_to_html


class CompileImageCode(MiddlewareMixin):

    def process_response(self, request, response):

        if request.path_info.find('show_tasks_for_pdf') >= 0:
#            ret = response.content.decode("UTF-8")
            ret = response.content
            ret = img_to_html(ret)
            response.content = ret

        return response
