import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import numpy as np
import random
import pandas as pd


name = "2EOR"

input_start = 3

input_end = 9

output_index = 11

df = pd.read_excel('Data/{}.xlsx'.format(name))


data_list = df.loc[0:len(df),:].values.tolist()

input_list = [row[input_start:input_end] for row in data_list]

label_list = [row[output_index]+1 for row in data_list]

principal=PCA(n_components=2)
principal.fit(input_list)
transformed=principal.transform(input_list)



x = transformed[:,0]
y = transformed[:,1]


plt.scatter(x, y, c=label_list, cmap="RdBu", s=100)


plt.colorbar()
plt.title("{} PCA".format(name))
plt.savefig("Images/{}_PCA.png".format(name))
plt.clf()

tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
tsne_results = tsne.fit_transform(np.array(input_list))
x = tsne_results[:,0]
y = tsne_results[:,1]

plt.scatter(x, y, c=label_list, cmap="RdBu", s=100)
plt.title("{} TSNE".format(name))

plt.colorbar()

plt.savefig("Images/{}_TSNE.png".format(name))
