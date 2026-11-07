from src.config import
DEMANDA_PICO_HORA
CAPACIDADE_CHAPA_HORA

def analisar_gargalo(num_chapas):
    capacidade_total = num_chapas * CAPACIDADE_CHAPA_HORA
    pedidos_atendidos = min(DEMANDA_PICO_HORA, capacidade_total)
    pedidos_perdidos = max(0, DEMANDA_PICO_HORA - capacidade_total)
    taxa_atendimento = (pedidos_atendidos / DEMANDA_PICO_HORA) * 100

    return{
        "chapas": num_chapas
        "capacidade_hora": capacidade_total
        "atendidos_hora": pedidos_atendidos
        "pedidos_hora": pedidos_perdidos
        "taxa_sucesso": taxa_atendimento 
    } 