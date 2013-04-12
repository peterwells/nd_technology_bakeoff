from django.template import loader
from django.template.context import RequestContext
from django.http import HttpResponse

from models import STVTERM

def academic_terms(request):
    terms = STVTERM.objects.raw('SELECT stvterm_code, stvterm_desc FROM STVTERM')

    template = loader.get_template('oracleresults.html')
    context = RequestContext(
        request,
        {'stvterm_terms': terms})

    return HttpResponse(template.render(context))