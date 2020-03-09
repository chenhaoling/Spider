# 爬取淘宝网页信息
import requests
import  re

def getHTMLText(url,head):
    try:
        r = requests.get(url,headers = head,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '获取HTML失败'

def parsePage(itl,html):
    try:
        plt = re.findall(r'"view_price":"[\d.]*"',html)
        tlt = re.findall(r'"raw_title":".*?"',html)
        for i in range(len(plt)):
            price = plt[i].split(':')[-1]
            title = tlt[i].split(':')[-1]
            itl.append([price,title])
        return itl
    except:
        print('parsePage Error')

def printGoodsList(itl):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format('序号','价格','商品名称'))
    count = 0
    for g in itl:
        count += 1
        print(tplt.format(count,g[0],g[1]))

def main():
    headers = {
        "user-agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
,       "cookie":
        "isg=BJubqcJ7QUSAo72ziG6VqYO-KPkFcK9yZu0HAI3c1BuNbLpOFUQlwvSuBkxi1wdq; l=dBLoz0unQJuqEAg3BOfBnurza779VCR08kPzaNbMiICPOefNKEafWZqz-O8eCn1VnsiWR372I_V_BuT5jP5-Jxpsw3k_J_b-3dgl.; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTUOan4vVHqJw%3D%3D&tag=8&lng=zh_CN; mt=ci=28_1; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; _nk_=tb257895770; cookie1=W8CE2kROKfX55fBSxCJ3pamUPtqsgW6tRcm5BMXtMWQ%3D; cookie17=UNX4Hdd7s1%2FjCA%3D%3D; cookie2=1b81010770fe104ead84c35f58fca1de; csg=a74f0bba; dnk=tb257895770; enc=I%2FFNng3xwnk4ZoqQNVz65PPvEcsRs43grbiJesWvKkGYNPKrn0iqpjH8entXp48zD0nbiwPePM67G%2FU1Rs%2FSJg%3D%3D; existShop=MTU4Mzc0OTA5OQ%3D%3D; lgc=tb257895770; sg=093; skt=a5e33f75e4f78aa4; t=db1ea1899083617fbc33fe131b8818c9; tfstk=cTg1Bd2B3x3EsfAStmOUu_3lt4a5ZB__TCwn1DGeizGhgbk1M52rNpaCp3CUt; tg=0; tracknick=tb257895770; uc3=lg2=VT5L2FSpMGV7TQ%3D%3D&nk2=F5RHpCwFG2D1N1Y%3D&vt3=F8dBxd7EcIyiyM8cGxA%3D&id2=UNX4Hdd7s1%2FjCA%3D%3D; uc4=nk4=0%40FY4MthL47X1VXzLJN%2Fa2IX1iG1Ofvg%3D%3D&id4=0%40UgJ9%2F0jghOEg6EIkcHgzIrtLt4Fc; unb=3539609679; JSESSIONID=E71CB455D77451D55E34E121C59423DA; alitrackid=login.taobao.com; lastalitrackid=login.taobao.com; _samesite_flag_=true; _tb_token_=f516068e67ef1; v=0; cna=ZePsFuni+TYCAW4TbhfljaHn; _m_h5_tk=515864a799a96b0191581430cb8c32e5_1583747460870; _m_h5_tk_enc=3c384670071ba5d5f9e85c517b8edf99"
    }
    goods = '书包'
    depth = 5
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" +str(44*i)
            html = getHTMLText(url,headers)
            it = parsePage(infoList,html)
            printGoodsList(it)
        except:
            print("打印%d页出错"%i)

main()
