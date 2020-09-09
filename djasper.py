#Теперь Джаспер по запросу сообщает время.

import pyowm 
import datetime 
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
    if query[1]=='который час?': 
        now = datetime.datetime.now() 
        if int(now.strftime("%H"))==0 or 4<int(now.strftime("%H"))<21: 
        hour='часов' 
        elif 1<int(now.strftime("%H"))<6 or 21<int(now.strftime("%H"))<24 : 
        hour='часа' 
        elif int(now.strftime("%H"))==1 or int(now.strftime("%H"))==21: 
        hour='час' 
        if int(now.strftime("%M"))%10==1: 
        minuta='минута' 
        elif int(now.strftime("%M"))%10==2 or int(now.strftime("%M"))%10==3 or                          int(now.strftime("%M"))%10==4: 
        minuta='минуты' 
    else: 
        minuta='минут' 
        print(f'сейчас {now.strftime("%H")} {hour} {now.strftime("%M")} {minuta}')
        
            
            
          



