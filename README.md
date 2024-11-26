Sample Input: 
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

Takes about ~5-10s per bank 
Sample Output:
         bank                  timestamp  rate
0    Discover 2024-11-26 15:45:04.648692  3.90
1        Ally 2024-11-26 15:45:13.109223  3.85
2        Amex 2024-11-26 15:45:17.563293  4.00
3  CapitalOne 2024-11-26 15:45:22.326325  3.90
4    Barclays 2024-11-26 15:45:25.887530  4.80
5    Citizens 2024-11-26 15:45:56.774512   NaN


