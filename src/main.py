from src.config import DEMANDA_PICO_HORA, CAPACIDADE_CHAPA_HORA
from src.simulador import analisar_gargalo
from src.financeiro import calcular_roi_expansao
from src.relatorio import gerar_cabecalho, gerar_rodape
from src.validador import validar_parametros

def executar_sistema():
    validar_parametros(DEMANDA_PICO_HORA, CAPACIDADE_CHAPA_HORA)

    gerar_cabecalho()

    atual = analisar_gargalo(num_chapas=1)
    fin_atual = calcular_roi_expansao(atual)
    print("\n[CENÁRIO ATUAL - 1 Chapa]")
    print(f"• Capacidade: {atual['capacidade_hora']} ped/h | Pedidos Perdidos: {atual['perdidos_hora']} ped/h")
    print(f"• Prejuízo Mensal Estimado: R$ {fin_atual['prejuizo_mensal_atual']:,.2f}")

    ideal = analisar_gargalo(num_chapas=3)
    fin_ideal = calcular_roi_expansao(ideal, chapas_adicionais=2, funcionarios_adicionais=2)
    print("\n[CENÁRIO PROPOSTO - 3 Chapas]")
    print(f"• Nova Capacidade: {ideal['capacidade_hora']} ped/h ({ideal['taxa_sucesso']:.1f}% atendidos)")
    print(f"• Investimento Inicial: R$ {fin_ideal['investimento_inicial']:,.2f}")

    gerar_rodape()

if __name__ == "__main__":
    executar_sistema()
