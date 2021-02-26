FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY WebApp/requirements.txt ./
ADD WebApp/. /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]