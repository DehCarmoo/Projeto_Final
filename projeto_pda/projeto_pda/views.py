from django.http import HttpResponse # importando a biblioteca HttpResponse
import datetime
from django.template import Template, Context 


def index(request):
    documentoExterno = open("C:/Users/Nataly/Documents/projeto.final/projeto_pda/projeto_pda/Projeto/index.html")
    pagina = Template(documentoExterno.read())
    documentoExterno.close()
    cxt = Context()
    documento = pagina.render(cxt)
    return HttpResponse(documento)

def livros(request):
    documentoExterno = open("C:/Users/Nataly/Documents/projeto.final/projeto_pda/projeto_pda/Projeto/livros.html")
    pagina = Template(documentoExterno.read())
    documentoExterno.close()
    cxt = Context()
    documento = pagina.render(cxt)
    return HttpResponse(documento)

def sites(request):
    documentoExterno = open("C:/Users/Nataly/Documents/projeto.final/projeto_pda/projeto_pda/Projeto/sites.html")
    pagina = Template(documentoExterno.read())
    documentoExterno.close()
    cxt = Context()
    documento = pagina.render(cxt)
    return HttpResponse(documento)