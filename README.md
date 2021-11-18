# Streamlit Docker image

## Usage

### Running the demo app locally

`docker run -p 8501:8501 streamlit`

### Containerising your own Streamlit app
No need to clone the GitHub repo. Just create a new folder with your app (named `streamlit_app.py`) and a `Dockerfile` with:

```Dockerfile
FROM samdobson/streamlit
COPY ./requirements.txt /usr/src/app
COPY ./streamlit_app.py /usr/src/app
```

... then build your container:

`docker build . -t my-streamlit-app`

... and run as above.

## Deploying to Kubernetes?

Check out https://github.com/samdobson/helm/tree/master/charts/streamlit
