import requests
from googletrans import Translator

# API key do OpenWeatherMap
api_key = "55ba8eb8f02b9c557e220b90281f7c2b"
#api_key = "6511c686f65239465d634cc91a535492"

def procurar_cidade(city):

    url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={10}&appid={api_key}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        result=[]

        
        for x in dados:
            linha=[]
            linha.append(x["name"])
            linha.append(x["country"])
            linha.append(x["lat"])
            linha.append(x["lon"])

            result.append(linha)

        return result
    
    else:
        return -1
    
def current_weather(latitude, longitude):

    # url=f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={api_key}"
    # url=f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={api_key}"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric&lang=pt"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        tipos={"Clouds":"Nuvens",
               "Clear":"Céu Limpo",
               "Atmosphere":"Nevoeiro",
               "Snow":"Neve",
               "Rain":"Chuva",
               "Rain":"Chuvisco",
               "Thunderstorm":"Tempestade"
                }
        

        result=[]
       

        result.append(tipos[dados["weather"][0]["main"]])
        result.append(dados["weather"][0]["description"])
        result.append(dados["weather"][0]["icon"])

        result.append(dados["main"]["temp"])
        result.append(dados["main"]["humidity"])
        


        
        print(result)
        return result
    else:
        return -1

if __name__=="__main()":
    # print(procurar_cidade("guimaraes"))
            
    current_weather(41.4417677, -8.2955712)