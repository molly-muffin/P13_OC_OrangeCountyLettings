.. P13_OC_Orange_County_Lettings documentation master file, created by
   sphinx-quickstart on Tue Sep 19 22:43:16 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to P13_OC_Orange_County_Lettings's documentation!
=========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Guide de Développement Local pour Orange County Lettings
========================================================

.. contents:: Table des matières

Résumé
======

Ce guide vous oriente à travers le processus de configuration et de développement en local du site web Orange County Lettings, dans le cadre du Projet de Développeur Python OpenClassrooms numéro 13 : "Mise à l'échelle d'une application Django grâce à une architecture modulaire".

Ce projet constitue une version améliorée du projet "Python OC Lettings FR", que vous pouvez trouver sur GitHub à l'adresse suivante : https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git.

Les améliorations apportées à cette nouvelle version incluent :

1. **Refactorisation de la dette technique :** Une révision en profondeur a été effectuée pour réduire la dette technique et améliorer la qualité globale du code.

2. **Refactorisation de l'architecture modulaire :** L'architecture du projet a été repensée pour être plus modulaire, ce qui facilite la maintenance, l'extension et la compréhension du code.

3. **Surveillance des applications et des erreurs via Sentry :** L'intégration de Sentry permet une surveillance proactive des erreurs et des performances de l'application, offrant ainsi une meilleure visibilité sur les problèmes potentiels.

4. **Pipeline CI/CD utilisant CircleCI :** Un pipeline de CI/CD (Intégration Continue / Déploiement Continu) a été mis en place en utilisant CircleCI. Cela garantit des tests automatisés et un déploiement en continu du code.

5. **Déploiement sur Heroku :** L'application est déployée sur la plateforme Heroku, ce qui la rend accessible au public de manière simple et évolutive.

Ce guide vous accompagnera tout au long du processus pour que vous puissiez tirer pleinement parti de ces améliorations dans le cadre de votre développement avec Django.


Développement local
===================

Prérequis
---------
- Compte GitHub avec accès en lecture à ce dépôt
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

**Links**
* `Heroku for this project <https://https://young-sea-11153-2cd36d75aaec.herokuapp.com/>`_
* `DockerHub Images <https://hub.docker.com/repository/docker/mollymuffin/p13oc_orange_county_lettings/>`_
* `CircleCI for this project <https://app.circleci.com/pipelines/github/molly-muffin/P13_OC_Orange_County_Lettings?branch=master>`_


Cloner le dépôt
~~~~~~~~~~~~~~~

.. code-block:: shell

   git clone https://github.com/molly-muffin/P13_OC_Orange_County_Lettings.git

Créer l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   cd /chemin/vers/projet/
   python -m venv venv

Activer l'environnement
~~~~~~~~~~~~~~~~~~~~~~~

** Windows**

.. code-block:: shell

   venv\Scripts\activate

** MacOS and Linux**

.. code-block:: shell

   source venv/bin/activate

Désactiver l'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   deactivate

Exécuter le site
~~~~~~~~~~~~~~~~~

.. code-block:: shell

   cd /chemin/vers/projet/
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py runserver

Linting
-------

** Flake8 **

.. code-block:: shell

   cd /chemin/vers/projet/
   source venv/bin/activate
   flake8

** Tests unitaires **

.. code-block:: shell

   cd /chemin/vers/projet/
   source venv/bin/activate
   python manage.py test home
   python manage.py test lettings
   python manage.py test profiles

Panel d'administration
----------------------

- Ouvrez http://localhost:8000 dans un navigateur pour vérifier que le site fonctionne correctement.
- Accédez au panel d'administration en ouvrant http://localhost:8000/admin dans un navigateur.
- Connectez-vous avec l'utilisateur admin et le mot de passe Abc1234!


Déploiement
===========

Le déploiement nécessite :
- Compte CircleCi
- Compte Docker
- Compte Heroku
- Compte Sentry

Le déploiement est géré par le fichier ``config.yml`` présent dans le dossier ``./.circleci``.  
Ce fichier est déclenché lors d'un push vers le dépôt GitHub. Un push sur la branche ``master`` déclenche les tests pyth et flake8.  
Ensuite, l'application est conteneurisée avec Docker et déployée en ligne via Heroku.  

URL de l'application en ligne : https://young-sea-11153-2cd36d75aaec.herokuapp.com/

Dans le dépôt CircleCi, configurez les variables d'environnement (Project Settings > Environment Variables) :

- ``DOCKER_LOGIN`` : Votre identifiant DOCKERHUB
- ``DOCKER_PASSWORD`` : Votre mot de passe DOCKERHUB
- ``DOCKER_REPO`` Nom de votre dépôt DockerHub
- ``HEROKU_KEY`` : Clé de l'application HEROKU
- ``HEROKU_APP_NAME`` : Nom de l'application HEROKU
