import requests
from selectolax.parser import HTMLParser

def get_email(email):
    cookies = {
        'cookie_csrf_token': '4c86024f0466d89f95a4b68db6b2f477',
        'cookie_keepalive_insert': '1',
        'cookie_last_page_recv': '0',
        '_ga': 'GA1.1.687010971.1707256563',
        'cookie_timezone': 'Asia%2FDhaka',
        'cookie_last_page_send': '0',
        'cookie_failedSlot': '',
        '__gads': 'ID=d76786fb677a234f:T=1707256564:RT=1707257606:S=ALNI_MY5JAk1-8OZ67Gb9eac5p6PBpmuLg',
        '__gpi': 'UID=00000cfac35ae5f6:T=1707256564:RT=1707257606:S=ALNI_MYFnLBVakXn_Z1gWY9TPCxrdHe7og',
        '__eoi': 'ID=593807cf68f69a46:T=1707256564:RT=1707257606:S=AA-Afjam_SHAzcjaSKmPYIn5Az7v',
        'cookie_sessionhash': 'SHASH%3A4f0cf3c697c592d91cd6f9bf4fa0f833',
        'cookie_last_page_addrlist': '0',
        '_ga_HMG13DJCGJ': 'GS1.1.1707256563.1.1.1707257924.0.0.0',
    }

    headers = {
        'authority': 'm.kuku.lu',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'cookie_csrf_token=4c86024f0466d89f95a4b68db6b2f477; cookie_keepalive_insert=1; cookie_last_page_recv=0; _ga=GA1.1.687010971.1707256563; cookie_timezone=Asia%2FDhaka; cookie_last_page_send=0; cookie_failedSlot=; __gads=ID=d76786fb677a234f:T=1707256564:RT=1707257606:S=ALNI_MY5JAk1-8OZ67Gb9eac5p6PBpmuLg; __gpi=UID=00000cfac35ae5f6:T=1707256564:RT=1707257606:S=ALNI_MYFnLBVakXn_Z1gWY9TPCxrdHe7og; __eoi=ID=593807cf68f69a46:T=1707256564:RT=1707257606:S=AA-Afjam_SHAzcjaSKmPYIn5Az7v; cookie_sessionhash=SHASH%3A4f0cf3c697c592d91cd6f9bf4fa0f833; cookie_last_page_addrlist=0; _ga_HMG13DJCGJ=GS1.1.1707256563.1.1.1707257924.0.0.0',
        'referer': 'https://m.kuku.lu/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.get(
        f'https://m.kuku.lu/recv._ajax.php?&page=0&q={email}&nopost=1&csrf_token_check=4c86024f0466d89f95a4b68db6b2f477&csrf_subtoken_check=b5e29a12276f07e90b737f90f65b7bff&_=1707257924030',
        cookies=cookies,
        headers=headers,
    )
    html = HTMLParser(response.text)

    id_name = html.css_first('div.mailbodybox').attributes['id'].split('_')[-1]
    return id_name

def get_otp(id_name):
    cookies = {
        'cookie_csrf_token': '4c86024f0466d89f95a4b68db6b2f477',
        'cookie_keepalive_insert': '1',
        'cookie_last_page_recv': '0',
        '_ga': 'GA1.1.687010971.1707256563',
        'cookie_timezone': 'Asia%2FDhaka',
        'cookie_last_page_send': '0',
        'cookie_failedSlot': '',
        '__gads': 'ID=d76786fb677a234f:T=1707256564:RT=1707257606:S=ALNI_MY5JAk1-8OZ67Gb9eac5p6PBpmuLg',
        '__gpi': 'UID=00000cfac35ae5f6:T=1707256564:RT=1707257606:S=ALNI_MYFnLBVakXn_Z1gWY9TPCxrdHe7og',
        '__eoi': 'ID=593807cf68f69a46:T=1707256564:RT=1707257606:S=AA-Afjam_SHAzcjaSKmPYIn5Az7v',
        'cookie_sessionhash': 'SHASH%3A4f0cf3c697c592d91cd6f9bf4fa0f833',
        'cookie_last_page_addrlist': '0',
        'cookie_last_q': 'bidsunfoe%40airsmtp.com',
        '_ga_HMG13DJCGJ': 'GS1.1.1707256563.1.1.1707258394.0.0.0',
    }

    headers = {
        'authority': 'm.kuku.lu',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'cookie_csrf_token=4c86024f0466d89f95a4b68db6b2f477; cookie_keepalive_insert=1; cookie_last_page_recv=0; _ga=GA1.1.687010971.1707256563; cookie_timezone=Asia%2FDhaka; cookie_last_page_send=0; cookie_failedSlot=; __gads=ID=d76786fb677a234f:T=1707256564:RT=1707257606:S=ALNI_MY5JAk1-8OZ67Gb9eac5p6PBpmuLg; __gpi=UID=00000cfac35ae5f6:T=1707256564:RT=1707257606:S=ALNI_MYFnLBVakXn_Z1gWY9TPCxrdHe7og; __eoi=ID=593807cf68f69a46:T=1707256564:RT=1707257606:S=AA-Afjam_SHAzcjaSKmPYIn5Az7v; cookie_sessionhash=SHASH%3A4f0cf3c697c592d91cd6f9bf4fa0f833; cookie_last_page_addrlist=0; cookie_last_q=bidsunfoe%40airsmtp.com; _ga_HMG13DJCGJ=GS1.1.1707256563.1.1.1707258394.0.0.0',
        'origin': 'https://m.kuku.lu',
        'referer': 'https://m.kuku.lu/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    data = {
        'num': id_name,
        'key': '139adb61017a091bdce89e3a8ed65829',
        'noscroll': '1',
    }

    response = requests.post('https://m.kuku.lu/smphone.app.recv.view.php', cookies=cookies, headers=headers, data=data)
    
    otp = HTMLParser(response.text).css_first('p.otp').text(strip=True)
    print(f'Your email OTP is {otp}')
    return otp
