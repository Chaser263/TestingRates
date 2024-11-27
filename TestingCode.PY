from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
## import necessary libraries: playwright for chrome, pandas for converting to CSV

##create function for checking robots.txt
def check_robots_allowed(url):
    try:
        parsed_url = urlparse(url)
        robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"

        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()

        path = parsed_url.path if parsed_url.path else '/'
        return rp.can_fetch("*", path)
    except Exception as e:
        print(f"Robot check error for {url}: {str(e)}")
        return True

##create list of banks we want to check
def scrape_bank_rates():
    banks = [
        {
            'name': 'Discover',
            'url': 'https://www.discover.com/online-banking/savings-account/',
            'selector': 'span.reflectApy'
        },
        ##This is the right selector for Ally, but Ally has a limit on multiple checks a day
        {
            'name': 'Ally',
            'url': 'https://www.ally.com/bank/online-savings-account/',
            'selector': 'span.allysf-rates-v1-value'
        },
        {
            'name': 'Amex',
            'url': 'https://www.americanexpress.com/en-us/banking/online-savings/account/',
            'selector': 'span#hysa-apy-1'
        },
        {
            'name': 'CapitalOne',
            'url': 'https://www.capitalone.com/bank/savings-accounts/online-performance-savings-account/',
            'selector': 'rates-inline[product="psa"]'
        },
        {
            'name': 'Barclays',
            'url': 'https://www.banking.barclaysus.com/tiered-savings.html',
            'selector': 'span#rate'
        },
        {
            #citizens has a bots exemption so won't pull a rate
            'name': 'Citizens',
            'url': 'https://www.secure.citizensaccess.com/Citizens',
            'selector': 'span._productLine.inactive.active[product_line="cax"]'
        }
    ]
    ##botsnotallowed for: Citizens

    results = []

##Open up Chrome Browser

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for bank in banks:
            print(f"\nProcessing {bank['name']}...")

            # Check robots.txt first
            bots_allowed = check_robots_allowed(bank['url'])
            print(f"Robots allowed for {bank['name']}: {bots_allowed}")

            rate = None

            ##grab the element from the page if bots are allowed
            if bots_allowed:
                try:
                    page.goto(bank['url'], wait_until='networkidle', timeout = 10000)
                    rate_element = page.locator(bank['selector']).first
                    rate_text = rate_element.text_content()

                    import re
                    rate = float(re.findall(r'\d*\.?\d+', rate_text)[0])
                    print(f"Completed {bank['name']}: Rate: {rate}%")

                except Exception as e:
                    print(f"Error processing {bank['name']}: {str(e)}")

            results.append({
                'bank': bank['name'],
                'timestamp': datetime.now(),
                'bots_allowed': bots_allowed,
                'rate': rate
            })

        browser.close()

    return pd.DataFrame(results)


if __name__ == "__main__":
    print("Starting rate collection...")

    df = scrape_bank_rates()

    filename = f"bank_rates_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    df.to_csv(filename, index=False)

    print("\nFinal Results:")
    print(df)
    print(f"\nResults saved to {filename}")
