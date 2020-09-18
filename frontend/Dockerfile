FROM node:12-alpine
ENV DEBUG=*

WORKDIR /app

COPY ./package.json /app
COPY ./package-lock.json /app

RUN npm install

COPY . /app

EXPOSE 3000
