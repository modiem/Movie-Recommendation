from typing import Optional
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

@app.get("/recommendation/")
def create_recommendations(sample,
                           hybrid: bool = True,
                           basis: Optional[str] = None,
                           n_movies: int = 3):

    sample = Recommender(sample,
                        hybrid=hybrid,
                        basis=basis,
                        n_movies=n_movies)
    
    recommendations = sample.get_recommendation()

    if hybrid:
        basis="hybrid"

    result = {"basis": basis,
              "recommendations": 
                [{"ranking": i+1, 
                  "name":name, 
                  "similarity":recommendations[i]}
                   for i, name in enumerate(recommendations.index)],
              }
    
    return result