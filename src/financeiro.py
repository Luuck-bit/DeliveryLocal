from src.config import CUSTO_NOVA_CHAPA, SALARIO_COZINHEIRO, LUCRO_MEDIO_LANCHE, HORAS_PICO_MES

def calcular_roi_expansao(dados_simulacao, chapas_adicionais=1, funcionarios_adicionais=1):
    perdidos_hora = dados_simulacao["perdidos_hora"]
    prejuizo_mensal = perdidos_hora * LUCRO_MEDIO_LANCHE * HORAS_PICO_MES

    investimento_equipamento = chapas_adicionais * CUSTO_NOVA_CHAPA
    custo_operacional_mensal = funcionarios_adicionais * SALARIO_COZINHEIRO
    investimento_total_inicial = investimento_equipamento + custo_operacional_mensal

    return {
        "prejuizo_mensal_atual": prejuizo_mensal,
        "investimento_inicial": investimento_total_inicial,
        "custo_mensal_equipe": custo_operacional_mensal
    }
