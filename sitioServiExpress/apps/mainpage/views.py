from django.core.checks import messages
from django.shortcuts import redirect, render
from django.db import connection,models
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from io import BytesIO

from django.http import HttpResponse
from django.views.generic import View
from apps.reserva.models import ReservaServicio
from apps.Boleta.models import boletaFactura
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, MO






# Create your views here.


def index(request):
    return render(request, 'user_portal.html')


def services(request):
    return render(request, 'services.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def estadisticas(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT sum(case when activa='1' then 1 else 0 end) as Activas,sum(case when activa='0' then 1 else 0 end) as Anuladas FROM serviexpress.boleta_boletafactura where extract(year from fecha_documento)='2021' group by extract(month from fecha_documento) order by extract(month from fecha_documento);")
        rawData = cursor.fetchall()
        activoTxt=''
        anuladoTxt=''
        for i in rawData:
            activoTxt+=str(i[0])+','
            anuladoTxt+=str(i[1])+','
        ms= []
        base = date.today()
        for x in range(0, base.month):

            ms.append(base + relativedelta(month=x))
        contexto = {
            'activo' : activoTxt,
            'anulado' : anuladoTxt,
            'options' : ms
            }

    if request.method == 'POST':
        monthFilter = request.POST.get("month")
        return redirect("create_report", monthFilter)
    
    return render(request, 'Informe/estadisticas.html',contexto)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        month = int(kwargs['monthFilter'])
        MesAnterior = month-1
        mesActual = datetime.strptime(str(month),'%m')
        print("mes actuaaaaal", mesActual)
        reserva = ReservaServicio.objects.filter(fecha_reserva__month = month)
        venta = boletaFactura.objects.filter(fecha_documento__month = month)
        ventaMA = boletaFactura.objects.filter(fecha_documento__month = MesAnterior)
        ventasAnuladas = boletaFactura.objects.filter(fecha_documento__month = month, activa = False)
        
        
        cantidadReserva = len(reserva)
        cantidadVenta = len(venta)
        cantidadVentaMA = len(ventaMA)
        try: 
            porcentajeVenta = round((cantidadVenta/cantidadVentaMA)*100,1)
        except:
            porcentajeVenta = round((cantidadVenta/1)*100,1)
        cantidadVA = len(ventasAnuladas)



        template = get_template('reportpdf.html')
        

        context = {
            "mesActual": mesActual,
            "cantidadReserva": cantidadReserva,
            "cantidadVenta" : cantidadVenta,
            "cantidadVentaMA": cantidadVentaMA,
            "porcentajeVenta": porcentajeVenta,
            "cantidadVA": cantidadVA,   
        }
        html = template.render(context)
        pdf = render_to_pdf('reportpdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Informe_ventas.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")