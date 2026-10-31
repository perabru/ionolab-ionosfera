# Tecnologias propostas

O HTML do briefing usa JavaScript e CSS nativos. A stack abaixo descreve o produto a desenvolver.

### React + TypeScript + Vite

Uma interface com contratos tipados e componentes reaproveitáveis.

- **Onde entra:** Aplicativo web responsivo; UI com CSS próprio e primitivas Radix.
- **Contrato:** Estados de carregamento, vazio, falha e foco visível em todas as rotas.
- [Documentação](https://react.dev/)

### Python + FastAPI + Pydantic

Validar entradas e publicar contratos REST/OpenAPI.

- **Onde entra:** Servidor da aplicação; processamento pesado fora da requisição.
- **Contrato:** IDs obtidos da sessão; validação, paginação e erros legíveis.
- [Documentação](https://fastapi.tiangolo.com/)

### PostgreSQL + SQLAlchemy + Alembic

Relacionar registros, versões, permissões e auditoria.

- **Onde entra:** Banco transacional; migrações versionadas.
- **Contrato:** Chaves únicas, transações, backup e restauração testada.
- [Documentação](https://www.postgresql.org/docs/)

### Keycloak + OIDC + sessão no servidor

Reutilizar identidade, verificação de e-mail, recuperação e MFA da equipe.

- **Onde entra:** BFF Python com Authlib; JWT verificado na API.
- **Contrato:** Cookie HttpOnly/Secure/SameSite; CSRF; papéis e propriedade conferidos no servidor.
- [Documentação](https://www.keycloak.org/securing-apps/oidc-layers)

### S3 compatível + checksums

Guardar originais e derivados sem transformar o banco em repositório de mídia.

- **Onde entra:** Armazenamento privado por projeto e URLs temporárias.
- **Contrato:** Chaves e permissões geradas no servidor; tamanho, MIME e integridade validados.
- [Documentação](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

### Redis + Celery

Executar importações e análises demoradas sem bloquear a tela.

- **Onde entra:** Workers separados da API com fila e status persistido.
- **Contrato:** Tarefa identificada por arquivo/versão; repetição idempotente e cancelamento cooperativo.
- [Documentação](https://docs.celeryq.dev/)

### Linux + Docker Compose + Caddy

Reproduzir o piloto e servir a interface por HTTPS.

- **Onde entra:** Ambientes de desenvolvimento, homologação e piloto separados.
- **Contrato:** Segredos fora do repositório, volumes persistentes e recuperação documentada.
- [Documentação](https://docs.docker.com/compose/)

### Git + CI + pytest + Vitest + Playwright

Verificar cálculo, contrato e percurso completo antes da entrega.

- **Onde entra:** Testes de API Python, componentes e navegador.
- **Contrato:** Versões fixadas no lockfile; testes de falha, autorização e retomada.
- [Documentação](https://playwright.dev/docs/intro)

### OpenTelemetry + Prometheus + Grafana

Observar recepção, latência, falhas e consumo.

- **Onde entra:** Instrumentação no servidor, métricas dos workers e logs estruturados.
- **Contrato:** Sem credenciais nos logs; alertas acionáveis e registro das interrupções.
- [Documentação](https://opentelemetry.io/docs/languages/python/)

### Adaptador INPE / EMBRACE + httpx

Receber imagens e metadados da estação selecionada.

- **Onde entra:** Importação autorizada por arquivo ou endpoint realmente disponível.
- **Contrato:** Preservar estação, UTC, filtro, licença, checksum e lacunas; disponibilidade não é presumida.
- [Documentação](https://www2.inpe.br/climaespacial/AGCImagerViewer/faces/about.xhtml?lan=pt)

### OpenCV + NumPy + SciPy

Preparar quadros e criar baselines de segmentação e movimento.

- **Onde entra:** Máscaras de qualidade, alinhamento, realce relativo e optical flow.
- **Contrato:** Brilho não é densidade; sem calibração não há localização geográfica confiável.
- [Documentação](https://docs.opencv.org/4.x/)

### xarray + Zarr / NetCDF

Organizar imagens como estação × tempo × posição.

- **Onde entra:** Cubos derivados com coordenadas, qualidade e atributos.
- **Contrato:** UTC, calendário, unidade e versão da projeção preservados.
- [Documentação](https://docs.xarray.dev/en/stable/)

### Persistência / advecção + PyTorch

Comparar modelo temporal com baselines antes de aumentar complexidade.

- **Onde entra:** Predição experimental de máscara ou probabilidade; ConvLSTM é candidato.
- **Contrato:** Horizontes 15/30/60 min são propostas; só treinar com séries suficientes e sem vazamento.
- [Documentação](https://pytorch.org/docs/stable/index.html)

### scikit-learn + validação por noite/estação

Quantificar detecção e previsão com unidade de avaliação definida.

- **Onde entra:** Precisão, recall, F1, IoU, Brier e curva de calibração conforme o alvo.
- **Contrato:** Split cronológico com janela de separação; teste intocado e revisão dos rótulos.
- [Documentação](https://scikit-learn.org/stable/modules/model_evaluation.html)

### MLflow + manifesto de dataset

Relacionar cada resultado ao conjunto e aos parâmetros usados.

- **Onde entra:** Experimentos, pesos, baseline, métricas e versão do pipeline.
- **Contrato:** Não promover um modelo com base no conjunto de teste usado repetidamente.
- [Documentação](https://mlflow.org/docs/latest/)

### Ollama + modelo local + JSON Schema

Produzir explicação limitada ao pacote de evidências.

- **Onde entra:** LLM recebe métricas, mapas resumidos, qualidade e referências permitidas.
- **Contrato:** Saída validada; números conferidos; abster se faltarem dados; guardar versão e prompt.
- [Documentação](https://docs.ollama.com/)

### Plotly.js + MapLibre GL JS

Exibir séries, mapas, horizonte e matriz.

- **Onde entra:** Interface com comparações lado a lado e cobertura observada.
- **Contrato:** Mapa esquemático identificado; sem confundir previsão, observação e campo real.
- [Documentação](https://plotly.com/javascript/)
