import requests
import os

def download_file(url, src):
    # faz requisição ao server e armazena na variável
    resposta = requests.get(url);
    if resposta.status_code == requests.codes.OK:
        with open(src,'wb') as new_file:    
            new_file.write(resposta.content)
            print("Download Finalizado, Salvo em {}".format(src))
            print(resposta.status_code)
    else: 
        resposta.raise_for_status()
        print("Deu erro, tio")

if __name__ == "__main__":
    BASE_URL = 'URL de um arquivo'
    OUTPUT_DIR = 'output'
    # for i in range (1, 25):
    nome_arquivo = os.path.join(OUTPUT_DIR, 'nome e formato do arquivo') # com FOR => 'aprendendo_{}'.format(i))
    # com FOR => download_file(BASE_URL .format(i), nome_arquivo )
    download_file(BASE_URL, nome_arquivo)