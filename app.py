import streamlit as st

st.title("Formatteur d'IDs pour Airtable")

# Zone de texte où tu colles ta liste d'IDs
ids_input = st.text_area("Collez ici votre liste d'identifiants", height=200)

if st.button("Formater"):
    # On découpe sur les espaces, nouvelles lignes, tabulations...
    ids_list = ids_input.replace(",", " ").split()
    # On filtre pour retirer les éventuels vides
    ids_list = [id_.strip() for id_ in ids_list if id_.strip()]
    # On join avec ", " comme séparateur
    formatted_ids = ", ".join(ids_list)
    
    st.text_area("Résultat formaté", formatted_ids, height=200)
    
    st.success("IDs formatés avec succès !")

