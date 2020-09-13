import pyowm
import datetime
from pycbrf.toolbox import ExchangeRates
city_friends={'Ваня':'Москва', 'Сергей':'Смоленск', 'Любомир':'Тверь'}
print('Джаспер: как вас зовут?')
user=str(input())
print(f'Джаспер: очень приятно познакомиться, {user}')
print('Джаспер: Я вас слушаю')
query_in=str(input())
query=query_in.split(', ')
if query[0]== 'Джаспер':
    if query[1]=='как дела?':
        print('Джаспер: всё хорошо')
    if query[1]=='привет':
        print('Джаспер: привет')
    if query[1]=='какая погода?':
        print('Джаспер: Какой город Вас интересует?')
        try:
            city=str(input())
            owm = pyowm.OWM('a99967bc9ee70d5b4bd387902982f400', language = "RU")
            observation = owm.weather_at_place(city)
            w = observation.get_weather()
            temperature = w.get_temperature('celsius')['temp']
            temperature1 = round(temperature)
            humi = w.get_humidity()
            windSpeed = w.get_wind()['speed']
            status = w.get_detailed_status()
            print('Джаспер: Сейчас в городе ' + city + ' +' + str(temperature1) + ' по цельсию')
            print('Джаспер: Влажность ' + str(humi))
            print('Джаспер: Скорость ветра ' + str(windSpeed) + ' метра в секунду')
            print('Джаспер: ' + str(status))
        except:
            print('Джаспер: такого города не существует') 
    if query[1]=='в каких городах живут мои друзья?':
        for city in city_friends.values():
           print(city, end=', ')
        print()
    if query[1]=='курс доллара':
        now = datetime.datetime.now()
        rates = ExchangeRates(str(now.strftime("%Y-%m-%d")), locale_en=True)
        kurs=int(rates['USD'].rate)
        if kurs%10==1:
            rubl='рубль'
        elif kurs%10==2 or kurs%10==3 or kurs%10==4:
            rubl='рубля'
        else:
            rubl='рублей'
        print(f'курс доллара на {now.strftime("%d-%m-%Y")} равен {kurs} {rubl}' )
    if query[1]=='кто я?':
        print(f'Джаспер: {user}')



        








