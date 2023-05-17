'''modulo para efetuar pings'''
import os


def ping_host_lote(filepath: str, encoding='utf-8', saltos=2):
    '''principal para efetuar os PINGs multiplos

    Arguments:
    -- filepath: string apontando o caminho do arquivo contendo ips
    -- encoding: tipo de encoding para leitura do arquivo
    -- saltos: quantas vezes vai pingar
    '''
    with open(filepath, encoding=encoding) as file:
        dump = file.read()
        dump = dump.splitlines()

        for ip in dump:
            print('-' * 80, f'\npingando em {ip}')
            os.system(f'ping -n {saltos} {ip}')

    print('-' * 80)
