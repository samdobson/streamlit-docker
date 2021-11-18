FROM python:3.10-slim
EXPOSE 8501
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY streamlit_app.py ./
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit_app.py"]
