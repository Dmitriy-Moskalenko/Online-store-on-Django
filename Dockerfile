FROM python:3

COPY . /app
WORKDIR /app

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install django
RUN pip install -r requirements.txt
RUN pip install virtualenv
RUN pip install Pillow

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0:8000" ]
EXPOSE 8000