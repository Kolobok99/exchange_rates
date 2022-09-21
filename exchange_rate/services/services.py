import requests
import xml.etree.ElementTree as ET

def get_exchange_rates_from_cbr_ru():
    """Возвращает список курсов валют с cbr.ru
        в виде (currency_name, currency_rate)
    """
    
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    
    page = requests.get(url)
    page_text = page.text

    root = ET.fromstring(page_text)
    valutes = []
    for valute in root.findall('Valute'):
        name = valute.findall('Name')[0].text
        rate = valute.findall('Value')[0].text
        rate = rate.replace(',', '.')
        d = (name, rate)
        valutes.append(d)
    return valutes
