import requests

req = requests.get('https://www.marketwatch.com/investing/stock/AAPL')    
pos = req.text.find('Yield</small>')
print(req.text[pos:pos+100])

with open("test.html", 'w') as f:
        f.write(req.text)