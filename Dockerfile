FROM python:3.7-buster

COPY api /api
COPY MovieRecommendation /MovieRecommendation
COPY requirements.txt /requirements.txt
COPY gcp_key/movie-recommender-api-304919-7b8a3d96787b.json /credentials.json

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT