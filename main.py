""" Import of libraries """
import pandas as pd
import requests
import streamlit as st
import numpy as np
import plotly.express as px
from streamlit_lottie import st_lottie
from bokeh.plotting import figure


def main():
    # Chargement de datasets
    @st.experimental_memo
    def loading(file1: str, file2: str, file3: str, file4: str, file5: str):
        f1 = pd.read_csv(file1, on_bad_lines='skip', dtype={"longitude": np.float64, "latitude": np.float64})
        f2 = pd.read_csv(file2, on_bad_lines='skip', dtype={"longitude": np.float64, "latitude": np.float64})
        f3 = pd.read_csv(file3, on_bad_lines='skip', dtype={"longitude": np.float64, "latitude": np.float64})
        f4 = pd.read_csv(file4, on_bad_lines='skip', dtype={"longitude": np.float64, "latitude": np.float64})
        f5 = pd.read_csv(file5, on_bad_lines='skip', dtype={"longitude": np.float64, "latitude": np.float64})
        return f1, f2, f3, f4, f5

    def get_month(dt):
        return dt.month

    def get_year(dt):
        return dt.year

    # Nettoyage
    def cleaning(f1: pd.DataFrame, f2: pd.DataFrame, f3: pd.DataFrame, f4: pd.DataFrame, f5: pd.DataFrame):
        f1["date_mutation"] = pd.to_datetime(f1["date_mutation"], format="%Y/%m/%d")
        f2["date_mutation"] = pd.to_datetime(f2["date_mutation"], format="%Y/%m/%d")
        f3["date_mutation"] = pd.to_datetime(f3["date_mutation"], format="%Y/%m/%d")
        f4["date_mutation"] = pd.to_datetime(f4["date_mutation"], format="%Y/%m/%d")
        f5["date_mutation"] = pd.to_datetime(f5["date_mutation"], format="%Y/%m/%d")

        # ON SUPPRIME LES DOUBLONS
        f1.drop_duplicates(inplace=True)
        f2.drop_duplicates(inplace=True)
        f3.drop_duplicates(inplace=True)
        f4.drop_duplicates(inplace=True)
        f5.drop_duplicates(inplace=True)

        # PROBLEME AVEC VALEURS NA
        f1.dropna(subset=["longitude", "latitude", "type_local"], inplace=True)
        f2.dropna(subset=["longitude", "latitude", "type_local"], inplace=True)
        f3.dropna(subset=["longitude", "latitude", "type_local"], inplace=True)
        f4.dropna(subset=["longitude", "latitude", "type_local"], inplace=True)
        f5.dropna(subset=["longitude", "latitude", "type_local"], inplace=True)

        # AJOUT DE NOUVELLES COLONNES

        f1["month"] = f1["date_mutation"].map(get_month)
        f2["month"] = f2["date_mutation"].map(get_month)
        f3["month"] = f3["date_mutation"].map(get_month)
        f4["month"] = f4["date_mutation"].map(get_month)
        f5["month"] = f5["date_mutation"].map(get_month)

        f1["year"] = f1["date_mutation"].map(get_year)
        f2["year"] = f2["date_mutation"].map(get_year)
        f3["year"] = f3["date_mutation"].map(get_year)
        f4["year"] = f4["date_mutation"].map(get_year)
        f5["year"] = f5["date_mutation"].map(get_year)

        f1["m2"] = f1["valeur_fonciere"]/f1["surface_reelle_bati"]
        f2["m2"] = f2["valeur_fonciere"]/f3["surface_reelle_bati"]
        f3["m2"] = f3["valeur_fonciere"]/f2["surface_reelle_bati"]
        f4["m2"] = f4["valeur_fonciere"]/f4["surface_reelle_bati"]
        f5["m2"] = f5["valeur_fonciere"]/f5["surface_reelle_bati"]

        # REMPLACEMENT DES FICHIERS CSV
        # f1.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\full_2016.csv")
        # f2.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\full_2017.csv")
        # f3.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\full_2018.csv")
        # f4.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\full_2019.csv")
        # f5.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\full_2020.csv")

        return f1, f2, f3, f4, f5

    # Filtrage des colonnes
    def filtering(f1: pd.DataFrame, f2: pd.DataFrame, f3: pd.DataFrame, f4: pd.DataFrame, f5: pd.DataFrame):
        f1 = f1[["id_mutation", "date_mutation", "nature_mutation", "valeur_fonciere", "adresse_nom_voie",
                 "code_commune", "nom_commune", "nombre_lots", "type_local", "surface_reelle_bati",
                 "nombre_pieces_principales", "longitude", "latitude", "month", "year", "m2"]]
        f2 = f2[["id_mutation", "date_mutation", "nature_mutation", "valeur_fonciere", "adresse_nom_voie",
                 "code_commune", "nom_commune", "nombre_lots", "type_local", "surface_reelle_bati",
                 "nombre_pieces_principales", "longitude", "latitude", "month", "year", "m2"]]
        f3 = f3[["id_mutation", "date_mutation", "nature_mutation", "valeur_fonciere", "adresse_nom_voie",
                 "code_commune", "nom_commune", "nombre_lots", "type_local", "surface_reelle_bati",
                 "nombre_pieces_principales", "longitude", "latitude", "month", "year", "m2"]]
        f4 = f4[["id_mutation", "date_mutation", "nature_mutation", "valeur_fonciere", "adresse_nom_voie",
                 "code_commune", "nom_commune", "nombre_lots", "type_local", "surface_reelle_bati",
                 "nombre_pieces_principales", "longitude", "latitude", "month", "year", "m2"]]
        f5 = f5[["id_mutation", "date_mutation", "nature_mutation", "valeur_fonciere", "adresse_nom_voie",
                 "code_commune", "nom_commune", "nombre_lots", "type_local", "surface_reelle_bati",
                 "nombre_pieces_principales", "longitude", "latitude", "month", "year", "m2"]]

        # # SELECTION DES ATTRIBUTS QUI NOUS INTERESSENT
        # f1 = f1[(f1["nature_mutation"] == "Vente") & (f1["type_local"] == "Appartement") &
        #         (f1["latitude"] < 48.882449) & (f1["latitude"] > 48.840321) &
        #         (f1["longitude"] < 2.832997) & (f1["longitude"] > 2.754977)]
        #
        # f2 = f2[(f2["nature_mutation"] == "Vente") & (f2["type_local"] == "Appartement") &
        #         (f2["latitude"] < 48.882449) & (f2["latitude"] > 48.840321) &
        #         (f2["longitude"] < 2.832997) & (f2["longitude"] > 2.754977)]
        #
        # f3 = f3[(f3["nature_mutation"] == "Vente") & (f3["type_local"] == "Appartement") &
        #         (f3["latitude"] < 48.882449) & (f3["latitude"] > 48.840321) &
        #         (f3["longitude"] < 2.832997) & (f3["longitude"] > 2.754977)]
        #
        # f4 = f4[(f4["nature_mutation"] == "Vente") & (f4["type_local"] == "Appartement") &
        #         (f4["latitude"] < 48.882449) & (f4["latitude"] > 48.840321) &
        #         (f4["longitude"] < 2.832997) & (f4["longitude"] > 2.754977)]
        #
        # f5 = f5[(f5["nature_mutation"] == "Vente") & (f5["type_local"] == "Appartement") &
        #         (f5["latitude"] < 48.882449) & (f5["latitude"] > 48.840321) &
        #         (f5["longitude"] < 2.832997) & (f5["longitude"] > 2.754977)]

        # CREATION DE NOUVEAUX FICHIERS AVEC LES DONNEES QUI NOUS INTERESSENT
        # f1.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\disney2016.csv")
        # f2.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\disney2017.csv")
        # f3.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\disney2018.csv")
        # f4.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\disney2019.csv")
        # f5.to_csv(r"C:\Users\king-\Documents\Master\ProjectDVF\data\disney2020.csv")

        return f1, f2, f3, f4, f5

    # Sampling
    @st.experimental_memo
    def sampling(f1: pd.DataFrame, f2: pd.DataFrame, f3: pd.DataFrame, f4: pd.DataFrame, f5: pd.DataFrame):
        return f1.sample(frac=0.05), f2.sample(frac=0.05), f3.sample(frac=0.05), f4.sample(frac=0.05), \
               f5.sample(frac=0.05)

    # Diagramme circulaires
    @st.experimental_memo(suppress_st_warning=True)
    def show_pies(f1: pd.DataFrame, f2: pd.DataFrame, f3: pd.DataFrame, f4: pd.DataFrame, f5: pd.DataFrame):
        return px.pie(f1, names="type_local",
                      title="Proportion de demande de ventes par type de local"), \
               px.pie(f2, names="type_local",
                      title="Proportion de demande de ventes par type de local"), \
               px.pie(f3, names="type_local",
                      title="Proportion de demande de ventes par type de local"), \
               px.pie(f4, names="type_local",
                      title="Proportion de demande de ventes par type de local"),\
               px.pie(f5, names="type_local",
                      title="Proportion de demande de ventes par type de local")

    # Maps
    @st.experimental_memo
    def show_maps(f1: pd.DataFrame, f2: pd.DataFrame, f3: pd.DataFrame, f4: pd.DataFrame, f5: pd.DataFrame):
        return f1[["longitude", "latitude"]], f2[["longitude", "latitude"]], f3[["longitude", "latitude"]], \
               f4[["longitude", "latitude"]], f5[["longitude", "latitude"]]

    # Premier onglet de l'application
    def show_evolution(f1: pd.DataFrame, f2: pd.DataFrame, f3: pd.DataFrame, f4: pd.DataFrame, f5: pd.DataFrame):
        st.title("Évolution du marché au Val d'Europe Agglomération")

        # DIAGRAMME
        st.subheader("Nombre de ventes par année")
        labels = ["2016", "2017", "2018", "2019", "2020"]
        ventes = [len(f1), len(f2), len(f3), len(f4), len(f5)]
        fig = figure(x_range=labels, width=800, height=400, x_axis_label="Année", y_axis_label="Nombre de ventes")
        fig.vbar(x=labels, top=ventes, width=0.7)
        st.bokeh_chart(fig)

        # DIAGRAMME
        st.subheader("Découvrez le marché de l'immobilier de Val d'Europe Agglomération !")
        st.write("Regardons quelques chiffres")
        c1, c2 = st.columns(2)
        pie16, pie17, pie18, pie19, pie20 = show_pies(dvf16_filtered, dvf17_filtered, dvf18_filtered, dvf19_filtered,
                                                      dvf20_filtered)
        map16, map17, map18, map19, map20 = show_maps(f1, f2, f3, f4, f5)
        annee = c1.selectbox(
            'Sélectionnez une année : ', (2016, 2017, 2018, 2019, 2020)
        )
        if annee == 2016:
            c2.plotly_chart(pie16)
        elif annee == 2017:
            c2.plotly_chart(pie17)
        elif annee == 2018:
            c2.plotly_chart(pie18)
        elif annee == 2019:
            c2.plotly_chart(pie19)
        else:
            c2.plotly_chart(pie20)
        maps = st.select_slider(
            'Selectionnez une année : ',
            options=["2016", "2017", "2018", "2019", "2020"])
        st.subheader("Ventes d'appartements au Val d'Europe Agglomération ", str(maps))
        if maps == "2016":
            st.map(map16)
        elif maps == "2017":
            st.map(map17)
        elif maps == "2018":
            st.map(map18)
        elif maps == "2019":
            st.map(map19)
        else:
            st.map(map20)

    # Deuxieme onglet de l'application
    def show_why(f1: pd.DataFrame, f2: pd.DataFrame, f3: pd.DataFrame, f4: pd.DataFrame, f5: pd.DataFrame):
        st.title("Pourquoi pas venir investir ici ?")

        # DIAGRAMME
        st.subheader("Voici un apperçu des chiffres en 2020:")
        c1, c2 = st.columns(2)
        m2 = c1.checkbox("Prix au mètre carré", value=False)
        surface = c2.checkbox("Surface et nombre de pièces", value=False)
        if m2 and surface:
            st.write(
                f5[["nom_commune", "valeur_fonciere", "m2", "surface_reelle_bati", "nombre_pieces_principales"]]
                .groupby("nom_commune").median())
        elif m2 and not surface:
            st.write(f5[["nom_commune", "valeur_fonciere", "m2"]].groupby("nom_commune").median())
        elif not m2 and surface:
            st.write(f5[["nom_commune", "valeur_fonciere", "surface_reelle_bati", "nombre_pieces_principales"]]
                     .groupby("nom_commune").median())
        else:
            st.write(f5[["nom_commune", "valeur_fonciere"]].groupby("nom_commune").median())

        # DIAGRAMME
        st.subheader("Regardons les valeurs foncières médianes au cours des années")
        ventes = pd.DataFrame([{"2016": f1["valeur_fonciere"].median(), "2017": f2["valeur_fonciere"].median(),
                                "2018": f3["valeur_fonciere"].median(), "2019": f4["valeur_fonciere"].median(),
                                "2020": f5["valeur_fonciere"].median()}],
                              columns=["2016", "2017", "2018", "2019", "2020"]).transpose()
        m2_commune = px.bar(ventes, labels={"index": "Année", "value": "Valeur foncière"})
        st.plotly_chart(m2_commune)

        # DIAGRAMME
        st.subheader("Regardons les valeurs médianes des appartements au cours des mois :")
        extreme = st.checkbox("Supprimer valeur extrême", value=False)
        if extreme:
            f2bis = f2.drop(f2[f2["valeur_fonciere"] > 2000000].index)
            st.line_chart(pd.DataFrame(
                {"2016": f1[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"],
                 "2017": f2bis[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"],
                 "2018": f3[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"],
                 "2019": f4[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"],
                 "2020": f5[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"]},
                columns=["2016", "2017", "2018", "2019", "2020"]
            ))
        else:
            st.line_chart(pd.DataFrame(
                {"2016": f1[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"],
                 "2017": f2[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"],
                 "2018": f3[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"],
                 "2019": f4[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"],
                 "2020": f5[["valeur_fonciere", "month"]].groupby("month").median()["valeur_fonciere"]},
                columns=["2016", "2017", "2018", "2019", "2020"]))

        # DIAGRAMME
        st.subheader("Regardons le prix médian au mètre carré des communes alentours en 2020 : ")
        m2_commune = px.bar(f5[["nom_commune", "m2", "valeur_fonciere"]].groupby("nom_commune").median(),
                            color="valeur_fonciere")
        st.plotly_chart(m2_commune)

        # DIAGRAMME
        st.subheader("Regardons la répartition des surfaces des appartements par commune en 2020: ")
        surface_commune = px.box(f5, x="nom_commune", y="surface_reelle_bati")
        st.plotly_chart(surface_commune)

    # Troisieme onglet de l'application
    def show_sources(f5: pd.DataFrame):
        c1, c2 = st.columns(2)
        c1.subheader("Nom des colonnes")
        c1.write(f5.columns)

        c2.subheader("Type des colonnes")
        c2.write(f5.dtypes)

        st.subheader("Description rapide du dataset")
        st.write(f5.describe())

        c1, c2 = st.columns(2)
        c1.subheader("Premières lignes du dataset")
        c1.write(f5.head(10))

        c2.subheader("Dernières lignes du dataset")
        c2.write(f5.tail(10))

        # Val d'Europe Agglo
        st.subheader("Encadrement géographique de Val d'Europe Agglomération")
        c0, c1, c2, c3, c4 = st.columns(5)
        c0.write("")
        c0.write("")
        c0.write("")
        c0.write("Longitude")
        c0.write("Latitude")
        c1.write("NO")
        c1.write(2.754977)
        c1.write(48.882449)
        c2.write("SO")
        c2.write(2.754977)
        c2.write(48.840321)
        c3.write("NE")
        c3.write(2.832997)
        c3.write(48.882449)
        c4.write("SE")
        c4.write(2.832997)
        c4.write(48.840321)

    # Charger une image qui bouge
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Barre d'onglets sur le cote
    def create_sidebar(f1: pd.DataFrame, f2: pd.DataFrame, f3: pd.DataFrame, f4: pd.DataFrame, f5: pd.DataFrame):
        with st.sidebar:
            st_lottie(load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_WxdqKO.json"))

        sidebar = st.sidebar.selectbox(
            "Bienvenue sur le comparateur immobilier de Val d'Europe Agglomération",
            ("Évolution du marché", "Pourquoi acheter ici ?", "Des sources techniques"))

        if sidebar == "Évolution du marché":
            show_evolution(f1, f2, f3, f4, f5)
        elif sidebar == "Pourquoi acheter ici ?":
            show_why(f1, f2, f3, f4, f5)
        elif sidebar == "Des sources techniques":
            show_sources(f5)

    # DATA LOADING
    dvf16, dvf17, dvf18, dvf19, dvf20 = loading("./data/full_2016.csv", "./data/full_2017.csv", "./data/full_2018.csv",
                                                "./data/full_2019.csv", "./data/full_2020.csv")
    dvf_disney16, dvf_disney17, dvf_disney18, dvf_disney19, dvf_disney20 = loading("./data/disney2016.csv",
                                                                                   "./data/disney2017.csv",
                                                                                   "./data/disney2018.csv",
                                                                                   "./data/disney2019.csv",
                                                                                   "./data/disney2020.csv")

    # Sampling
    # dvf_disney16_sample, dvf_disney17_sample, dvf_disney18_sample, dvf_disney19_sample, dvf_disney20_sample = \
    #     sampling(dvf_disney16, dvf_disney17, dvf_disney18, dvf_disney19, dvf_disney20)

    dvf16_cleaned, dvf17_cleaned, dvf18_cleaned, dvf19_cleaned, dvf20_cleaned = cleaning(dvf16, dvf17, dvf18, dvf19,
                                                                                         dvf20)
    dvf16_filtered, dvf17_filtered, dvf18_filtered, dvf19_filtered, dvf20_filtered = filtering(dvf16_cleaned,
                                                                                               dvf17_cleaned,
                                                                                               dvf18_cleaned,
                                                                                               dvf19_cleaned,
                                                                                               dvf20_cleaned)

    create_sidebar(dvf_disney16, dvf_disney17, dvf_disney18, dvf_disney19, dvf_disney20)


if __name__ == '__main__':
    main()
