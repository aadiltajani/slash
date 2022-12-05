from google_scrapper import searchGoogle

# searching without sorting, retrieving 10 items
googleSearch('iphone 14', False, 10)

# searching with sorting, retrieving 10 items
googleSearch('cake', True, 20)

# searching without sorting, retrieving all items
googleSearch('charger', False)

# searching with sorting, retrieving all items
googleSearch('milk', True)