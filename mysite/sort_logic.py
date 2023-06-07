import json


if __name__ == "__main__":
    with open('reviews (2) (2) (2).json', 'r') as file:
        reviews_data = json.load(file)
    filtered_reviews_text = []
    filtered_reviews_no_text = []
    min_rating = 3
    order_by_rating = False
    order_by_date = False
    priority_text = True
    for review in reviews_data:
        rating = review["rating"]
        if rating >= int(min_rating):
            if len(review['reviewText']) > 0:
                filtered_reviews_text.append(review)
            else:
                filtered_reviews_no_text.append(review)
    filtered_reviews_text.sort(key=lambda r:  r['reviewCreatedOnTime'], reverse=order_by_date)
    filtered_reviews_text.sort(key=lambda r: r['rating'], reverse=order_by_rating)
    filtered_reviews_no_text.sort(key=lambda r:  r['reviewCreatedOnTime'], reverse=order_by_date)
    filtered_reviews_no_text.sort(key=lambda r: r['rating'], reverse=order_by_rating)
    filtered_reviews = filtered_reviews_text + filtered_reviews_no_text
    for i in filtered_reviews:
        print(i)