FROM python:3.10
RUN pip install -r requirements.txt
WORKDIR /app
COPY src/* /app/
ENTRYPOINT ["streamlit", "run", "app.py"]