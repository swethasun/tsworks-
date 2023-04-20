url = 'https://finance.yahoo.com/quote/IBM/history?p=IBM'       #can be used for different companies

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'data-test': 'historical-prices'})
data = []

for row in table.tbody.find_all('tr'):
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
