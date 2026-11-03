window.PROTOTYPE_CONFIG = {
  "id": "iono",
  "name": "IonoLab",
  "initial": "datasets",
  "dark": true,
  "avatar": "IL",
  "roles": [
    {
      "id": "analysis",
      "name": "Preparação e análise",
      "screens": [
        "datasets",
        "import",
        "quality",
        "annotation"
      ]
    },
    {
      "id": "results",
      "name": "Avaliação e relatório",
      "screens": [
        "baseline",
        "evaluation",
        "report"
      ]
    }
  ],
  "nav": [
    [
      "Conjuntos",
      "datasets"
    ],
    [
      "Anotar",
      "annotation"
    ],
    [
      "Avaliação",
      "baseline"
    ],
    [
      "Relatório",
      "report"
    ]
  ],
  "screens": [
    {
      "id": "datasets",
      "title": "Conjuntos de imagens",
      "note": "Carregue a sequência sintética de seis quadros."
    },
    {
      "id": "import",
      "title": "Importação",
      "note": "Experimente a entrada de nomes de arquivos e metadados."
    },
    {
      "id": "quality",
      "title": "Qualidade dos quadros",
      "note": "Escolha um quadro, mostre a máscara e marque exclusões."
    },
    {
      "id": "annotation",
      "title": "Anotação",
      "note": "Atribua um rótulo à região ilustrativa de cada quadro."
    },
    {
      "id": "baseline",
      "title": "Referência de persistência",
      "note": "Compare duas máscaras sintéticas e calcule a sobreposição."
    },
    {
      "id": "evaluation",
      "title": "Avaliação",
      "note": "Confira as contagens e a fórmula de IoU do exemplo."
    },
    {
      "id": "report",
      "title": "Relatório",
      "note": "Exporte as escolhas e os resultados sintéticos em JSON."
    }
  ]
};
