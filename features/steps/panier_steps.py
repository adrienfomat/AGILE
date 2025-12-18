from behave import given, when, then

from PanierAchat import PanierAchat
from Produit import Produit


# GIVEN


@given("un panier vide")
def step_panier_vide(context):
    context.panier = PanierAchat()
    context.produits = {}


@given('un produit "{nom}" actif avec un prix de {prix:d} et un stock de {stock:d}')
def step_creer_produit(context, nom, prix, stock):
    produit = Produit(nom, prix, stock, True)

    if not hasattr(context, "produits") or context.produits is None:
        context.produits = {}

    context.produits[nom] = produit


@given('un panier contenant le produit "{nom}" avec une quantité de {quantite:d}')
def step_panier_avec_produit(context, nom, quantite):
    context.panier = PanierAchat()
    context.produits = {}

    # Prix/stock par défaut pour ce Given (suffisant pour les scénarios)
    produit = Produit(nom, 15, 50, True)
    context.produits[nom] = produit

    context.panier.ajouter_produit(produit, quantite)

# WHEN


@when('j\'ajoute {quantite:d} exemplaires du produit "{nom}" au panier')
@when('j\'ajoute {quantite:d} exemplaire du produit "{nom}" au panier')
def step_ajouter_produit(context, quantite, nom):
    produit = context.produits[nom]
    context.panier.ajouter_produit(produit, quantite)


@when('je supprime le produit "{nom}" du panier')
def step_supprimer_produit(context, nom):
    context.panier.supprimer_produit(nom)


@when("je consulte le panier")
def step_consulter_panier(context):
    # On l'appelle, mais les asserts sont faits dans les Then
    context.panier.afficher_panier()

# THEN


@then("le panier contient {nb:d} ligne")
def step_verifier_nombre_lignes(context, nb):
    assert len(context.panier.get_lignes()) == nb


@then('la quantité du produit "{nom}" est {quantite:d}')
def step_verifier_quantite(context, nom, quantite):
    assert context.panier.get_lignes()[nom].get_quantite() == quantite


@then("le panier est vide")
def step_panier_est_vide(context):
    assert len(context.panier.get_lignes()) == 0


@then("le total du panier est {total:d}")
def step_verifier_total(context, total):
    assert context.panier.calculer_total() == total
