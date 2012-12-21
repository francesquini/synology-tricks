import requests
import re
import os
import sys

#login and password
login = 'yourloginhere'
password = 'yourpasswordhere' 

#input parameter: example "big bang theory S03 E05"
query = sys.argv[1]

#set HTML headers
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

#login on legendas.tv
payload_login = {'txtLogin': login, 'txtSenha': password}
request_login = requests.post("http://legendas.tv/login_verificar.php", data=payload_login, headers=headers)

#search for subtitles using 'query'
payload_search = {'opcao': 'buscarlegenda', 'txtLegenda': query, 'selTipo': '1', 'int_idioma': '1'}
request_search = requests.post("http://legendas.tv/index.php", data=payload_search, headers=headers, cookies=request_login.cookies)

#parse results
expression = r"span onmouseover=\"this\.T_OPACITY=95; this\.T_WIDTH=400; return escape\(gpop\('.+?','.+?','.+?'.+?javascript:abredown\('(.+?)'\).+?Release: \<span class=\"brls\"\>(.+?)\</span\>"
result = re.findall(expression, request_search.text.replace('\n', ' ').replace('\r', ' '))

#for each result on the first page, download the corresponding subtitles and unzip/unrar them
#todo: consider other pages?
for code, name in result:
    request_subtitle = requests.get("http://legendas.tv/info.php?d=" + code + "&c=1", headers=headers, cookies=request_login.cookies, allow_redirects=False)
    filename = request_subtitle.headers['location']

    request_file = requests.get("http://legendas.tv/" + filename, headers=headers, cookies=request_login.cookies, stream=True, allow_redirects=False)
 
    filename = "subtitles/" + filename[filename.rfind('/')+1:]
    f = open(filename, 'wb')
    f.write(request_file.raw.read())
    f.close()
    
    file_type = filename[filename.rfind('.')+1:].lower()
    if file_type == "zip":
        os.system('unzip -o -qq ' + filename + " -d subtitles/")
    else:
        if file_type == "rar":
            os.system('unrar e -y -inul ' + filename + " subtitles/")
        else:
            print "error: can't recognize file extention: " + file_type

