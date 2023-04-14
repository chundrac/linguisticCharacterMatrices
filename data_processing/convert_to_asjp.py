import os
import asjp
import pandas as pd
import re

treenames = [fn.split('.')[0] for fn in os.listdir('../lexibank/data/mrbayes_posteriors')]

for tree in treenames:
    df = pd.read_csv('../lexibank/lexibank-analysed/raw/{}/cldf/forms.csv'.format(tree),na_filter=False)
    forms = list(df['Segments'])
    asjp_forms = []
    asjp_segs = []
    for w in forms:
        w_ = w.replace('/',' ').split()
        w__ = []
        for s in w_:
            try:
                w__.append(asjp.ipa2asjp(s))
            except:
                continue
        asjp_forms.append(' '.join(w__))
        asjp_segs.append(' '.join(sorted(set(w__))))
    df['asjp_forms'] = asjp_forms
    df['asjp_segs'] = asjp_segs
    df.to_csv('../lexibank/lexibank-analysed/raw/{}/cldf/forms_w_asjp.csv'.format(tree))