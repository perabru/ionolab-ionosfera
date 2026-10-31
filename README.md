<div align="center">

![IonoLab — briefing técnico](docs/banner.svg)

**O céu muda. O sinal também.**

HTML independente · 23 telas · 17 blocos tecnológicos · Fontes incorporadas

[Abrir o HTML](index.html) · [Telas](docs/telas.md) · [Stack](docs/tecnologias.md) · [Arquitetura](docs/arquitetura.md)

</div>

## O projeto

Python para detectar blobs e bubbles em imagens do INPE, estimar sua evolução espacial e explicar as evidências com LLMs.

> Prever ocorrência/localização de realces e depleções ópticas validados, não medir densidade absoluta a partir do brilho nem garantir interrupção de comunicação. Análise de efeitos depende de dados GNSS/radio complementares.

Este repositório contém o **briefing técnico navegável e suas demonstrações locais**. As integrações de produção descritas no projeto são o escopo de desenvolvimento, sem servidor compartilhado ou credenciais nesta versão.

## Experimente agora

1. Baixe o repositório em **Code → Download ZIP** ou clone com o comando abaixo.
2. Abra `index.html` no navegador.
3. Explore as telas, filtre a stack e teste a simulação identificada.
4. Use **Imprimir / salvar PDF** para obter a especificação completa, ou exporte o briefing em JSON.

```bash
git clone https://github.com/perabru/ionolab-ionosfera.git
cd ionolab-ionosfera
```

O arquivo inclui HTML, CSS, JavaScript, fontes e recursos visuais. Não exige instalação, `npm install`, chave de API ou internet para navegar. Os links da documentação oficial exigem conexão.

## O que está disponível

| Recurso | Esta versão |
| --- | --- |
| Inventário de telas | Busca, filtros, objetivo, campos, ações, estados, API e aceite |
| Tecnologias | Responsabilidade, local de uso, contrato e documentação |
| Método | Equações e demonstração com dados locais ou sintéticos |
| Entrega | Responsáveis, testes, pendências e sequência de implementação |
| Impressão | Anexo completo de telas, mesmo com filtro ativo |
| Serviço de produção | Especificado; depende de implementação e homologação |

## Tipografia e identidade

| Papel | Família | Intenção |
| --- | --- | --- |
| Títulos e marca | **Space Grotesk** | Hierarquia científica com letras desenhadas para facilitar a distinção. |
| Texto e controles | **Atkinson Hyperlegible Next** | Leitura mais confortável em parágrafos, listas e botões. |
| Código e medidas | **JetBrains Mono** | Alinhamento de valores, rotas e equações. |

As fontes são incorporadas no HTML em WOFF. Textos, controles e rótulos receberam tamanhos maiores e mais espaço entre linhas. Os avisos SIL OFL acompanham o projeto em [créditos de terceiros](THIRD_PARTY_NOTICES.md).

## Percurso principal

1. **Importar:** Sequências all-sky e metadados.
2. **Qualificar:** Nuvens, Lua, exposição e calibração.
3. **Detectar:** Máscaras revisadas e rastreamento.
4. **Prever:** Baseline e modelo temporal comparados.
5. **Explicar:** Relatório com evidências e limitações.

## Telas por área

| Área | Telas |
| --- | ---: |
| Público | 1 |
| Pesquisa | 17 |
| Gestão | 2 |
| Conta | 3 |
| **Total** | **23** |

[Consultar todas as telas e critérios de aceite →](docs/telas.md)

## Quem participa

| Área | Responsabilidade |
| --- | --- |
| Computação | Python, ingestão, detector, previsor, API e testes. |
| Orientação / aeronomia | Definir fenômeno, calibração, rótulos e interpretação. |
| Dados / validação | Noites e estações, split, baseline, incerteza e métricas. |
| Pesquisa e redação | Pergunta, método, referências e relatório de TCC reproduzível. |

## Critérios do piloto

- [ ] Noites do teste não aparecem em janelas de treino.
- [ ] Quadro nublado não vira falso bubble sem sinalização.
- [ ] Relatório LLM reproduz apenas métricas presentes no pacote.
- [ ] Previsão vencida deixa de aparecer como previsão atual.

Os itens descrevem testes da aplicação final. Marcar o checklist do briefing registra leitura local e não comprova a implementação.

## Decisões abertas

- Confirmar estações, licença, frequência e acesso aos dados INPE.
- Definir calibração, referência científica e protocolo de anotação.
- Escolher unidade da matriz, horizontes e critério mínimo de ganho sobre persistência.

## Organização do repositório

| Caminho | Conteúdo |
| --- | --- |
| [`index.html`](index.html) | Briefing completo e independente |
| [`docs/telas.md`](docs/telas.md) | Inventário das telas |
| [`docs/tecnologias.md`](docs/tecnologias.md) | Stack proposta e fontes |
| [`docs/arquitetura.md`](docs/arquitetura.md) | Fluxo e dados do domínio |
| [`docs/banner.svg`](docs/banner.svg) | Identidade aplicada ao README |
| [`font-licenses/`](font-licenses/) | Licenças das fontes incorporadas |
| [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) | Créditos e limites de licenciamento |

## Validação desta entrega

- Sintaxe dos scripts e integridade dos recursos incorporados.
- Referências entre telas e tecnologias.
- Navegação e tipografia verificadas na prévia do navegador.
- Preservação das demonstrações e dos critérios do briefing anterior.

---

<div align="center">

**IonoLab** · Projeto de [Bruno Michel Pera](https://github.com/perabru)

Briefing técnico · Documentação em português · 2026

</div>
