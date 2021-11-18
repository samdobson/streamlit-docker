FROM python:3.10-slim
EXPOSE 8501
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit_app.py"]
