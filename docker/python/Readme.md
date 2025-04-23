#Image server Python
```bash
docker build -t python-server .
docker run -p 8000:8000 python-server
```bash

##Créer un volume au lancement du conteneur
```bash
docker run -v volume1:/app -p 8000:8000 python-server
```bash

##Créer un volume
```bash
docker volume create volume1
```bash