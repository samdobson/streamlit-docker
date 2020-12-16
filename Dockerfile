FROM python:3.8-buster
EXPOSE 8501
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install streamlit==0.72.0
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit_app.py"]
