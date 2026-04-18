# EventHubDistributed - Système de Gestion d'Événements en Microservices

**Live Application :** [CLICK HERE](https://eventhub-webproject.vercel.app)

Ce repository contient le projet final du cours **Programmation Distribuée** (enseigné par Benoit Charroux).

**EventHubDistributed** est une application full-stack complète de gestion d’événements et de participants, repensée sous forme d’**architecture microservices** afin de respecter les contraintes imposées du projet :
- Microservices (REST et/ou gRPC – bonus)
- Docker / Kubernetes
- Option : déploiement cloud + front-end

Le projet a été développé en **binôme** à partir du code existant d’EventHub, en le découpant en plusieurs microservices communicants.

## Membres de l’équipe
* **Clara AIT MOKHTAR**
* **Maria AYDIN**

## Fonctionnalités principales
* Authentification & Autorisation (token-based avec rôles Admin/Editor vs Viewer)
* Gestion complète des événements (CRUD + filtres par statut/date)
* Gestion des participants (CRUD)
* Inscription aux événements (relation Many-to-Many sans doublons)
* Tableau de bord interactif avec résumés et profils utilisateurs
* Mode sombre/clair

## Stack technique
* **Microservices Backend** : Node.js / Express (service principal) + adaptation Django ou second service selon avancement
* **Communication** : REST (gRPC en option bonus)
* **Frontend** : React 19 + Vite + React Router + Axios
* **Containerisation** : Docker (Dockerfile par service)
* **Orchestration** : Kubernetes (déploiements, services, Ingress, option Service Mesh)
* **Base de données** : PostgreSQL / MySQL (ou in-memory pour démarrage)
* **Options réalisées** : Gateway (Ingress ou Istio), volumes, RBAC, mTLS, déploiement cloud

## Structure du projet

EventHubDistributed/
├── service-event/          # Microservice Gestion des événements
├── service-participant/    # Microservice Gestion des participants (ou autre)
├── frontend/               # Application React
├── k8s/                    # Manifests Kubernetes (deployments, services, ingress, istio, etc.)
├── docker-compose.yml      # Pour démarrage local facile
├── Dockerfile (par service)
└── README.md


## Installation & Lancement

### 1. Lancement local (un seul service – niveau 10/20)
```bash
# Aller dans le service choisi
```bash
cd service-event
docker build -t eventhub-event:latest .
docker run -p 8080:8080 eventhub-event:latest


### 2. Lancement complet avec Docker Compose (deux services + DB)
docker-compose up --build

### 3. Déploiement Kubernetes (Minikube ou cluster)
```bash
# Appliquer les manifests
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/

### 4. Ajout de la Gateway / Service Mesh (niveau 12/20 et +
Voir le dossier k8s/istio/ ou k8s/ingress/.

Un premier microservice en local (Docker + K8s)
 - Deuxième microservice + communication inter-services
 - Gateway (Ingress / Service Mesh)
 - Base de données persistante (PostgreSQL/MySQL)
 - Accès à un système de fichiers (volumes)
 - Sécurité du cluster (RBAC, mTLS, sécurité registry, HTTPS)
 - Déploiement cloud (option bonus – en cours / terminé selon avancement)


Projet réalisé dans le cadre du cours de Programmation Distribuée – Master VMI.
Toutes les technologies et patterns imposés ont été intégrés.
