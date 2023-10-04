import pingouin as pg

# Données d'exemple
X = [13, 130, 39, 33, 10,13, 68, 18, 3, 11,38, 23, 60, 5, 9,59, 5, 86, 22, 70,58, 3, 167, 15, 30, 
     8, 20, 67, 26, 19]
Y = [14, 8, 20, 3, 138,122, 78, 69, 111, 3,128, 31, 18, 35, 111,109, 36, 27, 32, 35,12, 27, 8, 3,
     80,91, 68, 66, 176, 15]
# Test t de Student
t_stat= pg.ttest(X, Y)
print("Statistique de test t :", t_stat)

