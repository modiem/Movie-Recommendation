import re
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
def create_recommendations(samples: str,
                           basis: str="hybrid",
                           n_movies: int=3):
    """
    Input: one or more 'sample movies' seperated by comma.
    Output: n recommendations.
    """
    samples=[f.strip("''") for f in re.split(r''', (?='|")''', samples)]

    recommendations = Recommender(samples, 
                                  basis=basis).get_recommendation(n_movies=n_movies)

    result = {"basis": basis,
              "recommendations": 
                [{"ranking": i+1, 
                  "name":name, 
                  "similarity":recommendations[i]}
                   for i, name in enumerate(recommendations.index)],
              }
    
    return result