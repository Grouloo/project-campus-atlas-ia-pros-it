import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Ventes par région
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')
print('ventes-par-région.html généré avec succès !')

# 5.a.i. Calcul du chiffre d'affaires par produit moyen
moyenne_ca = données.groupby('produit').apply(lambda x: (x['prix'] * x['qte']).mean())
print("\n-- Moyenne des chiffres d'affaires --")
print(moyenne_ca)

# 5.a.ii. Calcul du chiffre d'affaires par produit médian
mediane_ca = données.groupby('produit').apply(lambda x: (x['prix'] * x['qte']).median())
print("\n-- Médiane des chiffres d'affaires --")
print(mediane_ca)

# 5.a.i. Calcul du volume de vente moyen
moyenne_volume = données.groupby('produit')['qte'].mean()
print("\n-- Moyenne des volumes de vente --")
print(moyenne_volume)

# 5.a.ii. Calcul du chiffre d'affaires par produit médian
mediane_volume = données.groupby('produit')['qte'].median()
print("\n-- Médiane des volumes de ventes --")
print(mediane_volume)

# 5.b.i. Calcul de l'écart-type des volumes de ventes par produit
ecart_type_volume = données.groupby('produit')['qte'].std()
print("\n-- Écart-type des volumes de vente --")
print(ecart_type_volume)

# 5.b.ii. Calcul de la variance du volume des ventes par produit
variance_volume = données.groupby('produit')['qte'].var()
print("\n-- Variance des volumes de ventes --")
print(variance_volume)

# 6. Produit le plus vendu et le moins vendu
ventes_par_produit = {}

for index, row in données.iterrows():
    produit = row['produit']
    quantite = row['qte']
    
    if produit in ventes_par_produit:
        ventes_par_produit[produit] += quantite
    else:
        ventes_par_produit[produit] = quantite

produit_plus_vendu = None
max_ventes = 0

for produit, total_ventes in ventes_par_produit.items():
    if total_ventes > max_ventes:
        max_ventes = total_ventes
        produit_plus_vendu = produit

produit_moins_vendu = None
min_ventes = float('inf')

for produit, total_ventes in ventes_par_produit.items():
    if total_ventes < min_ventes:
        min_ventes = total_ventes
        produit_moins_vendu = produit

print(f"\nProduit le plus vendu : {produit_plus_vendu}")
print(f"Nombre d'unités vendues : {max_ventes}")
print(f"\nProduit le moins vendu : {produit_moins_vendu}")
print(f"Nombre d'unités vendues : {min_ventes}")


# 7. Graphiques des ventes par produit et du chiffre d'affaires par produit
figure_ventes = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')
figure_ventes.write_html('ventes-par-produit.html')

ca_par_produit = données.groupby('produit').apply(lambda x: (x['prix'] * x['qte']).sum()).reset_index()
ca_par_produit.columns = ['produit', 'ca']
figure_ca = px.pie(ca_par_produit, values='ca', names='produit', title="chiffre d'affaires par produit")
figure_ca.write_html('ca-par-produit.html')