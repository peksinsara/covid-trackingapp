docker run \
--name "covid_tracking-postgis" \
-p 25432:5432 \
-d -t kartoza/postgis \
-e POSTGRES=postres \
-e POSTGRES_PASS=postres \
-e POSTGRES_DBNAME=postres