import requests

f = open("constituents.csv",'r' )
csv = f.readlines()
f. close()
sp500 = []

for x in range(1,len(csv)):
    csvline = csv[x].split(",")
    company = csvline[0]
    try:
        req = requests.get('https://www.marketbeat.com/stocks/'+company,timeout=10)
        pos = req.text.find("Dividend Yield<strong>")
        co = []
        co.append(company)
        co.append(req.text[pos+22:pos+26])
        print(co)
        sp500.append(co)
    except Exception as e:
        print(e)
