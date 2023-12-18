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

