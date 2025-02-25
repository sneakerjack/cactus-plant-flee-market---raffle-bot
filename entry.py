import asyncio
from faker import Faker
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
import random
import string

# Function to load proxies from the file
def load_proxies(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

async def select_random_option(driver, dropdown_xpath, options_list):
    # Randomly select a value from the provided options list
    selected_value = random.choice(options_list)
    print(f"Randomly selected value: {selected_value}")

    # Find the dropdown element
    select = await driver.find_element(By.XPATH, dropdown_xpath)

    # Use JavaScript to set the dropdown value and trigger the change event
    cdp_command = '''
    const select = arguments[0];
    const value = arguments[1];
    select.value = value;
    select.dispatchEvent(new Event('change', {bubbles: true}));
    '''
    await driver.execute_script(cdp_command, select, selected_value)

async def fill_form(driver, email):
    try:
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.street_address()
        city = fake.city()
        zip_code = fake.zipcode()
        phone_number = '561' + ''.join(random.choices(string.digits, k=7))

        # Wait and click the sign-up button
        signup_button = await driver.find_element(By.XPATH, '//div[contains(@class, "raffle-app") and contains(@class, "raffle-trigger")]')
        await driver.execute_script("arguments[0].click();", signup_button)
        await asyncio.sleep(3)

        # Fill in the form fields
        await (await driver.find_element(By.ID, "email")).write(email)
        await (await driver.find_element(By.ID, "tel")).write(phone_number)
        await (await driver.find_element(By.ID, "firstName")).write(first_name)
        await (await driver.find_element(By.ID, "lastName")).write(last_name)
        await (await driver.find_element(By.ID, "address.address1")).write(address)
        await (await driver.find_element(By.ID, "address.city")).write(city)
        await (await driver.find_element(By.ID, "address.zip")).write(zip_code)

        # List of valid sizes
        valid_sizes = [
            "3.5", "4", "4.5", "5", "5.5", "6", "6.5", "7", "7.5", "8", "8.5",
            "9", "9.5", "10", "10.5", "11", "11.5", "12", "12.5", "13", "14", "15"
        ]
        # Select a random size
        await select_random_option(driver, '//select[@id="size"]', valid_sizes)

        # List of valid states
        valid_states = [
            "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL",
            "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE",
            "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD",
            "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
        ]
        # Select a random state
        await select_random_option(driver, '//select[@id="address.region"]', valid_states)

        # Agree to terms (checkbox)
        terms_checkbox = await driver.find_element(By.ID, "agreeTerms")
        await driver.execute_script("arguments[0].click();", terms_checkbox)
        await asyncio.sleep(3)

        # Submit the form
        submit_button = await driver.find_element(By.CSS_SELECTOR, 'button.c-signup__signup-button')
        await driver.execute_script("arguments[0].click();", submit_button)
        await asyncio.sleep(3)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

async def main():
    # Read emails from a file
    with open('emails.txt', 'r') as file:
        emails = file.readlines()

    emails = [email.strip() for email in emails]

    # Load proxies from file
    proxies = load_proxies('proxy.txt')
    proxy_count = len(proxies)

    for idx, email in enumerate(emails):
        proxy = proxies[idx % proxy_count]
        proxy_parts = proxy.split(':')
        proxy_host = proxy_parts[0]
        proxy_port = proxy_parts[1]
        proxy_user = proxy_parts[2]
        proxy_pass = proxy_parts[3]

        options = webdriver.ChromeOptions()

        # Keep your original proxy logic
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        cdp_command = f"""
        const url = 'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}';
        const [host, auth] = url.split('@');
        const proxyServer = host.replace('http://', '');
        session.setProxyOverride(proxyServer, auth)
        """

        async with webdriver.Chrome(options=options) as driver:
            try:
                await driver.get("https://shop.travisscott.com/")
                await asyncio.sleep(3)
                await fill_form(driver, email)
            except Exception as e:
                print(f"Failed to process email {email}: {e}")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nScript interrupted by user.")
