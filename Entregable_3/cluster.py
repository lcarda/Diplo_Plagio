# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:20:07 2020

@author: pablonicolasr
"""

from sklearn.cluster import DBSCAN

def cluster_ip(X, min_samples, metric="cosine",eps=0.1):
    cluster = DBSCAN(
        eps=eps,
        min_samples=min_samples,
        metric=metric,
        algorithm="brute"
    )

    cluster.fit_predict(X)

    return cluster


# Etiquetas asignadas por el algoritmo


#clusters = km.labels_


#print('Suma de los cuadrados de las distancias al centro de cada cluster=Inertia= ', km.inertia_)

#df_clusters=df_final_scaled.copy()
#df_clusters['kmeans_5'] = km.labels_ #clusters
#print('Kmeans encontró: ', max(km.labels_)+1, 'clusters, nosotros forzamos la cantidad')
#df_clusters.head(4)

