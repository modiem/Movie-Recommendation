from joblib import load
import numpy as np
import pandas as pd
from MovieRecommendation.gcp import download_matrix
from sklearn.metrics.pairwise import cosine_similarity

class Recommender(object):
    def __init__(self, sample, basis="hybrid"):
        self.sample = sample
        self.basis = basis

    def calculate_similarity(self, basis):
        matrix = download_matrix(f"{basis}")
        v=np.array(matrix.loc[self.sample]).reshape(1, -1)
        sim =  cosine_similarity(matrix, v).reshape(-1)
        df = pd.DataFrame({"similarity": sim}, index=matrix.index.tolist())
        return df

    def get_similarity_df(self):
        if self.basis == "hybrid":
            df1=self.calculate_similarity("metadata")
            df2=self.calculate_similarity("rating")
            df = (df1 + df2)/2
        else:
            df = self.calculate_similarity(self.basis)
        return df
    
    def get_recommendation(self, n_movies):
        df=self.get_similarity_df().sort_values(by="similarity", ascending=False)
        recommendations = df[1:n_movies+1]["similarity"]       
        return recommendations
        





