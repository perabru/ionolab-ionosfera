# Inventário de telas · IonoLab

23 telas e seus critérios de aceite.

## I01 · Fenômenos e proposta de TCC

`/` · Público

Explicar blobs, bubbles e a pergunta de pesquisa.

- **Campos:** Conceitos; Sinal GNSS; Limites.
- **Ações:** Comparar fenômenos; Ver método.
- **Estados:** Ilustração sem escala; Referência indisponível.
- **API:** `GET /v1/public/project`
- **Aceite:** Distinguir observação óptica de densidade eletrônica.

## I02 · Estações e fontes

`/dados/estacoes` · Pesquisa

Escolher cobertura e disponibilidade.

- **Campos:** Estação; Filtro; UTC; Fonte; Licença.
- **Ações:** Cadastrar; Ver cobertura.
- **Estados:** Sem dado; Acesso restrito; Estação legada.
- **API:** `GET /v1/stations`
- **Aceite:** A fonte real é verificada antes de agendar importação.

## I03 · Importar sequência

`/dados/importar` · Pesquisa

Registrar quadros com procedência.

- **Campos:** Arquivo; Estação; Data; Checksum.
- **Ações:** Importar; Validar.
- **Estados:** Timestamp ausente; Duplicata; Arquivo corrompido.
- **API:** `POST /v1/ingestions`
- **Aceite:** Preservar o original e informar lacunas da sequência.

## I04 · Qualidade do céu

`/dados/qualidade` · Pesquisa

Marcar condições que invalidam interpretação.

- **Campos:** Nuvens; Lua; Exposição; Máscara.
- **Ações:** Aceitar; Excluir; Revisar.
- **Estados:** Quadro inconclusivo; Sem metadado.
- **API:** `PATCH /v1/frames/:id/quality`
- **Aceite:** Região excluída não é convertida automaticamente em fundo.

## I05 · Calibração e projeção

`/dados/calibracao` · Pesquisa

Vincular geometria e hipótese de camada ao mapa.

- **Campos:** Lente; Orientação; Altura assumida; CRS.
- **Ações:** Calibrar; Versionar; Confrontar referência.
- **Estados:** Sem calibração; Erro de alinhamento.
- **API:** `POST /v1/calibrations`
- **Aceite:** O mapa informa hipótese de projeção e limite de cobertura.

## I06 · Explorador temporal

`/sequencias/:id` · Pesquisa

Percorrer quadros sincronizados.

- **Campos:** Quadro; UTC; Qualidade; Intervalo.
- **Ações:** Avançar; Sobrepor; Comparar.
- **Estados:** Lacuna; Quadro indisponível.
- **API:** `GET /v1/sequences/:id`
- **Aceite:** Ordem temporal não usa o horário de download como aquisição.

## I07 · Anotação de blobs e bubbles

`/anotar/:id` · Pesquisa

Criar rótulo revisável de realces e depleções.

- **Campos:** Máscaras; Classe; Justificativa; Revisor.
- **Ações:** Desenhar; Revisar; Abster.
- **Estados:** Ambiguidade; Discordância; Região inválida.
- **API:** `POST /v1/annotations`
- **Aceite:** Rótulos mantêm versão, autor e área inconclusiva.

## I08 · Dataset e partições

`/datasets/:id` · Pesquisa

Separar desenvolvimento e avaliação.

- **Campos:** Noites; Estações; Janelas; Gap.
- **Ações:** Dividir; Congelar; Auditar.
- **Estados:** Vazamento; Classe sem suporte.
- **API:** `POST /v1/datasets/:id/split`
- **Aceite:** Nenhuma noite ou evento compartilhado atravessa o split sem justificativa.

## I09 · Detecção e rastreamento

`/analise/deteccao` · Pesquisa

Aplicar baseline e acompanhar estruturas.

- **Campos:** Máscara; Contorno; Deriva; Qualidade.
- **Ações:** Executar; Comparar; Corrigir.
- **Estados:** Nuvem confundida; Rastreamento perdido.
- **API:** `POST /v1/detection-runs`
- **Aceite:** Todo resultado se liga ao quadro e versão do método.

## I10 · Treino e experimentos

`/experimentos` · Pesquisa

Comparar candidatos com baseline.

- **Campos:** Dataset; Parâmetros; Seed; Métricas.
- **Ações:** Treinar; Cancelar; Comparar.
- **Estados:** Falha de memória; Poucos dados.
- **API:** `POST /v1/experiments`
- **Aceite:** Teste final não é usado para selecionar hiperparâmetros.

## I11 · Previsão espacial

`/previsoes` · Pesquisa

Estimar ocorrência por célula e horizonte.

- **Campos:** Entrada até t; Δ; Probabilidade; Cobertura.
- **Ações:** Executar; Trocar horizonte.
- **Estados:** Entrada antiga; Sem cobertura; Modelo inválido.
- **API:** `POST /v1/forecasts`
- **Aceite:** A entrada nunca inclui um quadro posterior ao instante de emissão.

## I12 · Mapa observado × previsto

`/previsoes/:id/mapa` · Pesquisa

Comparar campos sem confundir origem.

- **Campos:** Observação; Previsão; Diferença; UTC.
- **Ações:** Sobrepor; Inspecionar célula.
- **Estados:** Sem observação futura; Área inválida.
- **API:** `GET /v1/forecasts/:id/map`
- **Aceite:** Mostrar emissão, validade, horizonte e legenda de probabilidade.

## I13 · Matriz de confusão

`/avaliacao/matriz` · Pesquisa

Contar acertos e erros na unidade declarada.

- **Campos:** TP; FP; FN; TN; Suporte; Limiar.
- **Ações:** Ajustar no conjunto permitido; Exportar.
- **Estados:** Classe ausente; Denominador zero.
- **API:** `GET /v1/evaluations/:id/confusion`
- **Aceite:** Mudar limiar da demonstração não altera o resultado publicado do teste.

## I14 · Curvas e calibração

`/avaliacao/curvas` · Pesquisa

Ver sensibilidade ao limiar e confiabilidade.

- **Campos:** PR; F1; IoU; Brier; Intervalos.
- **Ações:** Comparar; Estratificar.
- **Estados:** Amostra pequena; Calibração ausente.
- **API:** `GET /v1/evaluations/:id/curves`
- **Aceite:** Métricas declaram unidade, classes e período do conjunto.

## I15 · GNSS e comunicações

`/analise/comunicacoes` · Pesquisa

Relacionar estruturas a indicadores complementares.

- **Campos:** STEC; S4 se disponível; Período; Fonte.
- **Ações:** Sincronizar; Comparar.
- **Estados:** Sem receptor; Tempo incompatível.
- **API:** `POST /v1/link-analyses`
- **Aceite:** Não inferir uma queda de sinal apenas do brilho de uma imagem.

## I16 · Pacote de evidências

`/evidencias/:id` · Pesquisa

Preparar fatos verificáveis para a explicação.

- **Campos:** Métricas; Mapas; Qualidade; Referências.
- **Ações:** Validar; Versionar.
- **Estados:** Fonte ausente; Métrica inconsistente.
- **API:** `POST /v1/evidence-packages`
- **Aceite:** Números do pacote podem ser recalculados sem a LLM.

## I17 · Análise com LLM

`/relatorios/llm` · Pesquisa

Gerar explicação restrita à evidência.

- **Campos:** Modelo; Prompt; Fontes; Saída estruturada.
- **Ações:** Gerar; Revisar; Rejeitar.
- **Estados:** Alucinação numérica; Evidência insuficiente.
- **API:** `POST /v1/llm-reports`
- **Aceite:** Bloquear publicação se houver número não sustentado; guardar versão do modelo.

## I18 · Relatório do TCC

`/relatorios/tcc` · Pesquisa

Exportar método, resultados e limites.

- **Campos:** Pergunta; Método; Baseline; Validação; Referências.
- **Ações:** Montar; Exportar; Congelar versão.
- **Estados:** Experimento incompleto; Revisão pendente.
- **API:** `POST /v1/reports`
- **Aceite:** Ilustrações sintéticas e resultados reais aparecem identificados separadamente.

## I19 · Operação e modelos

`/gestao/operacao` · Gestão

Acompanhar ingestão, fila e versões liberadas.

- **Campos:** Fila; Falhas; Última coleta; Modelo ativo.
- **Ações:** Repetir; Suspender; Consultar logs.
- **Estados:** Serviço degradado; Previsão vencida.
- **API:** `GET /v1/ops`
- **Aceite:** Sem dados recentes, nenhuma previsão é apresentada como atual.

## I20 · Entrar e criar conta

`/conta/entrar` · Conta

Identificar a pessoa antes de abrir recursos privados.

- **Campos:** Nome público; E-mail; Retorno autorizado.
- **Ações:** Entrar via OIDC; Criar conta; Sair.
- **Estados:** E-mail não confirmado; Sessão expirada; Acesso recusado.
- **API:** `GET /auth/login · GET /auth/callback`
- **Aceite:** Nunca aceitar uma URL de retorno externa sem validação; nenhum token no armazenamento local.

## I21 · Verificação e recuperação de acesso

`/conta/recuperar` · Conta

Concluir verificação e redefinição pelo provedor de identidade.

- **Campos:** Solicitação; Expiração; Estado do link.
- **Ações:** Pedir novo link; Confirmar e-mail; Definir senha no provedor.
- **Estados:** Link expirado; Uso anterior; Limite de tentativas.
- **API:** `Fluxos de ação do Keycloak`
- **Aceite:** Respostas de recuperação não revelam se um endereço está cadastrado.

## I22 · Perfil e preferências

`/conta/perfil` · Conta

Editar os próprios dados e preferências de uso.

- **Campos:** Nome; Idioma; Preferências; Sessões.
- **Ações:** Salvar; Encerrar sessão; Solicitar exportação.
- **Estados:** Erro de validação; Sem conexão; Alteração pendente.
- **API:** `GET/PATCH /v1/me`
- **Aceite:** Uma conta nunca consulta o perfil privado de outra alterando um ID.

## I23 · Equipe, acessos e auditoria

`/gestao/equipe` · Gestão

Vincular pessoas ao escopo correto e registrar mudanças.

- **Campos:** Pessoa; Papel; Projeto; Convites; Histórico.
- **Ações:** Convidar; Revogar; Consultar alterações.
- **Estados:** Convite vencido; Sem permissão; Último responsável.
- **API:** `GET/POST /v1/members · GET /v1/audit`
- **Aceite:** Revogação vale no servidor; manter pelo menos um responsável e trilha de alteração.
