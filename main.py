from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from email_otp import get_email, get_otp


def getEmail_otp(content):
    html = HTMLParser(content)
    try:
        email = html.css_first('.a-spacing-small .a-spacing-micro').text().split('Time Password (OTP) to')[-1].strip().split()[0]
        print(f'OTP has been sent to {email}')
        print('Getting OTP from email...')
        email_id = get_email(email)
        email_otp = get_otp(email_id)
        return email_otp
    except:
        return None
    

def get_number():
    text_path = 'numbers.txt'
    with open(text_path, 'r') as f:
        lines = f.readlines()
        try:
            number = lines.pop(0)
        except Exception as e:
            print('Number not exist on the numbers.txt file!')
    with open(text_path, 'w') as file:
        file.writelines(lines)
    
    return number

def get_urls():
    url_path = 'urls.txt'
    with open(url_path, 'r') as f:
        lines = f.readlines()
        try:
            url = lines.pop(0).strip()
        except Exception as e:
            print('Automation done! No url exist on the urls.txt file!')
            return False
    
    with open(url_path, 'w') as file:
        file.writelines(lines)
    
        if url:
            return url
        else:
            return False


def main(url, country):
    print('Success!')
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto(url)
        change_button = page.locator("a").filter(has_text="Change")
        add_mobile_number_btn = page.get_by_label("Add mobile number")
        page.wait_for_timeout(3000)
        email_otp = getEmail_otp(page.content())
        if email_otp is None:
            print('Invalid link!')
            return None
        else:
            page.locator("#cvf-input-code").fill(email_otp)
            page.get_by_label("Verify").click()
            page.wait_for_load_state('networkidle')
            if '1' in country:
                country_btn = page.get_by_text("Vietnam +")
            elif '2' in country:
                country_btn = page.get_by_text("Mozambique +")
            
            for i in range(1,13):
                page.get_by_label("Select Country Code").locator("span").nth(1).click()
                country_btn.click()
                mobile_num = get_number()
                page.get_by_role("textbox").fill(mobile_num)
                add_mobile_number_btn.click()
                page.wait_for_load_state('networkidle')
                page.wait_for_timeout(2000)
                change_button.click()
                page.wait_for_load_state('networkidle')
                print(f'{i} OTP has been sent!')
            print(f'Job done for this url: {url}')
            page.wait_for_timeout(1000)
            browser.close()
            return None



if __name__ == "__main__":
    country = input('Please enter 1 for Vietnum and 2 for Moz:')
    while True:
        url = get_urls()
        if url:
            main(url, country)
        else:
            break
