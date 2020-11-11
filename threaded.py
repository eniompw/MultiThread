from concurrent import futures
import requests

sp500 = []
def get_div(csvline):
    company = csvline.split(",")
    try:
        req = requests.get('https://www.marketbeat.com/stocks/'+company[0],timeout=10)
        pos = req.text.find("Dividend Yield<strong>")
        co = []
        co.append(company[0])
        co.append(req.text[pos+22:pos+26])
        print(co)
        sp500.append(co)
    except Exception as e:
        print(e)

with futures.ThreadPoolExecutor(max_workers=128) as executor:
    #https://github.com/datasets/s-and-p-500-companies/blob/master/data/constituents.csv'
    f = open("constituents.csv",'r' )
    csv = f.readlines()
    f. close()
    for _ in executor.map(get_div, csv):
        pass
    div = sorted(sp500,key=lambda x: x[1])
    f = open("dividend.csv",'w')
    for i in range(len(csv)):
        f.write(str(div[i]) + '\n')
    f. close()
