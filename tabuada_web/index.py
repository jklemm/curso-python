from bottle import route, run, view, request

from tabuada_web.tabuada import tabuada


@route('/')
@view('form_template')
def form():
    return {}


@route('/resultado', method='POST')
@view('resultado_template')
def resultado():
    numero_tabuada = int(request.forms.get('numero_tabuada'))
    
    resultados = tabuada(numero_tabuada)
    
    return dict(resultados=resultados)


run(host='localhost', port=8080)
