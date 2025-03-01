import geoip2.database
from django.conf import settings

VALID_COUNTRIES = {'AZ', 'AM', 'BY', 'KZ', 'KG', 'MD', 'RU', 'TJ', 'TM', 'UZ'}


def get_country_from_ip(ip_address):
    """ Определяет страну по IP, используя локальную базу GeoLite2 """
    try:
        with geoip2.database.Reader(f"{settings.GEOIP_PATH}/GeoLite2-Country.mmdb") as reader:
            response = reader.country(ip_address)
            country_code = response.country.iso_code  # Вернет, например, 'RU', 'US', 'DE'
            return country_code if country_code in VALID_COUNTRIES else 'CSM'  # Если не СНГ, ставим 'CSM'
    except Exception as e:
        print(f"Ошибка определения страны: {e}")
        return 'CSM'  # Если ошибка — тоже 'CSM'
