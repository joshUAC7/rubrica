from rest_framework.views import APIView
from dj_rest_auth.views import AllowAny
from django.http import FileResponse, HttpRequest, HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from tempfile import NamedTemporaryFile
from docxtpl import DocxTemplate


from django.contrib.staticfiles.storage import staticfiles_storage
class PdfView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        print(staticfiles_storage.path('pdfs/Instrumento.pdf'))

        file_path = staticfiles_storage.path('pdfs/Instrumento.pdf')
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="example.pdf"'
            return response

class ReporteView(APIView):
    permission_classes=[AllowAny]
    def post(self,request:Request):
        file_path = staticfiles_storage.path('pdfs/anexo.docx')
        print(request.data)
        template = DocxTemplate(file_path)
        contextVars = request.data.copy()
        template.render(contextVars)
        template.save("staticfiles/pdfs/informe.docx")
        file_path = staticfiles_storage.path('pdfs/informe.pdf')
        return JsonResponse(request.data,safe=False)
       

 
