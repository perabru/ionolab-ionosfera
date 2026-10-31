"""Baseline causal: o último frame disponível prevê o próximo."""
import csv,json
from pathlib import Path
def avaliar(rows,emissao=1,alvo=2):
    assert alvo>emissao,'alvo precisa estar no futuro'
    frames={}
    for r in rows:frames.setdefault(int(r['frame']),{})[(int(r['linha']),int(r['coluna']))]=float(r['intensidade_demo'])
    observado=frames[emissao];referencia=frames[alvo]
    assert observado.keys()==referencia.keys()
    previsao=dict(observado)
    mae=sum(abs(previsao[k]-referencia[k]) for k in previsao)/len(previsao)
    return {'baseline':'persistencia','frame_emissao':emissao,'frame_alvo':alvo,'mae_intensidade_arbitraria':mae,'origem':'sintética'}
if __name__=='__main__':
    with Path(__file__).with_name('frames_demo.csv').open() as f:print(json.dumps(avaliar(list(csv.DictReader(f))),ensure_ascii=False,indent=2))
