
# ZOMATO RESTAURANT DATA ANALYSIS PROJECT

# Importing functions from other files

from data_cleaning import load_data, clean_data

from analysis import (
    basic_analysis,
    rating_analysis,
    cuisine_analysis,
    city_analysis,
    delivery_analysis,
    price_analysis
)

from visualization import (
    cuisine_chart,
    city_chart,
    delivery_chart,
    rating_chart,
    price_chart
)


# STEP 1: LOAD DATASET

print("\nLoading Zomato Dataset...")

df = load_data()


# STEP 2: CLEAN DATA

print("\nCleaning Dataset...")

df = clean_data(df)


# STEP 3: BASIC DATA ANALYSIS

print("\nPerforming Basic Analysis...")

basic_analysis(df)


# STEP 4: RATING ANALYSIS

print("\nPerforming Rating Analysis...")

rating_analysis(df)


# STEP 5: CUISINE ANALYSIS

print("\nPerforming Cuisine Analysis...")

cuisines = cuisine_analysis(df)


# STEP 6: CITY ANALYSIS

print("\nPerforming City Analysis...")

cities = city_analysis(df)


# STEP 7: DELIVERY ANALYSIS

print("\nPerforming Delivery Analysis...")

delivery_analysis(df)


# STEP 8: PRICE ANALYSIS

print("\nPerforming Price Analysis...")

price_analysis(df)


# STEP 9: DATA VISUALIZATION

print("\nCreating Graphs...")

cuisine_chart(cuisines)

city_chart(cities)

delivery_chart(df)

rating_chart(df)

price_chart(df)


# STEP 10: FINAL REPORT

print("\n================================")
print(" ZOMATO DATA ANALYSIS COMPLETED ")
print("================================")

print("Total Restaurants:", len(df))

print("Average Rating:",
      round(df["Aggregate rating"].mean(), 2))

print("Total Cities:",
      df["City"].nunique())

print("\nAll graphs saved in the output folder.")

print("\nThank You!")
