# Selenium webscraper using Chrome driver. 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

# Opens Yahoo Finance link with 5 year time period specified. 
driver = webdriver.Chrome()
driver.get('''https://au.finance.yahoo.com/quote/%5EAORD/history?period1=1414108800&period2=1587081600&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true''')

# Takes the date and adjusted closing price for all the table rows present. 
rows = []
for i in range(1, 67):
    xpath = '''//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[''' + str(i) + ']'
    row = driver.find_element(By.XPATH, xpath).text
    row = row.split(" ")

    date = row[0] + row[1] + row[2]
    adjusted_close = row[7]
    
    rows.append((date, float(adjusted_close.replace(',', ''))))

# Reverses list
rows = rows[::-1]

# Writes into a CSV file. Data then added to excel sheet. 
with open('market_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(0, len(rows)):
        writer.writerow([rows[i][0], rows[i][1]])

