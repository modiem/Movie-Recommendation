from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from MovieRecommendation.recommender import Recommender

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"message": "Welcome!"}

@app.get("/similarity_df/")
def get_sim_df(sample,
               basis: str = "hybrid"):

    sample = Recommender(sample,
                        basis=basis)
    
    df = sample.get_similarity_df()

    result = {"basis": basis,
              "similarity_df": df}
    return result

@app.get("/recommendation/")
def create_recommendations(sample,
                           basis: str="hybrid",
                           n_movies: int=3):

    sample = Recommender(sample,
                        basis=basis)
    
    recommendations = sample.get_recommendation(n_movies)

    result = {"basis": basis,
              "recommendations": 
                [{"ranking": i+1, 
                  "name":name, 
                  "similarity":recommendations[i]}
                   for i, name in enumerate(recommendations.index)],
              }
    
    return result