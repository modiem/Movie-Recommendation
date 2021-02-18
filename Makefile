# ----------------------------------
#         LOCAL SET UP
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

install:
	@pip install . -U

# ----------------------------------
#         RUN API
# ----------------------------------
run_api:
	uvicorn api.fast:app --reload  # load web server with code autoreload

# ----------------------------------
#         DOCKER & Deployment
# ----------------------------------
GCR_MULTI_REGION=eu.gcr.io
GCP_PROJECT_ID=movie-recommender-api-304919
DOCKER_IMAGE_NAME=${GCR_MULTI_REGION}/${GCP_PROJECT_ID}/api
GCR_REGION=europe-west4

build_image:
	docker build -t ${DOCKER_IMAGE_NAME} .

push_image:
	docker push ${DOCKER_IMAGE_NAME}

deploy_gcp:
	gcloud run deploy \
		--image ${DOCKER_IMAGE_NAME} \
		--platform managed \
		--region ${GCR_REGION} \
		--set-env-vars "GOOGLE_APPLICATION_CREDENTIALS=/credentials.json"


# ----------------------------------
#    CLEANING COMMAND
# ----------------------------------

clean:
	@rm -fr */__pycache__
	@rm -fr __pycache__
	@rm -fr */.ipynb_checkpoints
	@rm -fr .ipynb_checkpoints
	@rm -fr __init__.py
	@rm -fr build
	@rm -fr dist
