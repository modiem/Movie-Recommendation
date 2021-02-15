# ----------------------------------
#         LOCAL SET UP
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

install:
	@pip install . -U

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
