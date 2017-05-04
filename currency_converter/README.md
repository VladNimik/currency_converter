# Currency converter
##### Autor
Vladyslav Nimizhan (vladnimik@gmail.com)

## Parameters
- --amount - amount which we want to convert - float
- --input_currency - input currency - 3 letters name or currency symbol
- --output_currency - requested/output currency - 3 letters name or currency symbol

## Functionality
- if output_currency param is missing, convert to all known currencies
## Requirements
- Python 2.7
- BeautifulSoup from bs4

## Usage variants
Full version
```
currency_converter.py --amount 100 --input_currency £ --output_currency EUR
```
Short version
```
currency_converter.py --amount 100 --i £ -o EUR
```
## Output

- json with following structure.
```
{
    "input": {
        "amount": <float>,
        "currency": <3 letter currency code>
    }
    "output": {
        <3 letter currency code>: <float>
    }
}
```
## Examples

```
./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK
{
    "input": {
        "currency": "EUR",
        "amount": 100.0
    },
    "output": {
        "CZK": 2676.4
    }
}

```
```
./currency_converter.py --amount 0.9 --input_currency ¥ --output_currency AUD
{
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.20,
    }
}
```
```
./currency_converter.py --amount 100 --input_currency $
{
    "input": {
        "amount": 100.0,
        "currency": "GBP"
    },
    "output": {
        "AFN": 8716.24,
        "ALL": 15910.900000000001,
        "ANG": 230.224,
        "AUD": 174.219,
        "AWG": 230.74699999999999,
        "AZN": 217.132,
        "BAM": 230.69600000000003,
        "BGN": 230.853,
        "BOB": 891.7020000000001,
        "BRL": 409.84299999999996,
        "BWP": 1359.08,
        "BYN": 242.12699999999998,
        "BZD": 257.86899999999997,
        "CHF": 127.91900000000001,
        "CNY": 884.547,
        "CRC": 72638.4,
        "CUP": 3415.37,
        "CZK": 3162.76,
        "DKK": 877.4340000000001,
        "DOP": 6084.44,
        "EUR": 117.953,
        "FKP": 100.0,
        "GBP": 100.0,
        "GGP": 100.0,
        "GHS": 541.754,
        "GIP": 100.0,
        "GTQ": 946.1499999999999,
        "HNL": 3024.29,
        "HRK": 878.714,
        "HUF": 36826.0,
        "IDR": 1714986.0,
        "ILS": 466.27200000000005,
        "IMP": 100.0,
        "INR": 8279.42,
        "IRR": 4179656.0,
        "ISK": 13697.6,
        "JEP": 100.0,
        "JMD": 16615.600000000002,
        "JPY": 14544.0,
        "KGS": 8720.619999999999,
        "KHR": 522947.0,
        "KPW": 16773.4,
        "KRW": 146494.0,
        "KZT": 40744.600000000006,
        "LAK": 1049294.0,
        "LBP": 194642.0,
        "LKR": 19663.8,
        "MKD": 7252.95,
        "MNT": 311542.0,
        "MUR": 4491.95,
        "MYR": 557.6279999999999,
        "MZN": 8201.67,
        "NGN": 40740.4,
        "NIO": 3843.3900000000003,
        "NOK": 1117.81,
        "NPR": 13223.300000000001,
        "OMR": 49.6278,
        "PAB": 128.90900000000002,
        "PEN": 418.89300000000003,
        "PHP": 6440.82,
        "PKR": 13519.999999999998,
        "PLN": 497.291,
        "PYG": 719502.0,
        "QAR": 469.49500000000006,
        "RON": 535.987,
        "RSD": 14542.599999999999,
        "RUB": 7457.71,
        "SAR": 483.512,
        "SCR": 1752.1200000000001,
        "SEK": 1138.49,
        "SHP": 100.0,
        "SOS": 74756.8,
        "SYP": 27628.500000000004,
        "THB": 4466.530000000001,
        "TRY": 458.217,
        "TTD": 869.2,
        "TWD": 3887.2,
        "UAH": 3415.05,
        "USD": 128.828,
        "UYU": 3611.76,
        "UZS": 481564.00000000006,
        "VEF": 1286.54,
        "VND": 2931968.0,
        "YER": 32262.8,
        "ZAR": 1741.2600000000002,
        "ZWD": 46652.1
    }
}
```
## Notes

Application uses  actual currency conversion API http://rate-exchange-1.appspot.com/ and http://www.xe.com/symbols.php for all currency symbols. Application provide 86 various currencies.
