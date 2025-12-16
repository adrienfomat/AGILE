# 🛒 Projet Panier d’Achat – Java (BlueJ)

## 📌 Contexte du projet
Ce projet a pour objectif de modéliser un **système de panier d’achat en Java** en utilisant les principes de la **programmation orientée objet (POO)**.  
Il met en œuvre des classes, des objets, des associations entre classes ainsi que des **tests unitaires** à l’aide de l’environnement **BlueJ**.

Le système permet :
- d’ajouter des articles à un panier,
- de calculer le montant total,
- d’appliquer une remise en pourcentage,
- de vérifier le bon fonctionnement via des tests unitaires.

---

## 🧩 Classes principales

### 🔹 PanierAchat
Classe principale (classe fétiche du projet).

**Attributs :**
- `articles` : collection d’objets `Article`
- `montantTotal` : montant total du panier

**Méthodes principales :**
- `ajouterArticle(Article article)` : ajoute un article au panier
- `calculerTotalApresRemise(double pourcentage)` : calcule le total après remise

Le constructeur `PanierAchat()` initialise la liste des articles et le montant total à `0.0`.

---

### 🔹 Article
Classe représentant un article du panier.

**Attributs :**
- `nom` : nom de l’article
- `prix` : prix de l’article

**Constructeur :**
- `Article(String nom, double prix)`

Cette classe est utilisée par `PanierAchat` via une **association unidirectionnelle**.

---

### 🔹 PanierAchatTest
Classe de **tests unitaires** permettant de valider le comportement de `PanierAchat`.

**Fonctionnalités :**
- Initialisation des objets dans `setUp()`
- Nettoyage des objets dans `tearDown()`
- Vérification :
  - du nombre d’articles (`testNombreArticles`)
  - du montant total (`testMontantTotal`)

Les tests s’exécutent avec succès dans BlueJ (barre verte).

---

## ⚙️ Déroulement du projet

1. Création de la classe `PanierAchat` et de son constructeur
2. Ajout des attributs et accesseurs
3. Compilation et instanciation d’un objet `panier1`
4. Création de la classe `Article`
5. Ajout de méthodes métier dans `PanierAchat`
6. Instanciation de plusieurs objets `Article` (ex : PULL, JEAN)
7. Ajout des articles au panier et mise à jour du montant total
8. Création et exécution des tests unitaires
9. Validation via le diagramme de classes

---

## 🎯 Objectifs pédagogiques

- Comprendre la **modélisation objet**
- Manipuler des **collections d’objets**
- Mettre en place une **association entre classes**
- Utiliser des **constructeurs et méthodes**
- Apprendre les **tests unitaires** avec BlueJ

---

## ✅ Résultat
Le projet fonctionne correctement :
- les articles sont ajoutés au panier,
- le montant total est calculé correctement,
- les tests unitaires passent sans erreur.

---

## 🚀 Pistes d’amélioration
- Supprimer un article du panier
- Ajouter des remises spécifiques par article
- Gérer la persistance du panier (fichier ou base de données)
