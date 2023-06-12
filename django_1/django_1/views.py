from django.http import HttpResponse
import datetime
from django.template import Template, Context 


 




def Projeto_Final (request): 
    documentoExterno = open("C:/Users/Grta/pda/Projeto_Final/index.html")
    pagina =Template(documentoExterno.read())
    documentoExterno.close()
    ctx = Context()
    documento = pagina.render(ctx)
    return HttpResponse(documento)


def Projeto_Final (request): 
    documentoExterno = open("C:/Users/Grta/pda/Projeto_Final/inicio.html")
    pagina =Template(documentoExterno.read())
    documentoExterno.close()




def Projeto_Final (request): 
    documentoExterno = open("C:/Users/Grta/pda/Projeto_Final/contato.html")
    pagina =Template(documentoExterno.read())
    documentoExterno.close()




def Projeto_Final (request): 
    documentoExterno = open("C:/Users/Grta/pda/Projeto_Final/livros.html")
    pagina =Template(documentoExterno.read())
    documentoExterno.close()




def Projeto_Final (request): 
    documentoExterno = open("C:/Users/Grta/pda/Projeto_Final/sites.html")
    pagina =Template(documentoExterno.read())
    documentoExterno.close()