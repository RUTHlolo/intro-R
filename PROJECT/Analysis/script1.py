# <editor-fold Importing libraries>
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
# </editor-fold>

# <editor-fold data imputing>
filepath = "new_vitM_data"
new_vit_data = pd.read_excel(filepath)
# </editor-fold>
#<editor-fold Data cleaning 1: Age>
new_vit_data.info()
###Step 1: observing the data structure of the variables. no. of float, integer and string(object)
## Getting the list of the variable names
print(new_vit_data.columns.tolist())
## Using the right data type
new_vit_data.columns = new_vit_data.columns.str.strip()
# Convert both date columns to datetime
new_vit_data['Date de prélèvement'] = pd.to_datetime(new_vit_data['Date de prélèvement'], errors='coerce')
new_vit_data['DOB de l`animal'] = pd.to_datetime(new_vit_data['DOB de l`animal'], errors='coerce')

new_vit_data['Age'] = new_vit_data['Date de prélèvement'] - new_vit_data['DOB de l`animal']# Calculate age as timedelta
# Now check that Age is timedelta64
print(new_vit_data['Age'].dtype)  # should print: timedelta64[ns]
# Convert timedelta to months (approximate)
new_vit_data['Age_months'] = new_vit_data['Age'].dt.days / 30.44
#new_vit_data['Age'] = new_vit_data['Age'].dt.days / 365.25  ## Converting to years
new_vit_data['Age_months'] = round(new_vit_data['Age_months'], ndigits=1)
new_vit_data.head(2)
# </editor-fold>

#<editor-fold Data cleaning 2: Vitamine levels>
new_vit_data['Résultat_clean'] = new_vit_data['Résultat'].astype(str)
# First, remove 'µg/dl' and other units
new_vit_data['Résultat_clean'] = new_vit_data['Résultat_clean'].str.replace('µg/dl', '', regex=False)
new_vit_data['Résultat_clean'] = new_vit_data['Résultat_clean'].str.replace(',', '.', regex=False)  # In case comma decimals

# Then, handle "<" signs: you can remove the "<" or set it to a lower value
new_vit_data['Résultat_clean'] = new_vit_data['Résultat_clean'].str.replace('<', '', regex=False)

# Finally, convert to numeric (force errors='coerce' so invalid become NaN)
new_vit_data['Résultat_clean'] = pd.to_numeric(new_vit_data['Résultat_clean'], errors='coerce')

# Drop rows where clean result is NaN
new_vit_data = new_vit_data.dropna(subset=['Résultat_clean'])
# </editor-fold>

# <editor-fold Descriptive Statistics: counting number of observation>
new_vit_data.info()
##
Vit_CH = pd.crosstab(new_vit_data['Procédure (Acte professionnel)'], new_vit_data['Espèce'])
print(Vit_CH)
Vit_CH.plot(kind= 'bar', stacked=True, figsize=(8,4))

plt.title('Number of Bovine and Equine across Vitamin Level')
plt.xlabel("Vitamin")
plt.ylabel('number of animals')
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()

# Group by Vitamin type and Species, then describing their vitamin level
desc_table_v = new_vit_data.groupby(['Procédure (Acte professionnel)', 'Espèce'])['Résultat_clean'].describe()
#  Save as an Excel file
desc_table_v.to_excel('vitamin_summary_table.xlsx')

# Group by Vitamin type and Species, then describing their age distribution
desc_table_a = new_vit_data.groupby(['Procédure (Acte professionnel)', 'Espèce'])['Age_months'].describe()
#  Save as an Excel file
desc_table_a.to_excel('Age_summary_table.xlsx')
# </editor-fold>

# <editor-fold setting parameter for visualization>
vitamins = new_vit_data['Procédure (Acte professionnel)'].unique()
animals = new_vit_data['Espèce'].unique()

# Total plots needed
total_plots = len(animals) * len(vitamins)

# Create a grid of subplots
fig, axes = plt.subplots(
    nrows=(total_plots + 2) // 3,  # Automatically choose number of rows
    ncols=3,
    figsize=(18, 6 * ((total_plots + 2) // 3))
)
axes = axes.flatten()  # Flatten in case it’s a 2D array
# </editor-fold>

# <editor-fold Visual: Boxplot>

# Initialize plot counter
i = 0

# Plot each combination of animal and vitamin
for animal in animals:
    for vitamin in vitamins:
        subset = new_vit_data[
            (new_vit_data['Espèce'] == animal) &
            (new_vit_data['Procédure (Acte professionnel)'] == vitamin)
        ]

        if not subset.empty:
            sns.boxplot(
                data=subset,
                x='Résultat_clean',
                ax=axes[i]
            )
            axes[i].set_title(f'{vitamin} levels in {animal}')
            axes[i].set_xlabel('Vitamin Level')
            axes[i].set_ylabel('Count')
            i += 1

plt.tight_layout()
plt.savefig('vitamin_boxplot.jpeg')
plt.show()
# </editor-fold>

# <editor-fold Visual: Histogram>

# Initialize plot counter
i = 0

# Plot each combination of animal and vitamin
for animal in animals:
    for vitamin in vitamins:
        subset = new_vit_data[
            (new_vit_data['Espèce'] == animal) &
            (new_vit_data['Procédure (Acte professionnel)'] == vitamin)
        ]

        if not subset.empty:
            sns.histplot(
                data=subset,
                x='Résultat_clean',
                ax=axes[i]
            )
            axes[i].set_title(f'{vitamin} levels in {animal}')
            axes[i].set_xlabel('Vitamin Level')
            axes[i].set_ylabel('Count')
            i += 1

plt.tight_layout()
plt.show()

# </editor-fold>

# <editor-fold Visual: QQ_plot>

# Assuming you're looping through vitamins and using subplots:
i = 0  # Initialize subplot counter
for animal in animals:
    for vitamin in vitamins:
        subset = new_vit_data[
            (new_vit_data['Espèce'] == animal) &
            (new_vit_data['Procédure (Acte professionnel)'] == vitamin)
        ]['Résultat_clean'].dropna()  # drop missing values

        stats.probplot(subset, dist="norm", plot=axes[i])  # ✅ correct index
        axes[i].set_title(f"QQ Plot - {vitamin} ({animal})")  # optional: add animal
        i += 1  # ✅ increment plot counter

plt.tight_layout()
plt.show()

# </editor-fold>

# <editor-fold Visual: Scatter plot for vitamins levels and age>

# Initialize plot counter
i = 0

# Loop through animal types and vitamins
for animal in animals:
    for vitamin in vitamins:
        ax = axes[i]

        # Filter data for specific animal and vitamin
        subset = new_vit_data[
            (new_vit_data['Espèce'] == animal) &
            (new_vit_data['Procédure (Acte professionnel)'] == vitamin)
        ]

        # Scatter plot: age vs vitamin level
        ax.scatter(subset['Age_months'], subset['Résultat_clean'], alpha=0.7)

        # Set title and labels
        ax.set_title(f'{vitamin} - {animal}')
        ax.set_xlabel('Age (months)')
        ax.set_ylabel('Vitamin level')

        i += 1

# Adjust layout
plt.tight_layout()
plt.show()
# </editor-fold>

# <editor-fold Visual: Bar plot of vitamins levels across Race of animals>

# Initialize plot counter
i = 0
# Loop over animals and vitamins
for animal in animals:
    for vitamin in vitamins:
        ax = axes[i]

        # Filter for specific animal and vitamin
        subset = new_vit_data[
            (new_vit_data['Espèce'] == animal) &
            (new_vit_data['Procédure (Acte professionnel)'] == vitamin)
        ]

        # Group by race and calculate mean vitamin level
        bar_data = subset.groupby('Race')['Résultat_clean'].mean().sort_values()

        # Check if there is data
        if not bar_data.empty:
            # Bar plot
            bar_data.plot(kind='bar', ax=ax, color='skyblue')

            ax.set_title(f'{vitamin} - {animal}')
            ax.set_xlabel('Race')
            ax.set_ylabel('Average Vitamin Level')
            ax.tick_params(axis='x', rotation=90)  # Rotate x labels if needed
        else:
            # If no data, write a message in the subplot
            ax.text(0.5, 0.5, 'No data', ha='center', va='center')
            ax.set_title(f'{vitamin} - {animal}')
            ax.set_xticks([])
            ax.set_yticks([])

        i += 1

# Adjust layout
plt.tight_layout()
plt.show()
# </editor-fold>

# <editor-fold Visual: Heatmaps of vitamin, ville de clinic pour each animal>
for animal in animals:
    subset = new_vit_data[new_vit_data['Espèce'] == animal]
    DL = pd.crosstab(subset['Procédure (Acte professionnel)'], subset['Ville de la clinique'])

    plt.figure(figsize=(10, 6))
    sns.heatmap(DL, annot=True, cmap='Blues', fmt='d')
    plt.title(f"Number of {animal} that visited each clinic")
    plt.xlabel('Clinic Village')
    plt.ylabel("Vitamins")
    plt.tight_layout()
    plt.show()

## </editor-fold>
