# SuiviProjets - Application de Suivi de Projets de Recherche

## Description
Cette application permet de gérer des projets de recherche, des chercheurs impliqués, et les publications associées. Elle fournit une API complète et une interface utilisateur pour faciliter la gestion des informations.

## Prérequis
- Python 
- Django 
- Django REST Framework

## Installation
1. Clonez le dépôt :
    ```bash
    git clone https://github.com/ton-utilisateur/td-djangorestapi-NOM-PRENOM.git
    cd td-djangorestapi-NOM-PRENOM
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv env
    source env/bin/activate  
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations de la base de données :
    ```bash
    python manage.py migrate
    ```

5. Créez un superutilisateur pour accéder à l'admin :
    ```bash
    python manage.py createsuperuser
    ```

6. Lancez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

## Utilisation
### Accéder à l'interface d'administration
- Rendez-vous sur `http://127.0.0.1:8000/admin/` et connectez-vous avec les identifiants du superutilisateur.

### Tester l'API avec le fichier `.http`
- Utilisez un outil comme `Postman` ou un éditeur comme `VSCode` avec l'extension `REST Client` pour exécuter les requêtes dans le fichier `test.http`.

### Fonctionnalités de l'API
- **Chercheurs** :
  - Liste : `GET /api/chercheurs/`
  - Création : `POST /api/chercheurs/`
  - Détail : `GET /api/chercheurs/{id}/`
  - Mise à jour : `PUT /api/chercheurs/{id}/`
  - Suppression : `DELETE /api/chercheurs/{id}/`

- **Projets** :
  - Liste : `GET /api/projets/`
  - Création : `POST /api/projets/`
  - Détail : `GET /api/projets/{id}/`
  - Mise à jour : `PUT /api/projets/{id}/`
  - Suppression : `DELETE /api/projets/{id}/`

- **Publications** :
  - Liste : `GET /api/publications/`
  - Création : `POST /api/publications/`
  - Détail : `GET /api/publications/{id}/`
  - Mise à jour : `PUT /api/publications/{id}/`
  - Suppression : `DELETE /api/publications/{id}/`

## Authentification
- **Inscription** : `http://127.0.0.1:8000/register/`
- **Connexion** : `http://127.0.0.1:8000/accounts/login/`
- **Déconnexion** : `http://127.0.0.1:8000/accounts/logout/`

## Déploiement
Pour déployer cette application en production, suivez les recommandations de la documentation de Django concernant le déploiement, y compris la configuration du serveur web, la gestion des fichiers statiques, et la sécurité.

## Contributeurs
- Nom : {NOM}
- Prénom : {PRENOM}
