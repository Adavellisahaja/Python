import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# You can add the parameter data_home to wherever to where you want to download your data
dataset = pd.read_csv('CC.csv')
#print (dataset.isnull().sum())
dataset=dataset.fillna(dataset.mean())
#print (dataset.isnull().sum())
x = dataset.iloc[:,1:]
#y = dataset.iloc[:,-1]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x)
x_scaler = scaler.transform(x)
pca = PCA(2)

x_pca = pca.fit_transform(x_scaler)

df2 = pd.DataFrame(data=x_pca)
 #this is PCA of original data set with only 2 coloum now
print(df2)



wcss = []
for i in range(1,10):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,10),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

##building the model

# nclusters = i # this is the k in kmeans
km = KMeans(n_clusters=3)
km.fit(df2)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(df2)
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)