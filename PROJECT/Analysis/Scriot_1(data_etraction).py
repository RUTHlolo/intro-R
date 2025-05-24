# <editor-fold Importing libraries>
import pandas as pd
# </editor-fold>
# <editor-fold Loading dataset and concatenation>
filepath_Vit = "C:/Users/Admin/Documents/UdeM/PROJECT/Analysis/Extraction_Vitamines_2008-2025.xlsx"
Vit_A = pd.read_excel(filepath_Vit, sheet_name='Vitamine A')
print('Dimension of Vit_A dataset: ', Vit_A.shape)
print('Variable_name: ', Vit_A.columns)

Vit_B = pd.read_excel(filepath_Vit, sheet_name='b-Carotène')
print('Dimension of Vit_B dataset: ', Vit_B.shape)
print('Variable_name: ', Vit_B.columns)

Vit_E = pd.read_excel(filepath_Vit, sheet_name='Vitamine E')
print('Dimension of Vit_E dataset: ', Vit_E.shape)
print('Variable_name: ',Vit_E.columns)

Filepath_min = "C:/Users/Admin/Documents/UdeM/PROJECT/Analysis/Copie de Extraction_Selenium_2008-2025.xlsx"
selenium = pd.read_excel(Filepath_min)
print('Dimension of selenium dataset: ', selenium.shape)

Vit_Min_data = pd.concat([Vit_A, Vit_B, Vit_E,selenium])
print('Dimensionality: ', Vit_Min_data.shape)
Vit_Min_data.info()
# </editor-fold>
def compare_visits_sets(data1, data2, data3, data4):
    # Extract visit numbers as sets (drop missing values)
    set1 = set(data1['No Dossier Animal '].dropna())
    set2 = set(data2['No Dossier Animal '].dropna())
    set3 = set(data3['No Dossier Animal '].dropna())
    set4 = set(data4['No Dossier Animal '].dropna())

    # Check if all sets are the same
    if set1 == set2 == set3 == set4:
        print("✅ All visit numbers match across sheets (regardless of row).")
    else:
        print("❌ Visit numbers do not match:")
        if set1 != set2:
            print("- Main1 and Main2 differ by:", set1.symmetric_difference(set2))
        if set1 != set3:
            print("- Main1 and Main3 differ by:", set1.symmetric_difference(set3))
        if set1 != set4:
            print("- Main1 and Other differ by:", set1.symmetric_difference(set4))

compare_visits_sets(Vit_A, Vit_B, Vit_E, selenium)

## Identifying uniqueness
no_clinic = sorted(Vit_Min_data['Nom de la clinique '].dropna().unique())
print(no_clinic)
print(len(no_clinic))
ville_clinic = sorted(Vit_Min_data['Ville de la clinique '].dropna().unique())
print(ville_clinic)
print(len(ville_clinic))
species = sorted(Vit_Min_data['Espèce'].dropna().unique())
print(species)
print(len(species))
Species_count = Vit_Min_data['Espèce'].dropna().value_counts().head(5)
print(Species_count)


## Extracting Dataset only on Cows and Horses
new_vitM_data = Vit_Min_data[Vit_Min_data['Espèce'].isin(['BOVINE','EQUIN'])].copy()

print('Data type', type(new_vitM_data))
print('Data Dimension',new_vitM_data.shape)

new_vitM_data.to_excel('new_vitM_data.xlsx')
# </editor-fold>