import os
import pandas as pd
from collections import defaultdict

treenames = [fn.split('.')[0] for fn in os.listdir('../lexibank/data/mrbayes_posteriors')]

fams = defaultdict(list)
treesize = {}

for tree in treenames:
    df = pd.read_csv('../lexibank/lexibank-analysed/raw/{}/cldf/languages.csv'.format(tree))
    if len(list(set(df['Family'].dropna()))) == 1:
        fam = list(set(df['Family'].dropna()))[0]
        if fam == 'Karankawa':
            fam = 'Uto-Aztecan'
        fams[fam].append(tree)
        treesize[tree] = df.shape[0]-1
    else:
        print(tree,list(set(df['Family'].dropna())))