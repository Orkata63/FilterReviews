from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def form(request):
    return render(request, 'filter/form.html')


def filter_reviews(request):
    priority_text = request.POST.get('priority_text') == "True"
    order_by_rating = request.POST.get('order_by_rating') == "True"
    order_by_date = request.POST.get('order_by_date') == "True"
    min_rating = int(request.POST.get('min_rating'))

    filtered_reviews = sorting_json(priority_text, order_by_rating, order_by_date, min_rating)

    context = {'reviews': filtered_reviews}
    return render(request, 'filter/result.html', context)

def sorting_json(priority_text, order_by_rating,order_by_date, min_rating):
    with open('reviews (2) (2) (2).json', 'r') as file:
        reviews_data = json.load(file)
    filtered_reviews_text = []
    filtered_reviews_no_text = []

    for review in reviews_data:
        rating = review["rating"]
        if rating >= int(min_rating):
            if len(review['reviewText']) > 0:
                filtered_reviews_text.append(review)
            else:
                filtered_reviews_no_text.append(review)


    print(type(priority_text), type(order_by_rating), type(order_by_date), min_rating)
    # divided the text and no text for an easier time
    if priority_text == False:
        filtered_reviews = filtered_reviews_text + filtered_reviews_no_text
        filtered_reviews.sort(key=lambda r: ( r['reviewCreatedOnTime']), reverse=order_by_rating)
        filtered_reviews.sort(key=lambda r: r['rating'], reverse=order_by_date)
        return filtered_reviews
    else:
        filtered_reviews_text.sort(key=lambda r: r['reviewCreatedOnTime'], reverse=order_by_date)
        filtered_reviews_text.sort(key=lambda r: r['rating'], reverse=order_by_rating)
        filtered_reviews_no_text.sort(key=lambda r: r['reviewCreatedOnTime'], reverse=order_by_date)
        filtered_reviews_no_text.sort(key=lambda r: r['rating'], reverse=order_by_rating)
        filtered_reviews = filtered_reviews_text + filtered_reviews_no_text

        return filtered_reviews

