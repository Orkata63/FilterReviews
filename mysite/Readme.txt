Simple Django app that filters and sorts a Json file without a Database. The logic on the filtering and sorting is described in sort-logic.py,
which isn`t a part of the app. The filtering is done in 2 pages, the 1st form.html page contains the dropdown options on the 4 variables we look at
while the result.html prints the Reviews that meet the conditions. Implementation of reading and filtering + sorting the Json is done in the views.py
divided in filtering with min_rating and text and no text that is done separete then the sorting, which is done firstly by Date then by rating,
following pythons rules of secondary then primary keys
