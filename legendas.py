#import httplib, urllib
#params = urllib.urlencode(dict(txtLogin="mbcastro", txtSenha="syntricks"))
#headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
#conn = httplib.HTTPConnection("legendas.tv")
#conn.request("POST", "/login_verificar.php", params, headers)
#response = conn.getresponse()
#print response.status, response.reason
#data = response.read()
#print data
#conn.close()


from httplib2 import Http
import urllib
from urllib import urlencode

h = Http()
data = dict(txtLogin="mbcastro", txtSenha="syntricks")
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

resp, content = h.request("http://legendas.tv/login_verificar.php", method="POST", body=urlencode(data), headers=headers)

#print resp
#print content

data = ["txtLegenda=big bang theory", "selTipo=1", "int_idioma=1"]
print urllib.quote(data, '')
resp, content = h.request("http://legendas.tv/index.php?opcao=buscarlegenda", "POST", urlencode(data),headers)



#print resp
#print content
