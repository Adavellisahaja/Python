import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('CC.csv')
# replacing null values with mean
dataset = dataset.fillna(dataset.mean())
x = dataset.iloc[:,1:]
y = dataset.iloc[:,-1]


# feature scaling
from sklearn import preprocessing
scaler =preprocessing.StandardScaler()
scaler.fit(x)
x_scaled_array=scaler.transform(x)
x_scaled=pd.DataFrame(x_scaled_array, columns =x.columns)

# elbow method
wcss = []
for i in range(1,10):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,10),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

##building the model

# nclusters = i # this is the k in kmeans
km = KMeans(n_clusters=2)
km.fit(x_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(x_scaled)
from sklearn import metrics
score = metrics.silhouette_score(x_scaled, y_cluster_kmeans)
print(score)