# :movie_camera: Movie Recommendation API

## Data :open_file_folder:
This dataset consists of the following files:
- **movies.csv**: contains `movieId`, `imdbId`, `tmdbId`
- **tags.csv**: contains `userId`, `movieId`, `tag`, `timestamp`
- **ratings**: contains `userId`, `movieId`, `rating`, `timestamp`


## Under the hood :tophat:
- **Hybrid systems** combining **Content-based** and **Collaborative filtering**
- use **cosine distance** to find similar movies

## Steps :information_desk_person:
- [x] calculate similarity matrix based on metadata/rating
    - [x] vectorization (Tfid)
    - [x] reduce the dimension (TruncatedSVD)
    - [x] save matrix as `.joblib` file
- [x] calculate cosine_similarity on both matrix
    - [x] calculate the hybrid similarity based on both standards
- [x] packaging code
- [x] construc an API
- [ ] build `Docker image`
- [ ] deploy on google cloud run
- [ ] plug it to a front page
