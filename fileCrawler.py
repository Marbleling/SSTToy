import requests

f = open('text_sites.txt')
while True:
    l = f.readline()
    if not l: break

    url = l.strip()
    param = url.split('?')[1].split('&')[0].split('=')[1]
    target_url = 'https://gongu.copyright.or.kr/gongu/wrt/cmmn/wrtFileDownload.do?wrtSn=' + param + '&fileSn=1&wrtFileTy=01'
    r = requests.get(target_url)

    open('files/' + param +'.pdf', 'wb').write(r.content)

    print(url)

f.close()