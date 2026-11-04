"""Validate the published aggregate numbers, without training or private data."""
from pathlib import Path
import csv, math
R=Path(__file__).resolve().parents[1]
def read(name):
    with (R/'results'/name).open() as f:return list(csv.DictReader(f))
expected={2020:(4292,787,430,258),2021:(4794,747,480,227),2022:(5199,629,520,210)}
for r in read('annual_metrics.csv'):
    y=int(r['year']);n,p,k,h=expected[y]
    assert tuple(int(r[c]) for c in ['rows','positives','budget','found'])==(n,p,k,h)
    assert k==math.ceil(.1*n)
    assert abs(float(r['recall'])-h/p)<1e-12
    assert abs(float(r['precision'])-h/k)<1e-12
com=read('communication.csv');assert sum(int(r['fp32_bytes']) for r in com)==3205
assert sum(int(r['selected_bytes']) for r in com)==899
attack=read('privacy_attack.csv');task=read('privacy_task.csv')
means={}
for arm in ['S0','D1','MID']:
    a=[float(r['success_0.319']) for r in attack if r['arm']==arm and r['view']=='messages' and r['group']=='all']
    t=[float(r['recall']) for r in task if r['arm']==arm]
    assert len(a)==len(t)==5
    means[arm]=(sum(a)/5,sum(t)/5)
assert abs((means['S0'][0]-means['MID'][0])*100-20.423255630392)<1e-6
assert abs((means['S0'][1]-means['MID'][1])*100-.807381776239)<1e-6
print('Aggregate checks passed: annual lists, communication ledger and paired privacy means.')
print('No private samples loaded; no model trained.')
