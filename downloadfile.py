import requests
import os
import argparse

def DownloadFile(url, local):
    nome_arquivo = os.path.join(local, url.split('/')[-1])
    with requests.get(url, stream=True) as resposta:
        resposta.raise_for_status()
        with open(nome_arquivo, 'wb') as file:
            for pedaco in resposta.iter_content(chunk_size=8096):
                file.write(pedaco)
                file.flush()
                os.fsync(file.fileno())

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="digite a url que você deseja fazer download")
parser.add_argument("--filepath", help="digite o local que você deseja salvar")
args = parser.parse_args()
DownloadFile(args.url, args.filepath)