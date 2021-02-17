from joblib import load
import numpy as np
import pandas as pd
from MovieRecommendation.gcp import download_matrix
from sklearn.metrics.pairwise import cosine_similarity

class Recommender(object):
    def __init__(self, sample, basis="metadata", hybrid=True, n_movies=3):
        self.sample = sample
        self.basis = basis
        self.hybrid=hybrid
        self.n_movies = n_movies

    def similarity_df(self, basis):
        matrix = download_matrix(f"{basis}")
        v=np.array(matrix.loc[self.sample]).reshape(1, -1)
        sim =  cosine_similarity(matrix, v).reshape(-1)
        df = pd.DataFrame({f"{basis}_similarity": sim}, index=matrix.index.tolist())
        return df

    
    def get_recommendation(self):
        recommendations = {}

        if self.hybrid:
            df1=self.similarity_df("metadata")
            df2=self.similarity_df("rating")
            df = pd.concat([df1, df2],axis=1)
            df["hybrid_similarity"] = df[["metadata_similarity","rating_similarity"]].apply(lambda x: sum(x)/2, axis=1)
            df=df.sort_values(by="hybrid_similarity", ascending=False)
            recommendations = df[1:self.n_movies+1].hybrid_similarity
        
        else:
            df=self.similarity_df(self.basis).sort_values(by=f"{self.basis}_similarity", ascending=False)   
            print("tto")
            recommendations = df[1:self.n_movies+1][f"{self.basis}_similarity"]
        
        return recommendations
        





