import pandas_datareader.data as web
from bs4 import BeautifulSoup

# Replace 'AAPL' with the desired company's symbol
symbol = "AAPL"
company_name = "Apple Inc."  # Add the company name here

# Load the existing HTML content
with open("stock_data.html", "r") as html_file:
    existing_html = html_file.read()

# Parse the existing HTML content
soup = BeautifulSoup(existing_html, "html.parser")

# Find the table element in the HTML
table = soup.find("table")

# Load stock data
stock_data = web.DataReader(symbol, "stooq")

# Get the last 7 days of data and append to the table
last_days_data = stock_data.head(7)
for _, row in last_days_data.iterrows():
    new_row = soup.new_tag("tr")
    new_row.append(soup.new_tag("td", text=str(row.name)))
    new_row.append(soup.new_tag("td", text=str(row["Open"])))
    new_row.append(soup.new_tag("td", text=str(row["High"])))
    new_row.append(soup.new_tag("td", text=str(row["Low"])))
    new_row.append(soup.new_tag("td", text=str(row["Close"])))
    new_row.append(soup.new_tag("td", text=str(row["Volume"])))
    table.append(new_row)

# Add the company name to the webpage
header = soup.find("header")
if header:
    h1 = header.find("h1")
    if h1:
        h1.string = f"Stock Market Data for {company_name}"

# Save the updated HTML content back to the HTML file
with open("stock_data.html", "w") as html_file:
    html_file.write(str(soup))

print(f"Stock data for {company_name} has been updated.")
