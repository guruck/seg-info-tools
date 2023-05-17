'''modulo para discovey de IPs'''
import ipaddress


def teste_host(ip: str, saltos=2):
    '''principal para efetuar os saltos nos IP calculando proximos

    Arguments:
    -- ip: string apontando o caminho do arquivo contendo ips
    -- encoding: tipo de encoding para leitura do arquivo
    -- saltos: quantas vezes vai pingar
    '''
    endereco = ipaddress.ip_address(ip) + saltos
    print(ip, f'+ {saltos} => ', endereco)


def teste_rede(endereco_ip: str, subnet=28):
    '''principal para efetuar os calculos de subnet nos IP calculando

    Arguments:
    -- ip: string apontando o caminho do arquivo contendo ips
    -- encoding: tipo de encoding para leitura do arquivo
    -- saltos: quantas vezes vai pingar
    '''
    ip = f'{endereco_ip}/{subnet}'
    rede = ipaddress.ip_network(ip, strict=False)
    print(f'o ip {ip} está na rede: {rede}')
    for ip in rede:
        print(ip)
