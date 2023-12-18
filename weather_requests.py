import requests

params = {"access_key": "03f637409974d3bd297d1d269e4a87f8", "query": "Moscow"}
def get_weather():
    global params
    
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    grad = api_response['current']['temperature']
    
    send = []
    send.append("Сейчас в Москве " + str(grad) + skl(abs(grad)) + ", cкорость ветра " + str(api_response['current']['wind_speed'])+" м/c")
    send.append("Влажность " + str(api_response['current']['humidity']) +"%")
    return send

def skl(x) :
    f1 = lambda a: (a%100)//10 != 1 and a%10 == 1
    f2 = lambda a: (a%100)//10 != 1 and a%10 in [2,3,4]
    return " градус" if f1(x) else  " градуса" if f2(x) else " градусов"

