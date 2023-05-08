from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up the driver (assuming you're using Chrome)
driver = webdriver.Chrome()

# Load the page
url_pattern = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{}-martie-ora-13-00-2/"

# Define the date range for which we want to scrape data
start_date = 1
end_date = 5
data = {}

# Loop through the dates and scrape the data
for date in range(start_date, end_date):
    # Construct the URL for the current date
    url = url_pattern.format(date)

    print(url)

    # Load the page
    driver.get(url)

    # Find the first table on the page
    try:
        tables = driver.find_element(by=By.TAG_NAME, value="table")
    except:
        print(f"No table found on {url}. Skipping...")
        continue
    # Extract the data from each table
    rows = tables.find_elements(By.TAG_NAME, "tr")
    for i, row in enumerate(rows):
        if i == 0:
            continue  # skip the first row
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 3:
            city = cells[1].text
            value = cells[2].text
            if city not in data:
                data[city] = [value]
            else:
                data[city].append(value)

# Write the data to an Excel file using pandas
df = pd.DataFrame(data)
df.index.name = "City"
for i in range(start_date, end_date):
    df[f"Table {i}"] = df.pop(str(i))
df.to_excel("covid_data_pandas.xlsx")

# Close the driver
driver.quit()
