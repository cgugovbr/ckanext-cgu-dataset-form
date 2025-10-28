# ckanext-cgu-dataset-form

Extensão CKAN desenvolvida pela CGU para personalizar o formulário de criação e edição de datasets, adicionando campos específicos utilizados internamente pela CGU.

Esses campos são armazenados nos extras do dataset, mas foram incorporados diretamente no formulário para simplificar o preenchimento e garantir maior padronização das informações.

## **📦 Requisitos**

- CKAN ≥ 2.9
- Python 3.7 ou superior
- Acesso ao ambiente virtual onde o CKAN está instalado

### **⚙️ Instalação**

#### 1. Ativar o ambiente virtual do CKAN
```bash
. /usr/lib/ckan/default/bin/activate
```
>    Ajuste o caminho conforme o local onde o CKAN está instalado no seu ambiente (por exemplo, `/usr/lib/ckan/default`, `/opt/ckan/default`, etc.).

#### 2. Instalar o plugin a partir do repositório oficial
```bash
pip install --no-cache-dir 'ckanext-cgu-dataset-form[requirements] @ git+https://github.com/cgugovbr/ckanext-cgu-dataset-form.git'
```

#### 3. Configurar o CKAN
Edite o arquivo ckan.ini (geralmente em /etc/ckan/default/ckan.ini ou conforme o seu ambiente):

Adicione o plugin à lista de ckan.plugins:
```
ckan.plugins = cgu_dataset_form <outros_plugins>
```
Após executar todos os passos reinicie o ckan.

## 🧠 **Suporte**

Este plugin foi desenvolvido para uso interno da CGU, mas pode ser reutilizado por outros órgãos ou instâncias CKAN que precisem personalizar o formulário de datasets.

Em caso de dúvidas ou sugestões, abra uma issue no repositório:
https://github.com/cgugovbr/ckanext-cgu-dataset-form/issues