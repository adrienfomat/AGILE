image 1 & image 2 :  : On crée la classe PanierAchat, qui devient la classe principale du projet.
On définit le constructeur PanierAchat(), chargé d’initialiser l’objet.
On ajoute deux attributs :
articles
montantTotal
On met également en place les accesseurs associés pour pouvoir consulter l’état de l’objet.
Ensuite ,on compile la classe PanierAchat via le menu contextuel de BlueJ.
La compilation permet de vérifier que la classe et son constructeur PanierAchat() sont valides.

images 3.1 & 3.2 & 3.3
On instancie la classe en appelant le constructeur PanierAchat().
On crée un objet nommé panier1 à partir de la classe fétiche.
L’objet panier1 : PanierAchat apparaît dans l’Object Bench.
Cela confirme que le constructeur PanierAchat() a bien été exécuté et que l’objet existe.
On ajoute une seconde classe nommée Article au projet.
Cette classe est associée de manière unidirectionnelle à la classe fétiche PanierAchat, via l’attribut articles.
On inspecte l’objet panier1 pour visualiser ses attributs :
articles (initialisé par le constructeur)
montantTotal (initialisé à 0.0)
Cette inspection permet de constater l’état de l’objet après instanciation et après l’exécution du constructeur PanierAchat().


image 4 
On a ajouté 2 méthodes:
Une méthode ajouterArticle(Article article) est ajoutée pour modifier l’état de l’objet en ajoutant un article au panier.
Une méthode calculerTotalApresRemise(double pourcentage) est définie pour collaborer avec les objets Article afin de produire un résultat basé sur l’ensemble des articles du panier.

image 5
On visualise :
La classe PanierAchat est la classe fétiche du projet.
La classe Article est ajoutée comme seconde classe.
Une association unidirectionnelle est établie entre PanierAchat et Article.
Cette association correspond à l’utilisation de la classe Article par PanierAchat, notamment via l’attribut articles

images 6, 6.1, 6.2
On instancie deux objets Article en appelant le constructeur
Article(String nom, double prix) :
article1 avec le nom "PULL" et le prix 10.0
article2 avec le nom "JEAN" et le prix 40.0
Ces objets Article sont ensuite utilisés par l’objet panierAc1 : PanierAchat, créé précédemment via le constructeur PanierAchat().
On inspecte l’objet panierAc1 et on observe :
l’attribut articles, qui contient maintenant les objets article1 et article2,
l’attribut montantTotal, dont la valeur est passée à 50.0, ce qui reflète l’effet des méthodes appelées sur le panier.

image 7
On crée la classe de test PanierAchatTest associée à la classe PanierAchat.
Une fixture est définie avec les attributs panier, a1 et a2.
La méthode setUp() instancie le panier avec le constructeur PanierAchat(), crée deux articles avec le constructeur Article(String nom, double prix), puis les ajoute au panier.
La méthode tearDown() remet les objets à null après chaque test.

images 8.1,8.2
On exécute ensuite les tests unitaires :
testNombreArticles() vérifie l’état du panier après ajout des articles.
testMontantTotal() vérifie le résultat obtenu après l’utilisation des méthodes du panier.
Les résultats des tests s’affichent dans BlueJ avec une barre verte, indiquant que tous les tests ont réussi, sans erreurs ni échecs.
Enfin, le diagramme de classes montre la relation entre PanierAchatTest, PanierAchat et Article, confirmant que la classe de test utilise les deux classes pour valider leur collaboration.


