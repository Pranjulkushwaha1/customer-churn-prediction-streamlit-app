# Python 3.11 base image
FROM python:3.11-slim

# Working directory set karo
WORKDIR /app

# Requirements copy karo aur install karo
COPY requirements.txt .
RUN pip install -r requirements.txt

# Saari files copy karo
COPY . .

# Port expose karo
EXPOSE 8000

# App run karo
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]