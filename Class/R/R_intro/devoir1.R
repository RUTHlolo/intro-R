## Syntax & Comments
for (i in 1:5){
  print(paste('counting', i))
}
h <- 6
h + 1

## Variables & Concatenation
x <- 10
y <- 5
z <- x+y
paste(z, 'for Ifeoluwa R O')

## Data Types
age <- as.integer(45) ## integer
class(age)
height <- 5.6 ## numeric
class(height)
se <- 5i
class(se)
q <- as.numeric(20)
height + q

##Missing data
temp <- c(25, NA, 22, NA, 27)
is.na(temp)
temp[c(2,4)] = round(mean(temp, na.rm=T),1)
temp

### Conditions and loops
age1 = 27
age2 = 45
if (age1>age2){
  print('I am older than you')
}else if(age1 == age2){
  print("we are of the same age")
}else{
  print('You are older')
}

for (i in 1:30){
  if (i<18){
    print('Baby')
  }else{
    print('Adult')
  }
}

num = function(p,q){
  r = (p*q)+5
  print(r)
  return(r)
}
num(6.9,9)

## Data Structures
## Creating vector
vec <- c('Pierre', 'Paul','Marie')
vec
class(vec)
vec2 <- c(1990,1995)
## creating a list
list1 <- list(vec,vec2)
list1
### creating matrix
mat = matrix(1:9, nrow = 3, ncol = 3)
mat
array_3 <- array(c(1:21), dim = c(7,3,3))
array_3
age = c(43,22,36)
df = data.frame(vec, age)
df