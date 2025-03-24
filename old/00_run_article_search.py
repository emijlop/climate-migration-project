import datetime
from gdeltdoc import Filters, GdeltDoc  # importing the gdelt api client and filtering tools
import pandas as pd  # importing pandas for organizing and saving data

current_datetime=datetime.datetime.now()

# initializing the gdelt api client
gd = GdeltDoc()  # creating an instance of the gdelt api client to search for news articles

# defining the countries of interest and the keywords related to climate issues
search_queries = {
    "China": ["water scarcity", "crop failure", "sea-level rise", "pollution"],
    "Türkiye": ["drought", "earthquake", "flooding", "water stress"],
    "Philippines": ["typhoon", "storm surge", "sea-level rise", "El Niño"],
    "Somalia": ["drought", "conflict over water", "pastoralist crisis"],
    "Bangladesh": ["flooding", "monsoon displacement", "salinization", "cyclone"]
}

# defining country codes used by gdelt (fips 2-letter codes)
country_codes = {
    "China": "CH",
    "Türkiye": "TU",
    "Philippines": "RP",
    "Somalia": "SO",
    "Bangladesh": "BG"
}

# creating a list to store extracted news articles
all_results = []

# defining the time range for the search (last 3 months)
start_date = "2023-12-01"  # specifying the start date of the search
end_date = "2024-03-01"  # specifying the end date of the search

# iterating through each country and its respective keywords to fetch relevant news articles
for country, keywords in search_queries.items():  # looping through each country in the dictionary
    for keyword in keywords:  # looping through each keyword associated with the country
        
        # defining search filters for querying the gdelt api
        f = Filters(
            start_date=start_date,  # setting the start date for the search
            end_date=end_date,  # setting the end date for the search
            num_records=100,  # limiting the number of articles retrieved per keyword to 100
            keyword=keyword,  # specifying the keyword to search for
            country=country_codes[country]  # restricting results to the given country
        )

        # executing the search query using the gdelt api
        results = gd.article_search(f)  

        # checking if results were found
        if not results.empty:
            print(f"found articles for {country} - {keyword}")  # printing confirmation of results
            print("available columns:", results.columns)  # displaying available columns in the results
        else:
            print(f"no articles found for {country} - {keyword}")  # notifying if no articles were retrieved
            continue  # moving on to the next keyword

        # extracting relevant details from the retrieved articles
        for index, row in results.iterrows():
            all_results.append({  
                "Country": country,  # storing the country name
                "Keyword": keyword,  # storing the keyword used in the search
                "Title": row["title"],  # extracting the article title
                "URL": row["url"],  # extracting the article url
                "Source Country": row["sourcecountry"],  # extracting the article source,
                "Date": row.get("seendate", "N/A")  # extracting the article date, defaulting to "N/A" if missing
            })

# converting the extracted data into a pandas dataframe for easier manipulation
df_results = pd.DataFrame(all_results)

# saving the results as a csv file for further analysis
df_results.to_csv("data/climate_migration_news.csv", index=False)  # saving without row indices

# displaying the first few rows of the dataset to verify the output
print(df_results.head())  