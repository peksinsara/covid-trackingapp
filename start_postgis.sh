docker run \
--name "covid_tracking-postgis" \
-p 25432:5432 \
-d -t kartoza/postgis \
-e POSTGRES=postgres \
-e POSTGRES_PASS=postgres \
-e POSTGRES_DBNAME=postgres