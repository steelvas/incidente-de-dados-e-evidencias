# Vazaram dados: apagar os vestígios resolve?

Uma empresa identifica acesso indevido a dados pessoais. Restaurar o serviço é necessário, mas não substitui a apuração.

```python
incidente = {
    "afetou_dados_pessoais": True,
    "risco_relevante": True
}

if incidente["afetou_dados_pessoais"]:
    print("Registrar o que ocorreu e preservar evidências")

if incidente["risco_relevante"]:
    print("Acionar a avaliação de comunicação")
```

1. **Código:** o primeiro resultado trata da documentação do incidente. O segundo depende de uma avaliação concreta do risco; a variável não se preenche sozinha.
2. **Fundamento:** o controlador deve comunicar à ANPD e aos titulares o incidente que possa causar risco ou dano relevante. A regra geral de comunicação é de **três dias úteis**, contados do conhecimento de que dados pessoais foram afetados, ressalvados prazos específicos.
3. **O que fazer:** registrar cronologia, dados envolvidos, medidas de contenção, avaliação de risco e motivo da decisão de comunicar ou não. A regulamentação exige guardar o registro do incidente, inclusive o não comunicado, por pelo menos cinco anos.

**Papel do advogado:** conectar investigação técnica, direitos das pessoas afetadas e decisão documentada da empresa.

Fontes: [ANPD — comunicação de incidentes](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis) e [Resolução CD/ANPD nº 15/2024](https://bibliotecadigital.mj.gov.br/bitstream/1/12879/2/RES_ANPD_2024_15.html).

## Executar o exemplo

Com Python 3 instalado, rode `python exemplo.py`. O arquivo usa apenas dados fictícios e inclui verificações simples com `assert`. Ele não substitui a análise jurídica nem executa ações externas.


*Exemplo didático. A classificação de risco depende dos fatos e da norma aplicável.*
