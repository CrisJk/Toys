#coding:utf-8
import urllib.request
import http.cookiejar
import gzip
import requests

def ungzip(data):
    try:        # 尝试解压
        print('准备解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('无需解压')
    return data
filename = "cookie"
cj = http.cookiejar.LWPCookieJar(filename=filename)
def getOpener(head):
    # deal with the Cookies

    # try:
    #     cj.load(ignore_discard=True)
    # except IOError:
    #     print('Cookie未加载！')
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    print(opener.addheaders)
    return opener

web_header = {
'Origin':'https://login.ecnu.edu.cn',#可以不加
'Referer':'https://login.ecnu.edu.cn/srun_portal_pc.php?ac_id=1&', #可以不加
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
opener = getOpener(web_header)
url = 'https://login.ecnu.edu.cn/include/auth_action.php'
# op = opener.open(url);
# data = op.read();
#print(data.decode())

username = '51175100005'
password = 'kuang123456'
postDict = {
        'username': '51175100005',
        'password': 'kuang123456',
        'action':'login',
        'ac_id':1
}

postData = urllib.parse.urlencode(postDict).encode('utf-8')
op = opener.open(url,postData)



data = op.read()
#data = ungzip(data)

print(data.decode('utf-8'))

# url = "http://www.baidu.com" ;
# html = requests.get(url)
# response = html.status_code ;
# print(response) ;
cj.save(ignore_discard=True, ignore_expires=True);