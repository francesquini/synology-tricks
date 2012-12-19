from httplib2 import Http
from urllib import urlencode
h = Http()
data = {'txtLogin': "mbcastro", 'txtSenha': "syntricks", 'entrar.x':"20", 'entrar.y': "10"}
resp, content = h.request("http://legendas.tv/login_verificar.php", "POST", urlencode(data))

print resp
print content

#data = dict(txtLegenda="big bang theory", selTipo="1", int_idioma="1")
#resp, content = h.request("http://legendas.tv/index.php?opcao=buscarlegenda", "POST", urlencode(data))

#print resp
#print content
