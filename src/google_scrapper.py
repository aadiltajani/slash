# __author__      =
# "Aadil Tajani, Dhruvish Patel,
# Kaustubh Deshpande, Aastha Singh, Arpit Chaudhary"
# __copyright__      = "Open source libraries"
import requests
from bs4 import BeautifulSoup
import time

def searchGoogle(query, sortval, number=0):
    st = time.time()
    number = int(number)

    print('Searching for', query, '  Sort:', sortval, ','
          'showing {} results'.format(number if number != 0 else 'all'))

    # CONFIGURATION
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
            "537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    url = (r'https://www.google.com'
           r'/search?hl=en&tbm=shop&q={}&&sclient=products-cc'
           .format('+'.join(query.split(' '))))
    # REQUEST
    response = requests.get(url,
                            # params=params,
                            headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    # PARSING RESPONSE
    shopping_data_dict = {}
    inline_results = []
    shopping_results = []
    sellers = set()
    for inline_result in soup.select('.sh-np__click-target'):
        inline_shopping_title = inline_result.select_one(
            '.sh-np__product-title').text
        inline_shopping_link = f"https://www.google.com{inline_result['href']}"
        inline_shopping_price = inline_result.select_one('b').text
        inline_shopping_source = inline_result.select_one(
            '.E5ocAb').text.strip()
        sellers.add(inline_shopping_source)
        inline_shopping_image = inline_result.findAll('img')[0].attrs['src']
        try:
            inline_shopping_rating = inline_result.select_one('.qSSQfd').text
        except Exception:
            inline_shopping_rating = None
        try:
            price_description = inline_result.select_one(
                '.SHsMUd').text

        except Exception:
            price_description = ''

        inline_results.append({
            'title': inline_shopping_title,
            'source': inline_shopping_source,
            'price': inline_shopping_price,
            'rating': inline_shopping_rating,
            'link': inline_shopping_link,
            'delivery': None,
            'price_description': price_description,
            'image': inline_shopping_image,
        })

    res = soup.find_all('div', class_='sh-dgr__content')
    for r in res:
        title = r.select_one('.tAxDx').text
        product_link = f"https://www.google.com\
                       {r.select_one('.Lq5OHe.eaGTj')['href']}"
        source = r.select_one('.IuHnof').text
        sellers.add(source)
        price = r.select_one('.OFFNJ').text
        image = r.find('img')
        rating = r.select_one('.QIrs8').text
        try:
            delivery = r.select_one('.vEjMR').text
        except Exception:
            delivery = None

        try:
            price_description = r.select_one('.LGq5Zc').text
        except Exception:
            price_description = ''

        shopping_results.append({
            'title': title,
            'source': source,
            'price': price,
            'rating': rating,
            'link': product_link,
            'delivery': delivery,
            'image': image,
            'price_description': price_description
        })

    print('No of sellers:', len(sellers), '  Sellers:', sellers)
    results = inline_results + shopping_results
    if sortval:
        results.sort(key=lambda x: float(
                     ''.join(x['price'][1:].split()[0].split(','))))
    if 0 < number < len(results):
        results = results[:number]
    shopping_data_dict.update({"inline_shopping_results": results})
    print('Time Taken:', time.time() - st, 'seconds')
    for i in shopping_data_dict['inline_shopping_results']:
        print(i)

    return shopping_data_dict
