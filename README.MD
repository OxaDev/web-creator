## Environnement Python
```
python -m venv venv
``` 
### Activation de l'environnement python
Windows
```
venv\Scripts\activate
```

Unix
```
source venv\bin\activate
```

## Déploiement de l'application
Lancer le docker compose
```
docker compose up --build -d
```
L'application est ensuite accessible sur
http://localhost:25900/admin (admin Django)
`http://localhost:25900/htmls/<path>` (les rendus de pages html)

### Créer le premier utilisateur
`docker exec -it django_app python manage.py createsuperuser`