FROM python:3.8-slim-buster
EXPOSE 8501
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit_app.py"]
