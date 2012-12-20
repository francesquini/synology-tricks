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
import html5lib
from html5lib import treebuilders, treewalkers, serializer
from html5lib.filters import sanitizer


h = Http()
data = dict(txtLogin="mbcastro", txtSenha="syntricks")
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
resp, content = h.request("http://legendas.tv/login_verificar.php", "POST", urllib.urlencode(data), headers)

#Assert login successful


fields =["opcao", "txtLegenda", "selTipo", "int_idioma"]
values = map(lambda a: urllib.quote(a, ''), ["buscarlegenda", "big bang theory", "1", "1"])
encodedData = reduce (
    lambda a, b: a + '&' + b, 
    [field + '=' + value for (field, value) in zip(fields, values)])
resp, content = h.request("http://legendas.tv/index.php", "POST", encodedData, headers)

#Assert response successful

parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))
dom_tree = parser.parse(content)
walker = treewalkers.getTreeWalker("dom")
stream = walker(dom_tree)
serializer = serializer.htmlserializer.HTMLSerializer(omit_optional_tags=False)
output_generator = serializer.serialize(stream)

for item in output_generator:
    print item
