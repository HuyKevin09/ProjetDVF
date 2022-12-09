import pandas as pd
import numpy as np

f4 = pd.read_csv("./data/full_2019.csv", on_bad_lines='skip', low_memory=False, dtype={"longitude": np.float64, "latitude": np.float64})
f4["date_mutation"] = pd.to_datetime(f4["date_mutation"], format="%Y/%m/%d")
f4.drop_duplicates(inplace=True)


f4.dropna(subset=["longitude", "latitude", "type_local"], inplace=True)


def get_month(dt):
    return dt.month


def get_year(dt):
    return dt.year
# AJOUT DE NOUVELLES COLONNES


f4["month"] = f4["date_mutation"].map(get_month)

f4["year"] = f4["date_mutation"].map(get_year)

f4["m2"] = f4["valeur_fonciere"]/f4["surface_reelle_bati"]

f4 = f4[(f4["latitude"] < 48.882449) & (f4["latitude"] > 48.840321) &
        (f4["longitude"] < 2.832997) & (f4["longitude"] > 2.754977)]

f4.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\full_2019.csv")

# f4 = f4[["id_mutation", "date_mutation", "nature_mutation", "valeur_fonciere", "adresse_nom_voie",
#          "code_commune", "nom_commune", "nombre_lots", "type_local", "surface_reelle_bati",
#          "nombre_pieces_principales", "longitude", "latitude", "month", "year", "m2"]]
#
# f4 = f4[(f4["nature_mutation"] == "Vente") & (f4["type_local"] == "Appartement") &
#         (f4["latitude"] < 48.882449) & (f4["latitude"] > 48.840321) &
#         (f4["longitude"] < 2.832997) & (f4["longitude"] > 2.754977)]
#
# f4.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\disney2019.csv")