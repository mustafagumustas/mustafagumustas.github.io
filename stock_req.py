import pandas_datareader.data as web
import pandas_datareader as pdr


tsla = web.DataReader("TSLA", "stooq")
appl = web.DataReader("AAPL", "stooq")

# Modify the Python script to generate HTML content
html_content = "<table>"
html_content += "<tr><th>Date</th><th>Open</th><th>High</th><th>Low</th><th>Close</th><th>Volume</th></tr>"


last_days_data = appl.head(7)

for _, row in last_days_data.iterrows():
    html_content += f"<tr><td>{row.name}</td><td>{row['Open']}</td><td>{row['High']}</td><td>{row['Low']}</td><td>{row['Close']}</td><td>{row['Volume']}</td></tr>"

html_content += "</table>"

# Save the generated HTML content to the HTML file
with open("stock_data.html", "w") as html_file:
    html_file.write(html_content)
