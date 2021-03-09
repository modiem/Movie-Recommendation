from joblib import load
import numpy as np
import pandas as pd
from MovieRecommendation import gcp
from sklearn.metrics.pairwise import cosine_similarity

class Recommender(object):
    def __init__(self, samples, basis="hybrid"):
        '''
        Take a list of movies.
        '''
        self.samples = samples
        self.basis = basis

    def calculate_similarity(self, sample, basis):
        matrix = gcp.get_matrix(basis)
        v=np.array(matrix.loc[sample]).reshape(1, -1)
        sim =  cosine_similarity(matrix, v).reshape(-1)
        df = pd.DataFrame({"similarity": sim}, index=matrix.index.tolist())
        return df

    def get_similarity_df(self, sample):
        if self.basis == "hybrid":
            df1=self.calculate_similarity(sample, "metadata")
            df2=self.calculate_similarity(sample, "rating")
            df = (df1 + df2)/2
        else:
            df = self.calculate_similarity(sample, self.basis)
        return df
    
    
    def get_recommendation(self, n_movies=3):
        df_lst = []
        for i, sample in enumerate(self.samples):
            df = self.get_similarity_df(sample)
            df_lst.append(df)
        df = sum(df_lst)/len(df_lst)
        ## filter out all movies in samples.
        ## sort values based on similarity
        df = df[~df.index.isin(self.samples)].sort_values(by="similarity", ascending=False)
        recommendations = df[:n_movies]["similarity"]
        gcp.clean_matrix()    
        return recommendations
        





