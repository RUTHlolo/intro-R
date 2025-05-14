# 1) Syntaxe

"Bonjour tout le monde!"

5
10
25

5 + 10


print("Bonjour tout le monde!")

for (i in 1:10) {
  print(i)
}


# 2) Commentaires

# Ceci est un commentaire

h + 1 # Le nombre optimal de cafés

# j'ai "Error: object 'h' not found"

# Je dois donc définir h

h <- 2
h = 2
2 -> h

h + 1 # voilà!

y <- h + 1


# 3) Variables
h

v <- "nombre de cafés bus"
print(v)

class(y)
class(v)

# 3.1) Concaténer des éléments
class(paste(y , v))
paste0(y , v)

paste0(y ,"_", v)

# 4) Type de données
# numeric - (11.5, 5, 77)
# integer - (1L, 55L, 100L) - where "L" indicates it's an int
# complex - 9 + 3i, where "i" is anything a constant, a function, etc. 
# character or string - ("anything between cotes")
# logical or boolean - (T or F)

age <- 27
class(age)

name <- "Solène" 
str(name)
class(name)

x <- 9 + 3i
str(x)
class(x)

a <- F
str(a)  # Contraire : T (TRUE)
class(a)

# There are three "number" types of data in R:
# numeric --> the most common type 
# integer
# complex

x <- 10.5   # numeric
y <- 10L    # integer
z <- 1i     # complex 

# 4.1) Convertir les types de données

new_y <- as.numeric(y)
class(new_y)

new_y_back <- as.integer((new_y))
class(new_y_back)

age2 <- "40"

age + age2
age2 <- as.numeric(age2)
age + age2

is.character(age2)


# Supprimer un élément de l'environnement
rm(age2)


# 4.2) Les données manquantes
temperature <- c(18, 21, 30, NA)

temperature

# Identifier la données manquantes
is.na(temperature)

# Remplacer les données manquantes manuellement
temperature[4] <- 25



# 5) Quelques opérations : if else, boucles for while, functions
# 5.1) Arithmetic Operators
# + 	Addition 	x + y 	
# - 	Subtraction 	x - y 	
# * 	Multiplication 	x * y 	
# / 	Division 	x / y 	
# ^ 	Exponent 	x ^ y

10 + 5
10^2


# 5.2) Opérateurs de comparaison
# == 	Equal 	x == y 	
# != 	Not equal 	x != y 	
# > 	Greater than 	x > y 	
# < 	Less than 	x < y 	
# >= 	Greater than or equal to 	x >= y 	
# <= 	Less than or equal to 	x <= y


# Création d'un dataframe
classe <- data.frame(names = c("G","La","B","Lu", "K","P"))
str(classe)

# Ajout d'une variable
classe$students <- ifelse(classe$names != "P", "yes", "no")

# Création d'un vecteur
classe2 <- c("G","La","B","Lu", "K","P")

5 < 6
5 < 5



# 5.3) Opérateurs divers
# : 	Creates a sequence 	x <- 1:10
# %in% 	If an element belongs to a vector 	x %in% y
# %*% 	Matrix multiplication 	x <- M1 %*% M2

x <- 1:10
M1 <- matrix(1:9, nrow = 3, ncol = 3)
M2 <- matrix(12:20, nrow = 3, ncol = 3)
x <- M1 %*% M2

impair = seq(1, 10, 2)
impair

rep(1, 10)

length(impair)


# Repérer un motif dans une chaîne de caractères

nom <- "Ce cours est vraiment cool"

grep("cool", nom)
nom <-gsub("cool", "super cool!", nom)


# 5.4)  If Else
# We use : 
# == 	Equal 	x == y 	
# != 	Not equal 	x != y 	
# > 	Greater than 	x > y 	
# < 	Less than 	x < y 	
# >= 	Greater than or equal to 	x >= y 	
# <= 	Less than or equal to 	x <= y

# 5.4.1) IF statement:
solene <- 27
pablo <- 43

if (pablo < solene) {
  print("pablo is older than solene")
} # R uses { } to define the scope in the code

# 5.4.2) ELSE IF statement:
if (solene > pablo) {
  print("solene is older than pablo")
} else if (pablo > solene) {
  print ("pablo is older than solene")
} 

if (solene > pablo) {
  print("solene is older than pablo")
} 

# 5.4.3) IF ELSE statement:
if (solene > pablo) {
  print("solene is older than pablo")
} else if (solene == pablo) {
  print("solene and pablo have the same age")
} else {
  print("pablo is older than solene")
} 

# 5.5)  For loops:
for (i in 1:5) {
  print(i)
} 

for (i in 1:pablo) {
  if (i < 18) {
    print(paste(i,"baby"))}
  else {
    print(paste(i,"adult"))
  }
} 


# Création d'une liste
val <- list("salut", "bonjour", "bon matin", 28, 61)
str(val)


for (i in val) {
  print(i)
} 


# 5.5) Functions
fn1 <- function(z, w) {
  result <- z^2 + w
  
  print(result)
}

fn1(1,2)


# 6) Structures de données 
# 6.1) Vecteurs
years <- c(2024, 2025)
full_name <- c("Solene","Le Manach")

# 6.2) Listes
# A list can have different data types inside it
full_name_list <- list("Solene","Le Manach")
full_name_list[1]
full_name_list[2]

# Check if "Solene" is present in full_name_list:
"Solene" %in% full_name_list
"Pablo" %in% full_name_list 

# Remove list items
last_name_list <- full_name_list[-1]
last_name_list[1]

# 6.3) Matrice
M1 <- matrix(1:9, nrow = 3, ncol = 3)
M2 <- matrix(12:20, nrow = 3, ncol = 3)


# 6.4) Tableaux
ages <- c(1:28)

# 1st and 2nd number in the bracket indicates no. of rows and columns.
# Last number in the bracket indicates the number of dimensions.
multiages <- array(ages, dim = c(4, 3, 2)) 

# Access to an array
multiages[2, 1, 1] # array[row, column, dimension]

# 6.5) Cadre de données (Data frame)
xxx <- data.frame(multiages)

# Dimensions des données
dim(xxx)
nrow(xxx)
ncol(xxx)

# Se situer dans un dataframe
xxx[1, 2]

xxx[1, "X2"]





############ Créer un projet
# 7) Structurer son projet d'analyse
# 7.1) Créer un projet

## File > New Project > New Directory > New Project

# 7.3) Créer un Rmarkdown ou Quarto
## File > New File > Rmarkdown ou Quarto

# 7.4) Environnement courant
getwd()

setwd("C:/Users/oz21367/OneDrive - Universite de Montreal/Documents/Cours - Santé animale et science des données/Lab 1 - R & Python")

# 7.5) Importer des données
# Importer un fichier CSV

# Faire les premières analyse :
# - Dimensions des données (table, length, dim)
# - Vérifier le type des données
# - Summary
# - Visualiser les données
# - Compter les valeurs manquantes
# - Graph si on a le tps


data <- read.csv("train_.csv")

library(openxlsx)
data <- read.xlsx("aliment.xlsx")

data[is.na(data$site), "site"] <- 1
