## Running docker compose in detatched background mode

```bash
docker-compose up -d
```
### To shutdown

```bash
docker-compose down
```
## Running only django module

```bash
docker build --tag django-name-example .
```

```bash
docker run -d -p 8000:8000 --name whatever-name django-name-example
```
### To inspect what happens inside container

```bash
docker exec -it whatever-name bash
```

## In Progress

```bash
Add shp2pgsql postgis integration 
```

```bash
Improve UI
```
## TODO

```bash
Add GeoServer 
```
