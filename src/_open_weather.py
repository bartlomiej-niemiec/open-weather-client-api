class OpenWeatherRequest:
    GET_COORDINATE = "https://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit={limit}&appid={api_key}"
    CURRENT_WEATHER = "https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&lang={lang}&units={units}&mode={mode}"
    FORECAST = "https://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}&mode={mode}&cnt={cnt}&units={units}&lang={lang}"
    WEATHER_MAP = "https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={api_key}"

class Unit:
    KELVIN = ""
    FAHRENHEIT = "imperial"
    CELSIUS = "metric"


class Format:
    JSON = 'json'
    XML = 'xml'


class Language:
    Afrikaans = 'af'
    Albanian = 'al'
    Arabic = 'ar'
    Azerbaijani = 'az'
    Bulgarian = 'bg'
    Catalan = 'ca'
    Czech = 'cz'
    Danish = 'da'
    German = 'de'
    Greek = 'el'
    English = 'en'
    Basque = 'eu'
    Persian = 'fa'
    Finnish = 'fi'
    French = 'fr'
    Galician = 'gl'
    Hebrew = 'he'
    Hindi = 'hi'
    Croatian = 'hr'
    Hungarian = 'hu'
    Indonesian = 'id'
    Italian = 'it'
    Japanese = 'ja'
    Korean = 'kr'
    Latvian = 'la'
    Lithuanian = 'lt'
    Macedonian = 'lt'
    Norwegian = 'no'
    Dutch = 'nl'
    Polish = 'pl'
    Portuguese = 'pt'
    Português = 'pt_br'
    Brasil = 'pt_br'
    Romanian = 'ro'
    Russian = 'ru'
    Swedish = 'sv'
    Slovak = 'sk'
    Slovenian = 'sl'
    Spanish = 'sp'
    Serbian = 'sr'
    Thai = 'th'
    Turkish = 'tr'
    Ukrainian = 'ua'
    Vietnamese = 'vi'
    Chinese_Simplified = 'zh_cn'
    Chinese_Traditional = 'zh_tw'
    Zulu = 'zu'
