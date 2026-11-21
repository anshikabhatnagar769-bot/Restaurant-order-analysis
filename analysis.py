
import pandas as pd

def basic_analysis(df):
    print("\n===== BASIC ANALYSIS =====")
    print("Total Restaurants:", len(df))
    print("Total Cities:", df["City"].nunique())
    print("Average Rating:", round(df["Aggregate rating"].mean(), 2))
    print("Total Votes:", df["Votes"].sum())


def rating_analysis(df):
    print("\n===== RATING ANALYSIS =====")
    print(df["Rating text"].value_counts())


def cuisine_analysis(df):
    print("\n===== CUISINE ANALYSIS =====")
    cuisines = df["Cuisines"].value_counts().head(10)
    print(cuisines)
    return cuisines


def city_analysis(df):
    print("\n===== CITY ANALYSIS =====")
    cities = df["City"].value_counts().head(10)
    print(cities)
    return cities


def delivery_analysis(df):
    print("\n===== DELIVERY ANALYSIS =====")
    print(df["Has Online delivery"].value_counts())


def price_analysis(df):
    print("\n===== PRICE ANALYSIS =====")
    print(df["Price range"].value_counts().sort_index())


def country_analysis(df):
    print("\n===== COUNTRY ANALYSIS =====")
    print(df["Country Code"].value_counts())
