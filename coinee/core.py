import currency

converter = currency.BtcToX()

while 1:

    currencyCode = input("Enter 3 letter currency code or X to exit\n")

    currencyCode = currencyCode.upper()

    converter.btctoanything(currencyCode)
