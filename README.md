# :movie_camera: Movie Recommendation API
[![Front_end][screenshot]][hyperlink]
 
[hyperlink]: https://modiem.herokuapp.com/ 
[screenshot]: img/Screenshot.png "Screen Shot"

## Usage 
```python
import requests
url = "https://movie-recommender-5i6qxbf74a-ez.a.run.app/recommendation/"

### 
sample_movie="Jumanji (1995)"

params = dict(samples=sample_movie,
                      n_movies=1 ## number of recommendations to return
                      )
response = requests.get(url, params=params).json()
print(response)
```

## Data :open_file_folder:
The dataset consists of the following files:
- **movies.csv**: contains `movieId`, `imdbId`, `tmdbId`
- **tags.csv**: contains `userId`, `movieId`, `tag`, `timestamp`
- **ratings**: contains `userId`, `movieId`, `rating`, `timestamp`


## Under the hood :tophat:
- **Hybrid systems** combining **Content-based** and **Collaborative filtering**
- use **cosine distance** to find similar movies

### In steps :pencil:
- [x] calculate similarity matrix based on metadata/rating
    - [x] vectorization (Tfid)
    - [x] reduce the dimension (TruncatedSVD)
    - [x] save matrix as `.joblib` file
    - [x] upload it to google storage
- [x] calculate cosine_similarity of a sample movie on both matrix
    - [x] calculate hybrid similarity
- [x] packaging code (OOP)
- [x] construct an API (`FastAPI`)
    - [x] return `n` recommended movies as query
    - [x] return similarity df
- [x] build `Docker image`
```bash
docker build -t $DOCKER_IMAGE_NAME .
```
- [x] container registry
```bash
docker push $DOCKER_IMAGE_NAME
```
- [x] deploy on google cloud run
```bash
gcloud run deploy \
		--image ${DOCKER_IMAGE_NAME} \
		--platform managed \
		--region ${GCR_REGION} \
		--set-env-vars "GOOGLE_APPLICATION_CREDENTIALS=/credentials.json"

```
- [x] plug in the front-end


