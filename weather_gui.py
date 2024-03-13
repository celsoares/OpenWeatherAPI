import PySimpleGUI as sg
import api_resquest as ar
import requests

from io import BytesIO

list_result=["guimaraes", "porto"]
layout=[[sg.Text("Cidade"), sg.Input("", key="city_search"), sg.Button("Pesquisar")],
        [sg.Table(key="resul_city", headings=["Cidade", "Pais", "Latitude", "Longitude"], values=[],visible=False)],
        [sg.Text(key="inf1"), sg.Image(key="ico")],
        [sg.Text(key="inf2")],
        [sg.Text(key="inf3")],
        [sg.Text(key="inf4")],
        [sg.Button("Sair"), sg.Button("Ver tempo")]



]


janela=sg.Window("API Tempo Real", layout)

while True:
    evento, valores =janela.read()

    
    print(evento, "--", valores,"--")
    

    if evento=="Pesquisar":

        aux=ar.procurar_cidade(valores["city_search"])
        
        janela["resul_city"].Update(values=aux)
        janela["resul_city"].Update(visible=True)

    if evento=="Ver tempo":
        try:
            valores_linha = janela["resul_city"].Get()[valores["resul_city"][0]]
            clima_actual=ar.current_weather(valores_linha[2], valores_linha[3])
            janela["inf1"].Update(f"Tempo:{clima_actual[0]}")
            janela["inf2"].Update(f"Descrição:{clima_actual[1]}")
            janela["inf3"].Update(f"Temperatura:{clima_actual[3]}ºC")
            janela["inf4"].Update(f"Humidade:{clima_actual[4]}%")

            img_resp=requests.get(f" http://openweathermap.org/img/wn/{clima_actual[2]}@2x.png")
            bytes_imagem = BytesIO(img_resp.content)
        # Atualiza o elemento da imagem com os bytes baixados
            janela["ico"].update(data=bytes_imagem.getvalue())
            # janela["ico"].Update(f" http://openweathermap.org/img/wn/{clima_actual[2]}@2x.png")
        

            print(clima_actual)
        except:
            sg.popup_ok("Tem que seleccionar uma cidade")
    if evento==sg.WIN_CLOSED or evento=="Sair":
        break
