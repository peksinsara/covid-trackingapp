docker run \
--name "covid_tracking-postgis" \
-p 25432:5432 \
-d -t kartoza/postgis \
-e POSTGRES=covid_tracking \
-e POSTGRES_PASS=covid_tracking \
-e POSTGRES_DBNAME=covid_tracking