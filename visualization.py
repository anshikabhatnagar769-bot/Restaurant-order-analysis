
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")
os.makedirs("output", exist_ok=True)


def cuisine_chart(cuisines):
    plt.figure(figsize=(10, 5))
    cuisines.plot(kind="bar")
    plt.title("Top 10 Popular Cuisines")
    plt.xlabel("Cuisines")
    plt.ylabel("Number of Restaurants")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/cuisines.png")
    plt.show()


def city_chart(cities):
    plt.figure(figsize=(10, 5))
    cities.plot(kind="bar")
    plt.title("Top 10 Cities with Restaurants")
    plt.xlabel("City")
    plt.ylabel("Number of Restaurants")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/cities.png")
    plt.show()


def delivery_chart(df):
    delivery = df["Has Online delivery"].value_counts()
    plt.figure(figsize=(6, 6))
    delivery.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Online Delivery Availability")
    plt.ylabel("")
    plt.savefig("output/delivery.png")
    plt.show()


def rating_chart(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df["Aggregate rating"], bins=10)
    plt.title("Restaurant Rating Distribution")
    plt.xlabel("Restaurant Rating")
    plt.ylabel("Number of Restaurants")
    plt.tight_layout()
    plt.savefig("output/ratings.png")
    plt.show()


def price_chart(df):
    price = df["Price range"].value_counts().sort_index()
    plt.figure(figsize=(7, 5))
    price.plot(kind="bar")
    plt.title("Restaurant Price Range")
    plt.xlabel("Price Range")
    plt.ylabel("Number of Restaurants")
    plt.tight_layout()
    plt.savefig("output/price_range.png")
    plt.show()
