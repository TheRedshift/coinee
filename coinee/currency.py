import forex_python.bitcoin, forex_python.converter

# Write a function that takes a 3 letter currency codes and prints the current BTC price in that currency


class BtcToX:

    def btctoanything(self, currency_code):

        if currency_code == ('x' or 'X'):
            return

        else:

            b = forex_python.bitcoin.BtcConverter()

            result = b.convert_btc_to_cur(1, currency_code)

            c = forex_python.converter.CurrencyCodes()

            currency_code = c.get_symbol(currency_code)

            result = str(currency_code) + str(result)

            print(result)

