import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import numpy as np
import random
import pandas as pd


def plot(x, y, type, special):
    fig, ax = plt.subplots()

    plt.scatter(x, y, c=label_list, edgecolors='black', cmap="RdBu", s=100)
    plt.ylabel(special, fontsize=24)
    plt.xlabel("{} Component".format(type),fontsize=24)

    ax.tick_params(bottom=True, top=True, left=True, right=True, which='major', direction='in', length=8, width=2, labelsize=13,)
    plt.colorbar().set_label(label=color_label,size=24)
    plt.savefig("Images/{}_{}_{}_{}.png".format(name, special, color_label, type))
    plt.clf()

name = "2EOR"
color_label = "h2e-ORR"

inputs = [4, 5, 6, 7, 8]
special_index = 3
special = "ΔGO*"

output_index = 11

df = pd.read_excel('Data/{}.xlsx'.format(name))


data_list = df.loc[0:len(df),:].values.tolist()


input_list = [[row[i] for i in inputs] for row in data_list]


label_list = [row[output_index] for row in data_list]

principal=PCA(n_components=1)
principal.fit(input_list)
transformed=principal.transform(input_list)


x = [row[special_index] for row in data_list]
y = transformed[:,0]


plot(x, y, "PCA", special)





tsne = TSNE(n_components=1, verbose=1, perplexity=40, n_iter=300)
tsne_results = tsne.fit_transform(np.array(input_list))
x = tsne_results[:,0]


plot(x, y, "TSNE", special)
