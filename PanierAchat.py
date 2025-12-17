from LignePanier import LignePanier

class PanierAchat:

    # Constructeur
    def __init__(self):
        # Attributs : état du panier
        self.lignes = {}

    # Ajout d'un produit
    def ajouter_produit(self, produit, quantite):
        if not produit.est_actif() or quantite < 1 or quantite > produit.get_stock():
            print("Impossible d'ajouter le produit :", produit.get_nom())
            return

        nom_produit = produit.get_nom()

        if nom_produit in self.lignes:
            ligne = self.lignes[nom_produit]
            nouvelle_qte = ligne.get_quantite() + quantite
            if nouvelle_qte > produit.get_stock():
                print("Stock insuffisant pour", nom_produit)
                return
            ligne.set_quantite(nouvelle_qte)
        else:
            self.lignes[nom_produit] = LignePanier(produit, quantite)

        print(quantite, nom_produit, "ajoutés au panier.")

    # Suppression d'un produit
    def supprimer_produit(self, nom_produit):
        if nom_produit in self.lignes:
            del self.lignes[nom_produit]
            print(nom_produit, "supprimé du panier.")
        else:
            print("Produit absent du panier.")

    # Calcul du total
    def calculer_total(self):
        total = 0.0
        for ligne in self.lignes.values():
            total += ligne.get_sous_total()
        return total

    # Affichage du panier
    def afficher_panier(self):
        if not self.lignes:
            print("Panier vide.")
            return

        for ligne in self.lignes.values():
            print(ligne)

        print("Total général :", self.calculer_total())

    # Getter pour tests unitaires
    def get_lignes(self):
        return self.lignes
