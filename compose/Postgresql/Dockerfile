version: '3'

services:
  postgres:
    image: postgres:13  # Utiliza la versión de PostgreSQL que desees
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWD}
    ports:
      - "${DB_PORT}:5432"
