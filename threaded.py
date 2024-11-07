from concurrent import futures
import requests

# Add headers to avoid being blocked
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.marketwatch.com',
}

sp500 = []

def get_div(csvline):
    company = csvline.split(",")[0]  # Get just the company ticker
    try:
        req = requests.get('https://www.marketwatch.com/investing/stock/'+company,
                          headers=headers,
                          timeout=10)
        
        start = req.text.find('Yield</small>')
        if start != -1:  # Only proceed if 'Yield' is found
            # Find the class="primary" element that contains the yield value
            start = req.text.find('primary', start)
            # Move to the actual start of the yield value after the ">" character
            start = req.text.find('">', start) + 2
            # Find the end of the yield value (marked by the next HTML tag)
            end = req.text.find('<', start)
            # Extract and clean the yield percentage
            yield_percentage = req.text[start:end].strip()
            
            co = [company, yield_percentage]
            print(co)
            sp500.append(co)
        else:
            # Use N/A for consistency when yield data isn't found
            co = [company, "N/A"]
            print(co)
            sp500.append(co)
            
    except Exception as e:
        # Use N/A for any errors during processing
        co = [company, "N/A"]
        print(co)
        sp500.append(co)
        print(f"Error processing {company}: {e}")

with futures.ThreadPoolExecutor(max_workers=4) as executor:
    f = open("constituents.csv",'r')
    csv = f.readlines()[1:]  # Skip header row
    f.close()
    
    for _ in executor.map(get_div, csv):
        pass
    
    div = sorted(sp500, key=lambda x: x[1])
    with open("dividend.csv", 'w') as f:
        for item in div:
            f.write(str(item) + '\n')
