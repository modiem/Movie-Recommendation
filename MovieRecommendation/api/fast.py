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
    return {"ok": "True"}

@app.get("/recommendation/")
def create_recommendations(sample,
                           hybrid,
                           benchmark,
                           n_movies):

    sample = Recommender(sample,
                        hybrid=hybrid,
                        benchmark=benchmark,
                        n_movies=n_movies)
    
    recommendations = sample.get_recommendation()

    return recommendations

