FROM python:3.10
WORKDIR /app
COPY src/* /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit", "run", "app.py"]