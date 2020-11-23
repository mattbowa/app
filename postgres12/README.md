# Build a postgres 12 image called 'postgres12'
docker build -t postgres12 .


# TESTING
Make initial run to set password 'matt1234'
docker run --rm -P --name postgres12_test -e POSTGRES_PASSWORD=matt1234 postgres12

To connect to the postgres container with PSQL
psql -h localhost -p <port_number> -d postgres -U postgres --password

CREATE TABLE cities (
    name            varchar(80),
    location        point
);
INSERT INTO cities VALUES ('Mexico', '(-194.0, 53.0)');


psql -h localhost -p 6000 -d postgres -U postgres --password
