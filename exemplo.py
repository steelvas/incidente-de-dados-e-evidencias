"""Triagem didática. A avaliação jurídica do risco é humana."""

def triagem(afetou_dados_pessoais, risco_relevante):
    acoes = ["Registrar cronologia e preservar evidências"]
    if afetou_dados_pessoais and risco_relevante:
        acoes.append("Acionar avaliação de comunicação pelo controlador")
    return acoes


if __name__ == "__main__":
    for acao in triagem(True, True):
        print(acao)
    assert len(triagem(True, True)) == 2
    assert len(triagem(True, False)) == 1
