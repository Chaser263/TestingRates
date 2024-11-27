A rate scraper to get instant checks on other HYSA APY's, checks bots.txt to ensure compliant with web-scraping best practices

***Can add banks without a proper coding background***
1. go to bank website page, 2. right click inspect element in chrome 3. go directly over the rate number 
4. copy the highlighted span and add to list

***Ex: Discover***
1. go to https://www.discover.com/online-banking/savings-account/, 2. inspect element over the "3.90% APY", see it says "span.reflectApy", put "span.reflectApy" as the 'selector' in the list section of the code 

Sample input: 
        {
            'name': 'Discover',
            'url': 'https://www.discover.com/online-banking/savings-account/',
            'selector': 'span.reflectApy'
        },
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
            'name': 'Citizens',
            'url': 'https://www.secure.citizensaccess.com/Citizens',
            'selector': 'span._productLine.inactive.active[product_line="cax"]'
        }
    ]

Takes a maximum of ~10s per bank 
Final Results:
         bank                  timestamp  bots_allowed  rate
0    Discover 2024-11-27 14:37:59.387037          True  3.90
1        Ally 2024-11-27 14:38:09.183178          True  3.85
2        Amex 2024-11-27 14:38:13.235780          True  3.90
3  CapitalOne 2024-11-27 14:38:16.252499          True  3.90
4    Barclays 2024-11-27 14:38:19.260971          True  4.80
5    Citizens 2024-11-27 14:38:19.410490         False   NaN

