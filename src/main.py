from google_scrapper import searchGoogle

# searching without sorting, retrieving 10 items
searchGoogle('iphone 14', False, 10)

# searching with sorting, retrieving 10 items
searchGoogle('cake', True, 20)

# searching without sorting, retrieving all items
searchGoogle('charger', False)

# searching with sorting, retrieving all items
searchGoogle('milk', True)
