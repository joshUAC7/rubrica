from rest_framework.views import APIView
from dj_rest_auth.views import AllowAny
from django.http import FileResponse, HttpRequest, HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from tempfile import NamedTemporaryFile
from docxtpl import DocxTemplate
from drfauth.models import Document


from django.contrib.staticfiles.storage import staticfiles_storage

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open("staticfiles/"+filename, 'wb') as file:
        file.write(data)
class PdfView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        one = Document.objects.get(id=1)
        write_file(one.Doc_Content,one.FileName+"."+one.Extension)
        file_path = staticfiles_storage.path(one.FileName+"."+one.Extension)
        print(file_path)
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Instrumento de Evaluacion.pdf"'
            return response

class ReporteView(APIView):
    permission_classes=[AllowAny]
    def post(self,request:Request):
        one = Document.objects.get(id=2)
        write_file(one.Doc_Content,one.FileName+"."+one.Extension)
        file_path = staticfiles_storage.path(one.FileName+"."+one.Extension)
        template = DocxTemplate(file_path)
        contextVars = request.data.copy()
        template.render(contextVars)
        template.save("staticfiles/informe"+"."+one.Extension)
        file_path = staticfiles_storage.path("informe" +"."+one.Extension)
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Informe.pdf"'
            return response
        # return JsonResponse(request.data,safe=False)
       

 
