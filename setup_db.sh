#!/bin/bash


if [ -f .env.development ]; then
    export $(grep -v '^#' .env.development | xargs)
else
    echo "❌ Error: .env.development file not found!"
    exit 1
fi


echo "🔄 Initialising [$ENV] database: $DB_NAME as user: $DB_USER..."

# 3. Execute setup.sql while mapping the bash ENV variables into psql variables

PGPASSWORD=$DB_PASSWORD psql \
  -h "$DB_HOST" \
  -p "$DB_PORT" \
  -U "$DB_USER" \
  -d "postgres" \
  -v DB_NAME="$DB_NAME" \
  -f db/setup.sql
