import streamlit as st

st.title("Formatteur d'IDs (un par ligne) → Airtable")

ids_input = st.text_area(
    "Collez ici vos identifiants (un par ligne)",
    height=200,
    placeholder="ID1\nID2\nID3\n..."
)

# Reformater en temps réel
if ids_input.strip():
    # On sépare par lignes
    ids_list = ids_input.strip().split("\n")
    # On retire les espaces inutiles
    ids_list = [id_.strip() for id_ in ids_list if id_.strip()]
    # On met dans le format voulu
    formatted_ids = ", ".join(ids_list)
    
    st.text_area("Résultat formaté", formatted_ids, height=200)
else:
    st.info("Collez vos IDs ci-dessus pour voir le résultat.")
