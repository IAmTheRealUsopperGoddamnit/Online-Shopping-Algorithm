products = int(input("Number of products you want to choose between: "))
ratings = []
reviews = []
prices = []

for i in range(1, products + 1):
    rating = float(input(f"Enter the rating of product {i}: "))
    review = float(input(f"Number of reviews of product {i}: "))
    price = float(input(f"Price of product {i}: "))
    ratings.append(rating)
    reviews.append(review)
    prices.append(price)
    
avgratall = sum(ratings) / products
avgrevall = sum(reviews) / products
avgpriall = sum(prices) / products

weights = []

for i in range(1, products + 1):
    weight = (((avgratall * reviews[i - 1]) + (ratings[i - 1] * avgrevall)) / (reviews[i - 1]
    + avgrevall)) * (avgpriall + sum(prices)) / (prices[i - 1] + sum(prices))
    weights.append(weight)
    
maxweirat = max(weights)
bestpronum = weights.index(maxweirat)

answer = input("Do you want to see the weighted rating of all products (y/n)?")
if answer == "y":
    for i in range(1, products + 1):
        print(f"The weighted rating of product {i} is: ", (((avgratall * reviews[i - 1]) + (ratings[i - 1] * avgrevall)) / (reviews[i - 1]
               + avgrevall)) * (avgpriall + sum(prices)) / (prices[i - 1] + sum(prices)))
else:
    print("Product", bestpronum + 1, "has the highest weighted rating of", maxweirat)

