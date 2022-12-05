import google_scrapper

# searching without sorting, retrieving 10 items
google_scrapper.searchGoogle('iphone 14', False, 10)

# searching with sorting, retrieving 10 items
google_scrapper.searchGoogle('cake', True, 20)

# searching without sorting, retrieving all items
google_scrapper.searchGoogle('charger', False)

# searching with sorting, retrieving all items
google_scrapper.searchGoogle('milk', True)
