from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

# incercare cu pandas NOT READY!

# Setup
driver = webdriver.Chrome()

url_pattern = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{}-martie-ora-13-00-2/"

start_date = 1
end_date = 5
data = {}


for date in range(start_date, end_date):
    url = url_pattern.format(date)

    print(url)

    driver.get(url)

    # Find the first table on the page
    try:
        tables = driver.find_element(by=By.TAG_NAME, value="table")
    except:
        print(f"No table found on {url}. Skipping...")
        continue

    rows = tables.find_elements(By.TAG_NAME, "tr")
    num_cells = None
    for i, row in enumerate(rows):
        if i == 0:
            num_cells = len(row.find_elements(By.TAG_NAME, "th"))
            continue  # skip the first row
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) != num_cells:
            print(
                f"Skipping row {i} on {url} because it has {len(cells)} cells instead of {num_cells}"
            )
            continue

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
for i, col_name in enumerate(data.keys()):
    df[col_name] = data[col_name]
df.to_excel("covid_data_pandas.xlsx")

driver.quit()
