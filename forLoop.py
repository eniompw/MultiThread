import requests

f = open("constituents.csv",'r' )
csv = f.readlines()
f. close()
sp500 = []

for x in range(1,len(csv)):
    csvline = csv[x].split(",")
    company = csvline[0]
    try:
        req = requests.get('https://www.marketwatch.com/investing/stock/'+company,timeout=10)
        pos = req.text.find("Yield")
        co = []
        co.append(company)
        co.append(req.text[pos+57:pos+62])
        print(co)
        sp500.append(co)
    except Exception as e:
        print(e)
