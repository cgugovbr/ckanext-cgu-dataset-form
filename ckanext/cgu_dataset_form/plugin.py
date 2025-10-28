from __future__ import annotations

from ckan.common import CKANConfig
from ckan.types import Schema

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

import logging


logger = logging.getLogger(__name__)

OBERVANCIAS_LEGAIS = {
        '1': 'Público',
        '2': 'Restrito - Direito Autoral (Lei nº 9.610/1998)',
        '3': 'Restrito - Informação Pessoal (Art. 31 da Lei nº 12.527/2011)',
        '4': 'Restrito - Propriedade Intelectual (software) (Lei nº 9.609/1998)',
        '5': 'Restrito - Protocolo pendente de análise de restrição (Art. 6º, III, da Lei nº 12.527/2011)',
        '6': 'Restrito - Restrição de Acesso a Documento Preparatório (Art. 7º, §3º, da Lei nº 12.527/2011)',
        '7': 'Restrito - Segredo de Justiça no Processo Civil (Art. 189 da Lei 13.105/2015)',
        '8': 'Restrito - Segredo de Justiça no Processo Penal (Art. 201, §6º, do Decreto-Lei 3.689/1941)',
        '9': 'Restrito - Segredo Industrial (Lei nº 9.279/1996)',
        '10': 'Restrito - Sigilo Comercial (Sociedades Anônimas) (Art. 155, § 2º da Lei nº 6.404/1976)',
        '11': 'Restrito - Sigilo Contábil (Art. 1.190 da Lei nº 10.406/2002)',
        '12': 'Restrito - Sigilo de nome, imagem, qualificação e demais info (Art. 5º, II da Lei 12.850/13)',
        '13': 'Restrito - Sigilo do Inquérito Policial (Art. 20 do Decreto-Lei 3.689/1941)',
        '14': 'Restrito - Sigilo do Procedimento Admin. Disciplinar em Curso (Art. 150 da Lei nº 8.112/1990)',
        '15': 'Restrito - Sigilo dos autos (Art. 7° da Resolução CNMP n° 23/2007)',
        '16': 'Restrito - Sigilo Empresarial (Art. 169 da Lei nº 11.101/2005)',
        '17': 'Restrito - Sigilo Funcional - SFC (Art. 26, §3º, da Lei nº 10.180/2001)',
        '18': 'Restrito - Sigilo por Possibilidade de Risco ou Dano (Art. 45 do Decreto nº 7.845/2012)',
        '19': 'Restrito - Sigilo Procedimento Admin. de Responsabilização (Art. 5º do Decreto nº 11.129/2022)',
        '20': 'Restrito - Sigilo Profissão do Advogado (Art. 7°, inciso II, da Lei n°11.767/2008)',
        '21': 'Sigiloso - Documento Preparatório - Sigiloso (Art. 7º, § 3º, da Lei nº 12.527/2001)',
        '22': 'Sigiloso - Informação Pessoal Sensível (Art. 31 da Lei nº 12.527/2011)',
        '23': 'Sigiloso - Reserva do Processo Ético (Art. 13 do Decreto nº 6.029/2007 e Art. 14 da Reso)',
        '24': 'Sigiloso - Segredo de Justiça no Processo Civil (Art. 189 da Lei 13.105/2015)',
        '25': 'Sigiloso - Segredo de Justiça no Processo Penal (Art. 201, §6º, do Decreto-Lei 3.689/1941)',
        '26': 'Sigiloso - Sigilo Bancário (Art. 1º da Lei Complementar nº 105/2001b)',
        '27': 'Sigiloso - Sigilo Fiscal (Art. 198, caput, da Lei nº 5.172/1966)',
        '28': 'Sigiloso - Sigilo de Acordo de Leniência (Art. 31, §1º, do Decreto nº 8.420/2015)',
        '29': 'Sigiloso - Sigilo de PAD em curso p/ servidores da CGU (Art. 150 da Lei nº 8.112/1990)',
        '30': 'Sigiloso - Sigilo do Inquérito Policial (Art. 20 do Decreto-Lei 3.689/1941)',
        '31': 'Sigiloso - Sigilo dos autos (Art. 7° da Resolução CNMP n° 23/2007)',
        '32': 'Sigiloso - Sigilo Funcional - SFC (Art. 26, §3º, da Lei nº 10.180/2001)',
        '33': 'Sigiloso - Sigilo Procedimento Administ. de Responsabilização (Art. 5º do Decreto nº 11.129/2022)',
        '34': 'Sigiloso - Sigilo Profissão de Advogado (Art. 7°, inciso II, da Lei n°11.767/2008)',
    }

PERIODICIDADES = {
    'DIARIA': 'Diária',
    'SEMANAL': 'Semanal',
    'QUINZENAL': 'Quinzenal',
    'MENSAL': 'Mensal',
    'TRIMESTRAL': 'Trimestral',
    'QUADRIMESTRAL': 'Quadrimestral',
    'SEMESTRAL': 'Semestral',
    'ANUAL': 'Anual',
    'SOB_DEMANDA': 'Sob Demanda',
    'OUTRAS': 'Outras',
}

OBJETIVOS_DESENVOLVIMENTO_SUSTENTAVEL = {
    '1': 'Erradicação da Pobreza',
    '2': 'Fome Zero e Agricultura Sustentável',
    '3': 'Saúde e Bem-Estar',
    '4': 'Educação de Qualidade',
    '5': 'Igualdade de Gênero',
    '6': 'Água Limpa e Saneamento',
    '7': 'Energia Limpa e Acessível',
    '8': 'Trabalho Decente e Crescimento Econômico',
    '9': 'Indústria, Inovação e Infraestrutura',
    '10': 'Redução das Desigualdades',
    '11': 'Cidades e Comunidades Sustentáveis',
    '12': 'Consumo e Produção Sustentáveis',
    '13': 'Ação contra a Mudança Global do Clima',
    '14': 'Vida na Água',
    '15': 'Vida Terrestre',
    '16': 'Paz, Justiça e Instituições Eficazes',
    '17': 'Parcerias e Meios de Implementação',
}

OPCOES_ESPACIAIS = {
    'FEDERAL': 'Federal',
    'ESTADUAL': 'Estadual',
    'MUNICIPAL': 'Municipal',
}

CAMPOS_CGU = [
    'periodicidade', 'coberturaTemporalInicio', 'coberturaTemporalFim', 'coberturaEspacial', 'valorCoberturaEspacial', 'granularidadeEspacial', 
    'atualizacaoVersao', 'descontinuado', 'dataDescontinuacao', 'observanciaLegal', 'dadosAbertos', 'relacaoOds', 'ods', 'dadosRacaEtnia', 'dadosGenero']

def periodicidades_helper():
    periodiciades = []
    for valor, nome in PERIODICIDADES.items():
        periodiciades.append({'text': nome, 'value': valor})
    return periodiciades

def periodicidades_label(value):
    try:
        return PERIODICIDADES[value]
    except KeyError:
        return ''

def observancias_legais():
    return OBERVANCIAS_LEGAIS

def label_observancia_legal(value):
    try:
        return OBERVANCIAS_LEGAIS[value]
    except KeyError:
        return ''

def objetivos_desenvolvimento_sustentavel_helper():
    return OBJETIVOS_DESENVOLVIMENTO_SUSTENTAVEL

def objetivos_desenvolvimento_sustentavel_label(value):
    try:
        return OBJETIVOS_DESENVOLVIMENTO_SUSTENTAVEL[value]
    except KeyError:
        return ''

def opcoes_espaciais_helper():
    opcoes = [{'text': '', 'value': ''}]
    for valor, nome in OPCOES_ESPACIAIS.items():
        opcoes.append({'text': nome, 'value': valor})
    return opcoes

def opcoes_espaciais_label(value):
    try:
        return OPCOES_ESPACIAIS[value]
    except KeyError:
        return ''

# converter que junta lista => string
def list_to_comma_string_converter(key, data, errors, context):
    """
    Converte listas, dicionários ou conjuntos em strings separadas por vírgula.
    Exemplo:
      ['a', 'b', 'c'] -> "a,b,c"
      {'1', '2'} -> "1,2"
      {'a': True, 'b': False} -> "a,b"
    """
    value = data.get(key)

    if value is None:
        return

    if isinstance(value, (list, set, tuple)):
        data[key] = ','.join(map(str, value))

    elif isinstance(value, dict):
        data[key] = ','.join(map(str, value.keys()))

    elif isinstance(value, str):
        # Já é string, não faz nada
        return

    else:
        # Força pra string (só pra garantir)
        data[key] = str(value)


def debug(value):
    logger.debug('#################### LOG ##########################')
    logger.debug(value)
    logger.debug('#################### FIM ##########################\n\n')

class CguDatasetFormPlugin(
        tk.DefaultDatasetForm,
        plugins.SingletonPlugin,
):

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=False)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)
    
    def _remove_cgu_extras(self, extras: list):
        result = []
        for item in extras:
            if item['key'] not in CAMPOS_CGU:
                result.append(item)
        return result
    
    def _get_extra(self, extras: list, key: str, default = None):
        for item in extras:
            if item['key'] == key:
                return item['value']
        return default

    def update_config(self, config: CKANConfig):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    def get_helpers(self):
        return {
            'periodicidades': periodicidades_helper,
            'periodicidades_label': periodicidades_label,
            'observancias_legais': observancias_legais ,
            'label_observancia_legal': label_observancia_legal,
            'objetivos_desenvolvimento_sustentavel': objetivos_desenvolvimento_sustentavel_helper,
            'objetivos_desenvolvimento_sustentavel_label': objetivos_desenvolvimento_sustentavel_label,
            'opcoes_espaciais': opcoes_espaciais_helper,
            'opcoes_espaciais_label': opcoes_espaciais_label,
            'cgu_dataset_form_remove_extras': self._remove_cgu_extras,
            'cgu_dataset_form_get_extra': self._get_extra,
        }

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self) -> list[str]:
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def _modify_package_schema(self, schema: Schema):
        schema.update({
                'periodicidade': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ],
                'coberturaTemporalInicio': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ],
                'coberturaTemporalFim': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ],
                'coberturaEspacial': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ],
                'valorCoberturaEspacial': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ],
                'granularidadeEspacial': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ],
                'atualizacaoVersao': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ],
                'descontinuado': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')
                ],
                'dataDescontinuacao': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras'),
                ],
                'observanciaLegal': [
                    list_to_comma_string_converter,
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras'),
                ],
                'dadosAbertos': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras'),
                ],
                'relacaoOds': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras'),
                ],
                'ods': [
                    list_to_comma_string_converter,
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras'),
                ],
                'dadosRacaEtnia': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras'),
                ],
                'dadosGenero': [
                    tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras'),
                ],
            })
        # Add our custom_test metadata field to the schema, this one will use
        return schema

    def create_package_schema(self):
        schema: Schema = super(
            CguDatasetFormPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema: Schema = super(
            CguDatasetFormPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
