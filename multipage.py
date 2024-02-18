import asyncio
from playwright.async_api import async_playwright
from email_otp import get_email, get_otp
from selectolax.parser import HTMLParser


async def get_urls():
        url_path = 'urls.txt'
        with open(url_path, 'r') as f:
            lines = f.readlines()
            return lines


async def getEmail_otp(content):
    # Parse HTML content to extract email and OTP
    html = HTMLParser(content)
    try:
        email = html.css_first('.a-spacing-small .a-spacing-micro').text().split('Time Password (OTP) to')[-1].strip().split()[0]
        print(f'OTP has been sent to {email}')
        print('Getting OTP from email...')
        email_id = get_email(email)
        email_otp = get_otp(email_id)
        return email_otp
    except Exception as e:
        print(f'Error while extracting OTP: {e}')
        return None
    
async def get_number(number_path):
    # Retrieve mobile numbers from a file
    with open(number_path, 'r') as f:
        lines = f.readlines()
        try:
            number = lines.pop(0)
        except Exception as e:
            print(f'Number does not exist in the {number_path} file!')
            return None
    with open(number_path, 'w') as file:
        file.writelines(lines)
    
    return number

async def main(urls, country_code):
    # Main function for processing multiple URLs
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=90)
        context = await browser.new_context()
        tasks = []
        for url in urls:
            tasks.append(fetch_page(context, url, country_code))
        await asyncio.gather(*tasks)


async def fetch_page(context, url, country_code):
    try:
        # Fetch and process each page
        page = await context.new_page()
        await page.goto(url)
        
        # Locating elements
        change_button = page.locator("a").filter(has_text="Change")
        add_mobile_number_btn = page.get_by_label("Add mobile number")
        
        # Waiting for page to load
        await page.wait_for_timeout(3000)
        
        # Getting OTP from email
        email_otp = await getEmail_otp(await page.content())
        
        # Handling OTP verification
        if email_otp is None:
            print('Invalid link!')
            return None
        else:
            await page.locator("#cvf-input-code").fill(email_otp)
            await page.get_by_label("Verify").click()
            await page.wait_for_load_state('networkidle')
            
            # Selecting country code
            if '1' in country_code:
                country_btn = page.get_by_text("Vietnam +")
                number_path = 'vietnam.txt'
            elif '2' in country_code:
                country_btn = page.get_by_text("Mozambique +")
                number_path = 'mozam.txt'
            elif '3' in country_code:
                country_btn =page.get_by_text("Indonesia +")
                number_path = 'indonatia.txt'
            
            # Adding mobile number
            for i in range(1, 13):
                await page.get_by_label("Select Country Code").locator("span").nth(1).click()
                await country_btn.click()
                mobile_num = await get_number(number_path)
                await page.get_by_role("textbox").fill(mobile_num)
                await add_mobile_number_btn.click()
                await page.wait_for_load_state('networkidle')
                await page.wait_for_timeout(2000)
                await change_button.click()
                await page.wait_for_load_state('networkidle')
                print(f'{i} OTP has been sent!')
            
            # Finalizing
            print(f'Job done for this url: {url}')
            await page.wait_for_timeout(1000)
    except TimeoutError as te:
        print(f'Timeout error occurred: {te}')
    except Exception as tce:
        pass
        # print(f'Something wired!')
    finally:
        if page:
            await page.close()



async def start():
    # Starting point of the program
    # urls = [
    #     'https://sellercentral.amazon.com/ap/cvf/request?arb=c57ff05d-ee71-4c21-a024-a7266bcf6cb2&language=en_US',
    #     'https://sellercentral.amazon.com/ap/cvf/request?arb=a8f70d4b-650a-4154-9f06-bc867dfa9809&language=en_US'
    # ]
    urls = await get_urls()
    country_code = input('''
Please chosse a number for country select
1: Vietnam
2: Mozambique
3: Indonesia
''')
    # country = '2'
    await main(urls, country_code)


asyncio.run(start())
