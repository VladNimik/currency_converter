import argparse
import json
import sys
import urllib2
import html2json


class SaveCurrencies:
    def __init__(self):
        self.currency = html2json.parseTable()
        # self.currency = htmlToJson.parseJson()

    # get USD and compare with $
    def getInputCurrency(self, code):
        currencyList = []
        for key, value in self.currency.iteritems():
            try:
                if value == code.decode('utf-8') or key == code.decode('utf-8'):
                    currencyList.append(key)
                    break
            except:
                if value == code or key == code:
                    currencyList.append(key)
                    break

        return currencyList

    # return all currencies from web
    def getAll(self):
        currencyList = []
        for key, value in self.currency.iteritems():
            currencyList.append(key)
        # print currencyList
        return currencyList


class CovertCurrencies:
    def __init__(self, ic, oc, amount):
        self.ic = ic
        self.oc = oc
        self.amount = amount

    def convertLink(self):
        # json dumps
        response = {}
        response['input'] = {}
        response['input']['amount'] = self.amount
        response['input']['currency'] = self.ic[0]  # first item
        response['output'] = {}
        # get all links from rate-exchange for all currencies
        for ic in self.ic:  # all input currencies
            for oc in self.oc:  # output currencies
                self.convertCurrency(ic, oc)  # call converter
                html = self.convertCurrency(ic, oc)
                data = json.loads(html)
                response['output'][oc] = data['v']
            print json.dumps(response, sort_keys=True, indent=4)

    def convertCurrency(self, ic, oc):
        response = urllib2.urlopen(
            'http://rate-exchange-1.appspot.com/currency?from=' + str(ic) + '&to=' + str(oc) + '&q=' + str(self.amount))

        html = response.read()
        return html


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('-a', '--amount',
                       metavar='amount',
                       type=float,
                       help='amount which we want to convert - float',
                       required=True)
    parse.add_argument("-i", "--input_currency",
                       metavar='input_currency',
                       type=str,
                       help='3 letters name or currency symbol',
                       required=True)

    parse.add_argument("-o", "--output_currency",
                       metavar='output_currency',
                       type=str,
                       help='requested/output currency - 3 letters name or currency symbol',
                       required=False)

    opts = parse.parse_args()

    # print opts


    if opts.amount is None or opts.input_currency is None:
        sys.exit(1)

    if len(opts.input_currency) <= 3:
        # print (opts.input_currency)

        myDict = SaveCurrencies()
        currencyListInput = myDict.getInputCurrency(opts.input_currency)
        currencyListOutput = myDict.getInputCurrency(opts.output_currency)

    if opts.input_currency and opts.amount and opts.output_currency is None:
        myDict = SaveCurrencies()
        currencyListOutput = myDict.getAll()

    link = CovertCurrencies(currencyListInput, currencyListOutput, opts.amount)
    link.convertLink()


if __name__ == '__main__':
    currency = main()
