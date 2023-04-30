
## Installation 

Il faut télécharger dans un premier temps les modules python, les modules sont dans le fichier requirements.txt 

Ensuite, dans un terminal, faite : 

```bash
  cd client 
```

Puis taper la commande, pour installer toutes les dépendances du serveur NodeJs

```bash
  npm install 
```

```bash
  npm run serve  
```

Puis à la racine du projet taper : 

```bash
  uvicorn main:app --reload 
```

Une fois l'API lancer, allez dans la base MongoDb pour pouvoir mettre l'administrateur, l'administrateur ce trouve dans le dossier json "admin.json"

Pour acceder à l'espace d'administration il faut saisir coté API : 
```bash
  /admin/login 
```

Les identifiant administrateur sont : 
- Login : admin 
- Mot de passe : admin 


## Ce qui n'a pas étais fait : 
- Les sockets 
- Le faite de pouvoir changer de musique avec les boutons ">" et "<" 
- La supression des playlist et des musiques 
- La page profil (par manque de temps)
