# Projeto: Pacote de Seguranca da Informacao

Projeto ideação para pratica do Bootcamp Python no modulo "Descomplicando a criação de pacotes de processamento de imagens em Python" ministrado por Karina Kato através da plataforma Digital Innovation One - DIO.

## Descrição

O pacote "seginfo-tools" é usado para:

- Módulo "Processing":
  - Realizar Multiplos Pings em Hosts ou Endereço de IPv4;

- Módulo "Utils":
  - Calcular Subnets;
  - Calcular IPs;

---------------------------------------------

## Passo a passo da configuração para hospedar um pacote em Python Test do Pypi

- [x] Upgrade do pip
- [x] instalação do twine
- [x] Instalação das últimas versões de "setuptools" e "wheel"

```bash
python -m pip install --user twine
py -m pip install --user --upgrade setuptools wheel
```

- [x] Tenha certeza que o diretório no terminal seja o mesmo do arquivo "setup.py"

```bash
/home/user/workspace/seginfo-tools-package> py setup.py sdist bdist_wheel
```

- [x] Após completar a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:
  - [x] build;
  - [x] dist;
  - [x] seginfo-tools.egg-info.

- [x] Basta subir os arquivos, usando o Twine, para o Test Pypi:

```bash
py -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

- [x] Após rodar o comando acima no terminal, será pedido para inserir o usuário e senha. Feito isso, o projeto estará hospedado no Test Pypi.

- [x] Instalação de dependências

```bash
pip install -r requirements.txt
```

## Author do projeto base

- [x] Instalção do Pacote Teste

Use o gerenciador de pacotes ```pip install``` para instalar seginfo-tools

```bash
pip install -i https://test.pypi.org/simple/ seg-info-tools
```

## Author

[guruck](https://github.com/guruck)

## License

[MIT](https://choosealicense.com/licenses/mit/)
