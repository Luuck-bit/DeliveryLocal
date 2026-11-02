def validar_parametros(demanda, capacidade):
    if demanda <= 0:
        raise ValueError("Erro: A demanda de pico por hora deve ser maior que zero.")
    if capacidade <= 0:
        raise ValueError("Erro: A capacidade da chapa por hora deve ser maior que zero.")
    return True