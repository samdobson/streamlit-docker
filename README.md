# Streamlit Docker image

## How to use

No need to clone the GitHub repo. Just create a new folder with your app (named `streamlit_app.py`) and a `Dockerfile` with:

```Dockerfile
FROM samdobson/streamlit
COPY ./streamlit_app.py /usr/src/app
```

Then you can build your image with `docker build -t mystreamlitapp .`

## Deploying to Kubernetes?

Check out https://github.com/samdobson/helm/tree/master/charts/streamlit
