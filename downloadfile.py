import requests
import os

def DownloadFile(url, local_filename):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as resposta:
        resposta.raise_for_status()
        with open(local_filename, 'wb') as file:
            for pedaco in resposta.iter_content(chunk_size=8096):
                file.write(pedaco)
                file.flush()
                os.fsync(file.fileno())
    return local_filename


if __name__ == "__main__":
    # Descomentar e colocar uma URL aqui =P
    # BASE_URL = 'COLOCAR UMA URL AQUI'
    OUTPUT_DIR = 'output'
    nome_arquivo = os.path.join(OUTPUT_DIR, 'bkp_mensageria.gz')
    DownloadFile(BASE_URL, nome_arquivo)