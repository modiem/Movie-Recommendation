# :movie_camera: Movie Recommendation API

## Data :open_file_folder:
This dataset consists of the following files:
- **movies.csv**: contains `movieId`, `imdbId`, `tmdbId`
- **tags.csv**: contains `userId`, `movieId`, `tag`, `timestamp`
- **ratings**: contains `userId`, `movieId`, `rating`, `timestamp`


## Under the hood :tophat:
- **Hybrid systems** combining **Content-based** and **Collaborative filtering**
- use **cosine distance** to find similar movies

## Steps :pencil:
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
[Try it out?](https://movie-recommender-5i6qxbf74a-ez.a.run.app)
- [ ] plug it to a front page

