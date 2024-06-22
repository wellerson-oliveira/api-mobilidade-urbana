import pandas as pd

MAP_COLS = {'Embreagues': 'embreagues',
            'Idade': 'idade',
            ' condutor': 'condutor',
            ' cod_severidade': 'cod_severidade',
            ' desc_severidade': 'desc_severidade',
            ' data_hora_boletim': 'data_hora_boletim',
            ' Nº_envolvido': 'numero_envolvido',
            ' sexo': 'sexo',
            ' cinto_seguranca': 'cinto_seguranca',
            ' Embreagues': 'embreagues',
            ' Idade': 'idade',
            ' nascimento': 'nascimento',
            ' categoria_habilitacao': 'categoria_habilitacao',
            ' descricao_habilitacao': 'descricao_habilitacao',
            ' declaracao_obito': 'declaracao_obito',
            ' cod_severidade_antiga': 'cod_severidade_antiga',
            ' pedestre': 'pedestre',
            ' passageiro': 'passageiro',
            'Nº_boletim': 'num_boletim'}


def process_data(data: list[dict]):
    df_final = pd.DataFrame()

    for item in data:
        df = item.get("data")
        df.rename(columns=MAP_COLS, inplace=True)
        df['ano'] = item.get("id").replace("si_env-", "")

        #
        df['num_boletim'] = df['num_boletim'].astype(str)

        df_final = pd.concat([df_final, df], axis=0)

    df_final = df_final.drop(columns=' ')
    return df_final
