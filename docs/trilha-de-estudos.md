# Trilha de estudos - IonoLab

Da imagem ao experimento de previsão.

Fevereiro a julho de 2027. 86 horas estimadas de leitura e prática; não é a estimativa total do produto. O progresso fica no navegador e tem backup próprio na aba Trilha de estudos.

[Baixar kit de exercícios](../materiais/kit-estudos-ionolab.zip)

## E01 - Relacionar plasma, imagem e comunicação

2027-02-01 a 2027-02-07 | 8 h | Base

Base recomendada: início da trilha.

**Aprender:** Bolha e intensificação; Aeroluminescência; Emissão; Cintilação; Limites de interpretação.

**Prática:** Fichar a instrumentação do INPE e separar observação óptica, indicador GNSS e hipótese de impacto.

**Conferir:**
- [ ] Grandeza observada identificada
- [ ] Fonte da imagem
- [ ] Limites descritos

**Fontes:**
- [INPE: imageador de aeroluminescência](https://www2.inpe.br/climaespacial/AGCImagerViewer/faces/about.xhtml?lan=pt) - INPE / EMBRACE | PT-BR | Leitura gratuita. Entender emissão, campo de visão, filtros e contexto das imagens.
- [Cintilação ionosférica](https://www.spaceweather.gov/phenomena/ionospheric-scintillation) - NOAA / SWPC | EN | Leitura gratuita. Contextualizar cintilação e propagação de sinais.
- [Pro Git em português](https://git-scm.com/book/pt-br/v2) - Git / autores do Pro Git | PT-BR | Leitura gratuita. Commits, branches, revisão e recuperação do trabalho.

Entregas: P01, P02.

Arquivos: [protocolo_experimento.md](../materiais/protocolo_experimento.md).

## E02 - Preparar Python, arrays e tempo UTC

2027-02-08 a 2027-02-21 | 12 h | Base

Base recomendada: E01.

**Aprender:** Python; NumPy; Arrays; Dimensões; UTC e manifesto.

**Prática:** Ler os frames CSV sintéticos, ordenar por UTC e registrar origem, estação demonstrativa e licença do conjunto real futuro.

**Conferir:**
- [ ] Sequência ordenada
- [ ] Origem registrada
- [ ] Teste separado por noite

**Fontes:**
- [Tutorial oficial de Python](https://docs.python.org/pt-br/3/tutorial/) - Python Software Foundation | PT-BR | Leitura gratuita. Funções, arquivos, exceções, módulos e ambientes. Para quem já conhece lógica.
- [NumPy para começar](https://numpy.org/doc/stable/user/absolute_beginners.html) - NumPy | EN | Leitura gratuita. Arrays, eixos, máscaras e operações vetorizadas.
- [Xarray: dados multidimensionais](https://docs.xarray.dev/en/stable/) - Xarray | EN | Leitura gratuita. Dimensões nomeadas, tempo UTC, coordenadas e séries de imagens.

Entregas: P02, P03, P04.

Arquivos: [frames_demo.csv](../materiais/frames_demo.csv), [manifesto_demo.json](../materiais/manifesto_demo.json).

## E03 - Pré-processar e segmentar imagens

2027-02-22 a 2027-03-07 | 12 h | Aplicação

Base recomendada: E02.

**Aprender:** Máscaras; Nuvens; Limiar; Morfologia; Rotulagem.

**Prática:** Comparar segmentações em uma amostra anotada e registrar o que foi removido pela máscara de qualidade.

**Conferir:**
- [ ] Máscara guardada
- [ ] Limiar documentado
- [ ] Rótulos revisados

**Fontes:**
- [OpenCV: módulos e tutoriais](https://docs.opencv.org/4.x/) - OpenCV | EN | Leitura gratuita. Pré-processamento, máscaras, segmentação e fluxo óptico.
- [NumPy para começar](https://numpy.org/doc/stable/user/absolute_beginners.html) - NumPy | EN | Leitura gratuita. Arrays, eixos, máscaras e operações vetorizadas.

Entregas: P04, P05.

Arquivos: [frames_demo.csv](../materiais/frames_demo.csv), [avaliar.py](../materiais/avaliar.py).

## E04 - Prever a partir de um baseline verificável

2027-03-08 a 2027-03-28 | 12 h | Aplicação

Base recomendada: E03.

**Aprender:** Persistência; Advecção; Horizonte; Treino e teste; Emissão e validade.

**Prática:** Executar a persistência do último frame e avaliar no frame seguinte. Comparar uma proposta posterior no mesmo conjunto.

**Conferir:**
- [ ] Sem acesso ao futuro
- [ ] Horizonte explícito
- [ ] Baseline preservado

**Fontes:**
- [NumPy para começar](https://numpy.org/doc/stable/user/absolute_beginners.html) - NumPy | EN | Leitura gratuita. Arrays, eixos, máscaras e operações vetorizadas.
- [Xarray: dados multidimensionais](https://docs.xarray.dev/en/stable/) - Xarray | EN | Leitura gratuita. Dimensões nomeadas, tempo UTC, coordenadas e séries de imagens.
- [PyTorch: conceitos básicos](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) - PyTorch | EN | Leitura gratuita. Tensores, treino e avaliação. Estudar depois de validar o baseline.

Entregas: P07, P08, P09.

Arquivos: [prever_persistencia.py](../materiais/prever_persistencia.py), [frames_demo.csv](../materiais/frames_demo.csv).

## E05 - Calcular matriz de confusão e incerteza

2027-03-29 a 2027-04-18 | 10 h | Aplicação

Base recomendada: E04.

**Aprender:** TP e TN; FP e FN; Precisão; Recall; F1 e IoU.

**Prática:** Recalcular a matriz do CSV e mostrar como o limiar muda os erros. Relatar suporte e unidade de avaliação.

**Conferir:**
- [ ] Matriz recalculável
- [ ] Suporte indicado
- [ ] Limiar declarado

**Fontes:**
- [Métricas e avaliação de modelos](https://scikit-learn.org/stable/modules/model_evaluation.html) - scikit-learn | EN | Leitura gratuita. Matriz de confusão, precisão, revocação, F1 e métricas conforme o alvo.
- [OpenCV: módulos e tutoriais](https://docs.opencv.org/4.x/) - OpenCV | EN | Leitura gratuita. Pré-processamento, máscaras, segmentação e fluxo óptico.

Entregas: P09, P10.

Arquivos: [avaliar.py](../materiais/avaliar.py), [rotulos_demo.csv](../materiais/rotulos_demo.csv).

## E06 - Usar LLM para explicar evidências

2027-04-19 a 2027-05-16 | 10 h | Aplicação

Base recomendada: E05.

**Aprender:** Pacote de evidências; JSON; Validação de números; Abstenção; Proveniência.

**Prática:** Produzir uma síntese que cite apenas métricas calculadas e recuse uma conclusão sem cobertura observacional.

**Conferir:**
- [ ] JSON válido
- [ ] Números conferidos
- [ ] Incerteza preservada

**Fontes:**
- [Ollama: saída estruturada](https://docs.ollama.com/capabilities/structured-outputs) - Ollama | EN | Leitura gratuita. Respostas em esquema JSON e validação da síntese das evidências.
- [Tutorial oficial de Python](https://docs.python.org/pt-br/3/tutorial/) - Python Software Foundation | PT-BR | Leitura gratuita. Funções, arquivos, exceções, módulos e ambientes. Para quem já conhece lógica.

Entregas: P12, P13.

Arquivos: [evidencias_demo.json](../materiais/evidencias_demo.json).

## E07 - Publicar mapa observado e previsto

2027-05-17 a 2027-05-30 | 12 h | Validação

Base recomendada: E06.

**Aprender:** Georreferenciamento; MapLibre; API; Rastreabilidade; Experimento reproduzível.

**Prática:** Mostrar lado a lado origem observada, emissão, horizonte e validade da previsão. Executar de novo o pacote de teste.

**Conferir:**
- [ ] Observado e previsto identificados
- [ ] Cobertura visível
- [ ] Reexecução documentada

**Fontes:**
- [MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/) - MapLibre | EN | Leitura gratuita. Mapas interativos, camadas, legendas e GeoJSON.
- [FastAPI: tutorial guiado](https://fastapi.tiangolo.com/tutorial/) - FastAPI | EN | Leitura gratuita. Rotas, validação, dependências e respostas de API.
- [Playwright: primeiros testes](https://playwright.dev/docs/intro) - Playwright / Microsoft | EN | Leitura gratuita. Testes do percurso do usuário e evidências de falha.

Entregas: P14, P15, P16, P18.

Arquivos: [manifesto_demo.json](../materiais/manifesto_demo.json), [protocolo_experimento.md](../materiais/protocolo_experimento.md).

## E08 - Transformar evidências em monografia e artigo

2027-06-01 a 2027-07-16 | 10 h | Validação

Base recomendada: E07.

**Aprender:** Busca e fichamento; Método reproduzível; Figuras e tabelas; Citações e referências; Modelo INIC.

**Prática:** Preencher a matriz de referências, redigir um resultado sustentado pelos dados e fechar o primeiro texto integral do artigo em junho.

**Conferir:**
- [ ] Cada número tem origem
- [ ] Referências revisadas
- [ ] Modelo do evento conferido

**Fontes:**
- [Zotero: guia inicial](https://www.zotero.org/support/quick_start_guide) - Zotero | EN | Leitura gratuita. Coleções, metadados, citações e biblioteca compartilhada.
- [Normas e guias de normalização](https://biblioteca.ufes.br/normalizacao) - Sistema Integrado de Bibliotecas / UFES | PT-BR | Leitura gratuita. Conferir normas de apresentação, citações, referências e resumos.
- [INIC: modelo e submissão](https://www.univap.br/inic/submissao_trabalhos.php) - UNIVAP / INIC | PT-BR | Leitura gratuita. Consultar o modelo da edição de 2027 quando divulgado. A consulta atual identifica 2026.

Entregas: M08, M13, M15, A01, A05, A09.

Arquivos: [matriz_referencias.csv](../materiais/matriz_referencias.csv), [protocolo_experimento.md](../materiais/protocolo_experimento.md).

## Hardware e recursos de bancada

| Item | Quantidade | Uso | Etapa / observação |
| --- | --- | --- | --- |
| Computador com Python | 1 | Pré-processamento e modelos de referência | Essencial. 8 a 16 GB como referência de exercícios pequenos; medir custo do conjunto real. |
| Armazenamento para imagens e metadados | 1 | Preservar originais, máscaras e resultados | Essencial.  |
| Acesso ao conjunto do INPE | Conforme disponibilidade | Dados e contexto de instrumentação | Essencial. Confirmar acesso, termos e produto por estação; não há API pública presumida. |
| GPU compatível com o framework | 1 | Experimentos posteriores de deep learning | Opcional. Persistência e os exercícios iniciais funcionam sem GPU. |
| Receptor GNSS com produto científico adequado | 1 | Comparar indicador de propagação | Pesquisa. Definir grandeza, taxa, sincronização e calibração antes da seleção. |
| Imageador all-sky científico | 1 | Possível aquisição óptica própria | Fase futura. Instrumentação, filtros e calibração pertencem a uma etapa própria; o TCC pode começar com os dados existentes. |

## Drive de Pobre: consulta registrada

[Drive de Pobre](https://drivedepobre.com/) | 31/10/2026 | Consulta bloqueada por verificação humana

O catálogo exigiu verificação humana nesta consulta. Nenhum curso ou arquivo do acervo foi validado ou redistribuído. Use os termos como roteiro de busca e confira autoria e permissão na origem. Os materiais desta trilha estão ligados diretamente às fontes e aos exercícios do projeto.

Termos de busca: Python, álgebra linear, processamento de imagens, séries temporais.

## Uso dos arquivos

Os exercícios e dados do kit são autorais e sintéticos. Fontes externas permanecem no endereço do autor. Conferir versão, autoria e permissão antes de reutilizar material externo. A aplicação não depende do catálogo para abrir os recursos da trilha.
