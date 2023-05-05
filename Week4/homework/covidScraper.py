from selenium import webdriver
import pandas as pd
import datetime

# Define the URL pattern
url_pattern = "https://example.com/injuries/{}"

# Define the date range for which we want to scrape data
start_date = datetime.date(2023, 4, 28)
end_date = datetime.date(2023, 5, 4)

# Initialize a webdriver
driver = webdriver.Chrome()

# Create an empty dataframe to store the scraped data
data = pd.DataFrame(columns=["City"])

# Loop through the dates and scrape the data
for date in pd.date_range(start=start_date, end=end_date):
    # Construct the URL for the current date
    url = url_pattern.format(date.strftime("%Y-%m-%d"))

    # Load the page
    driver.get(url)

    # Find the table on the page
    table = driver.find_element_by_tag_name("table")

    # Extract the data from the table
    rows = table.find_elements_by_tag_name("tr")

    # Loop through the rows and extract the city and number of injuries
    for row in rows:
        cells = row.find_elements_by_tag_name("td")
        if len(cells) == 2:
            city = cells[0].text
            injuries = cells[1].text

            # If the city is not already in the dataframe, add it
            if city not in data["City"].tolist():
                data.loc[len(data)] = [city]

            # Add the number of injuries to the appropriate date column
            data.loc[data["City"] == city, date.strftime("%d %B")] = injuries

# Save the data to an Excel file
data.to_excel("injuries.xlsx", index=False)
