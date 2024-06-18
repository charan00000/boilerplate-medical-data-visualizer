import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2

df['overweight'] = ((df['weight'] / (df['height']/100) ** 2) > 25).astype(int)
# 3
df['cholesterol'] = (df['cholesterol']>1).astype(int)
df['gluc'] = (df['gluc']>1).astype(int)
# 4

def draw_cat_plot():
    # 5
    df_cat = df.melt(value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 
                                 'active', 'overweight'], id_vars=['cardio'])
    #print(df_cat)
    # 6
    df_cat['count'] = 1
    df_cat = df_cat.groupby(by = ['variable', 'cardio', 'value'], as_index = False).count()
    #df_grouped['cardio' == 1, 'opposite'] = num_cardio - df_grouped['value']

    # 7



    # 8
    fig = sns.catplot(x = 'variable', y='count', kind = 'bar', data=df_cat, hue='value'
                      , col = 'cardio')


    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['height'] >= df['height'].quantile(.025)) &
        (df['height'] <= df['height'].quantile(.975)) &
        (df['weight'] >= df['weight'].quantile(.025)) &
        (df['weight'] <= df['weight'].quantile(.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr.to_numpy())



    # 14
    fig, ax = plt.subplots(figsize = (12,12))

    # 15

    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')

    # 16
    fig.savefig('heatmap.png')
    return fig
