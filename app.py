import pickle

import streamlit as st
import numpy as np
from sklearn import svm
load_model=pickle.load(open('C:/ProgramData/Anaconda3/envs/djegui/deployement_machine_learning/modelWAGUE.PKL','rb'))
def diabete_prediction(entree_data):
    tableau_numpy = np.array(entree_data)
    input_data_reshape = tableau_numpy.reshape(1, -1)
    prediction = load_model.predict(input_data_reshape)

    if (prediction[0]) == 1:
        return " La personne est  diabetique"
    else:
        return "La personne n'est pas  diabetique"

def main():

    st.title("APPLICATION MOBILE POUR LA DETECTION DE DIABETE")
    st.subheader("(AUTEUR: Mr.DJEGUI_WAGUE)")

    #   on crée un fonction aui permet de telecharger nos données
  #  @st.cache(persist=True)
  #  def load_data():
   #   data=pd.read_csv("diabetes.csv")
    #    return data
    #    affichage de la dataset
    #     df= load_data()
     #    df_sample=  df.sample(100)
    #if st.sidebar.checkbox("AFFICHER LES DONNEES BRUTE" ,False):
     #      st.subheader("Jeu de données diabete : echantillon de 100 observations ")
     #      st.write(df_sample)

    Pregnancies = st.number_input('Nombre de fois enceinte', 0, 20, 0)
    Glucose = st.number_input('Taux de glucose', 0, 200, 100)
    BloodPressure = st.number_input('Pression arterielle', 0, 200, 50)
    SkinThickness = st.number_input('Epaisseur de Peau', 0, 200, 30)
    Insulin = st.number_input("INSULIN", 0, 200, 95)
    BMI = st.number_input('Indice de masse corporelle', 0, 200, 5)
    DiabetesPedigreeFunction = st.number_input('FonctionPedigreeDiabete', 0, 100, 0)
    Age = st.number_input('Votre age ', 0, 200, 18)
    # creer code de prediction
    diagnostique = ""
    if st.button("resultat_du_rest_diabetique"):
        diagnostique = diabete_prediction(
            [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    st.success(diagnostique)





if __name__ == "__main__":
    main()


#   streamlit run app.py





