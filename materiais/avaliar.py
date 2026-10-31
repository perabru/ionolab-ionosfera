"""Matriz binária: linhas = verdade; colunas = previsão."""
import csv,json
from pathlib import Path
def metricas(rows):
    tn=fp=fn=tp=0
    for r in rows:
        a,b=int(r['verdade']),int(r['previsao']);assert a in [0,1] and b in [0,1]
        if a==b==0:tn+=1
        elif a==0:fp+=1
        elif b==0:fn+=1
        else:tp+=1
    div=lambda a,b:a/b if b else None
    return {'matriz_TN_FP_FN_TP':[[tn,fp],[fn,tp]],'suporte':tn+fp+fn+tp,'precisao':div(tp,tp+fp),'recall':div(tp,tp+fn),'f1':div(2*tp,2*tp+fp+fn),'iou':div(tp,tp+fp+fn),'origem':'sintética'}
if __name__=='__main__':
    with Path(__file__).with_name('rotulos_demo.csv').open() as f:print(json.dumps(metricas(list(csv.DictReader(f))),ensure_ascii=False,indent=2))
