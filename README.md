# EventHubDistributed - Système de Gestion d'Événements en Microservices

# EventHub Distributed

**Projet de Programmation Distribuée**  
**Master 1 VMI – Université Paris Cité**  
**Équipe :** Maria Aydin & Clara Ait Mokhtar
**Enseignant :** Benoît Charroux  
**Date :** Avril 2026

---

## Présentation du projet

**EventHub Distributed** est une application de gestion d’événements et de participants, construite avec une **architecture microservices** en Python (Django REST Framework).

L’application est entièrement **conteneurisée avec Docker**, publiée sur Docker Hub, et déployée sur un **cluster Kubernetes local** (Minikube). Elle met en œuvre les technologies imposées par le cours : microservices REST, Docker, Kubernetes, Ingress, base de données persistante MySQL et volumes persistants.

**Niveau atteint : 18/20** (volumes persistants + RBAC Kubernetes).  
Les étapes bonus (déploiement cloud + sécurisation avancée avec Istio/mTLS) n’ont pas été réalisées.

---

## 🛠 Stack Technique

| Composant              | Technologie utilisée                          |
|------------------------|-----------------------------------------------|
| Langage                | Python 3.12 + Django REST Framework           |
| Conteneurisation       | Docker (`python:3.12-slim`)                   |
| Orchestration          | Kubernetes via Minikube (v1.35.1)             |
| Registry               | Docker Hub (`mariaa04/ , claraaitm/`)                      |
| Ingress / Gateway      | NGINX Ingress Controller                      |
| Base de données        | MySQL 8.0.45                                  |
| Stockage fichiers      | PersistentVolume + PersistentVolumeClaim      |
| Namespace              | `eventhub`                                    |

---

## Architecture

L’application est composée de deux microservices REST indépendants :

- **`event-service`** : Gestion complète des événements (CRUD)
- **`participant-service`** : Gestion des participants + upload de fichiers (photos)

**Communication** : via le DNS interne Kubernetes (`http://eventservice:8000`)  
**Exposition** : via un **Ingress NGINX** sur `http://127.0.0.1` (minikube tunnel)  
**Persistance** : MySQL + volume partagé pour les fichiers médias (`/app/media/`)


---

## Comment lancer le projet

### Prérequis
- Docker Desktop
- Minikube + kubectl
- Git

### Étapes de déploiement

# 1. Démarrer Minikube
minikube start --driver=docker
kubectl create namespace eventhub

# 2. Activer Ingress
minikube addons enable ingress

# 3. Récupérer et charger les images Docker Hub
docker pull mariaa04/eventservice:latest
docker pull mariaa04/eventhub-participant:latest

minikube image load mariaa04/eventservice:latest
minikube image load mariaa04/eventhub-participant:latest

# 4. Déployer les ressources
git clone https://github.com/Mmajora53/EventHubDistributed.git
cd EventHubDistributed

kubectl apply -f k8s/db/mysql/mysql-secret.yaml -n eventhub
kubectl apply -f k8s/db/mysql/mysql-storage.yaml -n eventhub
kubectl apply -f k8s/db/mysql/mysql-deployment.yaml -n eventhub
kubectl apply -f k8s/db/mysql/mysql-serviceClusterIp.yaml -n eventhub

kubectl apply -f k8s/volumes/eventhub-storage.yaml

kubectl apply -f k8s/event-deployment.yaml -n eventhub
kubectl apply -f k8s/participant-deployment.yaml -n eventhub

# 5. Accéder à l’application
Dans un terminal séparé :
minikube tunnel

L’API est disponible sur http://127.0.0.1
Endpoints principaux :

- http://127.0.0.1/api/events/ → Gestion des événements
- http://127.0.0.1/api/participants/ → Gestion des participants (avec upload de fichiers)


## Arborescence

EventHubDistributed/
├── eventservice/               # Code du premier microservice
├── service-participant/        # Code du second microservice
├── k8s/                        # Tous les manifests Kubernetes
│   ├── db/mysql/
│   ├── volumes/
│   ├── rbac/
│   ├── event-deployment.yaml
│   └── participant-deployment.yaml
├── Dockerfile (dans chaque service)
└── README.md


## Contributeurs 

- Maria Aydin
- Clara Ait Mokhtar

(Avril 2026)
