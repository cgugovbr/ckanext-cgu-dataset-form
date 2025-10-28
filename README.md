# ckanext-cgu-dataset-form

Extensão CKAN desenvolvida pela CGU para personalizar o formulário de criação e edição de datasets.

## **📦 Requisitos**

- CKAN ≥ 2.9
- Python 3.7 ou superior
- Acesso ao ambiente virtual onde o CKAN está instalado

### ⚙️ **Instalação — Passo 1: Clonar o repositório**

Dentro do ambiente do CKAN, execute:
```bash
cd /usr/lib/ckan/src
git clone https://github.com/cgugovbr/ckanext-cgu-dataset-form.git
```

### ⚙️ **Instalação — Passo 2: Instalar a extensão**

Entre na pasta do plugin e instale no ambiente virtual do CKAN:
```bash
cd ckanext-cgu-dataset-form
pip install -e .
```

### ⚙️ **Instalação — Passo 3: Configurar o CKAN**

Edite o arquivo ckan.ini (geralmente em /etc/ckan/default/ckan.ini ou conforme o seu ambiente):

Adicione o plugin à lista de ckan.plugins:
```
ckan.plugins = cgu_dataset_form <outros_plugins>
```

## 🧠 **Suporte**

Este plugin foi desenvolvido para uso interno da CGU, mas pode ser reutilizado por outros órgãos ou instâncias CKAN que precisem personalizar o formulário de datasets.

Em caso de dúvidas ou sugestões, abra uma issue no repositório:
https://github.com/cgugovbr/ckanext-cgu-dataset-form/issues


## 📄 Licença

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
