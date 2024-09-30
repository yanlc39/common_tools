import requests

from lxml import etree

cookies = {
    'JSESSIONID': '0000zhmzLnp7or66gg2FMbCEFOK:-1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://srh.bankofchina.com',
    'Pragma': 'no-cache',
    'Referer': 'https://srh.bankofchina.com/search/whpj/search_cn.jsp',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

body_data = {
  'erectDate': '',
  'nothing': '',
  'pjname': '港币',
  'head': 'head_620.js',
  'bottom': 'bottom_591.js'
}

def get_HTML_doc(exchange):
    body_data['pjname'] = exchange
    response = requests.post('https://srh.bankofchina.com/search/whpj/search_cn.jsp', headers=headers, cookies=cookies,
                             data=body_data)
    return response.text

def parse_HTML_doc(html_body):
    root = etree.HTML(html_body)
    children = root.xpath('/html//div[@class="BOC_main publish"]')[0]
    print(children.get('class'))
    trs = children.xpath('table')[0]
    trs = trs.findall('tr')
    ths = trs[0].findall('th')
    del(trs[0])
    for th in ths:
        print(th.text.strip(), end='\t')
    print()
    for tr in trs:
        tds = tr.findall('td')
        for td in tds:
            print(td.text.strip(), end='\t')
        print()


if __name__ == '__main__':
    html_doc = get_HTML_doc('港币')
    parse_HTML_doc(html_doc)