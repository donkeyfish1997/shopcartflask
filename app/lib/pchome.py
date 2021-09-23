# %%
from bs4 import BeautifulSoup
import requests
import json
import re
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-tw",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
    "Connection": "keep-alive",
    "X-Requested-With": "XMLHttpRequest"
}
session = requests.session()


def pchomeSearch(keword, page):

    res = session.get(
        f"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={keword}&page={page}&sort=sale/dc", headers=headers)

    data = json.loads(res.text)  # ["prods"]
    return data


def pchomeitem(id):
    info = {}
    url_info = f"https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{id}&fields=Id,Name,Price,Pic,Qty&_callback=jsonp_prod&1632276900?_callback=jsonp_prod"
    url_kword = f"https://ecapi-pchome.cdn.hinet.net/cdn/ecshop/prodapi/v2/prod/{id}/desc&fields=Id,Liability,Slogan&_callback=jsonp_desc?_callback=jsonp_desc"
    url_intro = f"https://ecapi-pchome.cdn.hinet.net/cdn/ecshop/prodapi/v2/prod/{id}/intro&fields=Pic,Intro&_callback=jsonp_intro?_callback=jsonp_intro"

    res_info = session.get(url_info, headers=headers).text
    dic_info = ana_json(res_info)
    info['name'] = dic_info['Name']
    info['price'] = dic_info['Price']['P']
    info['pic'] = dic_info['Pic']['B']
    info['qty'] = dic_info['Qty']

    res_kword = session.get(url_kword, headers=headers).text
    dic_kword = ana_json(res_kword)
    info['id'] = dic_kword['Id']
    info['liability'] = dic_kword['Liability']
    info['slogan'] = dic_kword['Slogan']

    res_intro = session.get(url_intro, headers=headers).text
    dic_intro = ana_json(res_intro)
    info['intro'] = dic_intro
    return info


def ana_json(info):
    spl_info = re.findall(
        r"\"\:(.+?)\}\);\}catch\(e\)\{if\(window.console\)\{console.log\(e\);\}\}", info)[0]
    dic_info = json.loads(spl_info)

    return dic_info


# %%
if __name__ == "__main__":
    id = 'DYAJ2N-1900BSH2M'
    a = (pchomeitem(id))
    a =a['slogan']
    # print(pchomeSearch('apple',1))

# %%
soup = BeautifulSoup(a, 'html.parser')

# %%
from bs4 import BeautifulSoup


# %%

# %%
