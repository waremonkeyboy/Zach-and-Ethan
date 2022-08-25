import pandas as pd
import numpy as np

print('Measurements are all in lbs')
print('Percentages are 95, 90, 85, 80, 75, 70, 65')
Name = input('What is your name:')
Bench = input('What is your Bench:')
Squat = input('What is your Squat:')
Deadlift = input('What is your Deadlift:')
Overhead_Press = input('What is your Overhead press:')

Bench_Calculator = [.95, .90, .85, .80, .75, .70, .65]
Bench_Percentages = []
for number in Bench_Calculator:
    percentage = float(Bench) * number
    Bench_Percentages.append(percentage)
A = Bench_Percentages[0]
B = Bench_Percentages[1]
C = Bench_Percentages[2]
D = Bench_Percentages[3]
E = Bench_Percentages[4]
F = Bench_Percentages[5]
G = Bench_Percentages[6]

Squat_Calculator = [.95, .90, .85, .80, .75, .70, .65]
Squat_Percentages = []
for number in Squat_Calculator:
    percentage = float(Squat) * number
    Squat_Percentages.append(percentage)
H = Squat_Percentages[0]
I = Squat_Percentages[1]
J = Squat_Percentages[2]
K = Squat_Percentages[3]
L = Squat_Percentages[4]
M = Squat_Percentages[5]
N = Squat_Percentages[6]

Deadlift_Calculator = [.95, .90, .85, .80, .75, .70, .65]
Deadlift_Percentages = []
for number in Deadlift_Calculator:
    percentage = float(Deadlift) * number
    Deadlift_Percentages.append(percentage)
O = Deadlift_Percentages[0]
P = Deadlift_Percentages[1]
Q = Deadlift_Percentages[2]
R = Deadlift_Percentages[3]
S = Deadlift_Percentages[4]
T = Deadlift_Percentages[5]
U = Deadlift_Percentages[6]

Overhead_Press_Calculator = [.95, .90, .85, .80, .75, .70, .65]
Overhead_Press_Percentages = []
for number in Overhead_Press_Calculator:
    percentage = float(Overhead_Press) * number
    Overhead_Press_Percentages.append(percentage)
V = Overhead_Press_Percentages[0]
W = Overhead_Press_Percentages[1]
X = Overhead_Press_Percentages[2]
Y = Overhead_Press_Percentages[3]
Z = Overhead_Press_Percentages[4]
AA = Overhead_Press_Percentages[5]
AB = Overhead_Press_Percentages[6]
calculation_metrics = input('Would you like to calculate your percentages based off of 95% of 1RM yes or no:')
if calculation_metrics == 'yes' :
    Overhead_Press = (float(Overhead_Press) * float(.95))
    Bench = (float(Bench) * float(.95))
    Squat = (float(Squat) * float(.95))
    Deadlift = (float(Deadlift) * float(.95))
elif calculation_metrics == 'no' :
    Overhead_Press = Overhead_Press
    Bench = Bench
    Squat = Squat
    Deadlift = Deadlift
print(Name, 'Here are your percentages:')
print('your Bench percentages are:', '95%:',A, '90%:',B, '85%:',C, '80%:',D, '75%:',E, '70%:',F, '65%:',G)
print('your Squat percentages are:', '95%:',H, '90%:',I, '85%:',J, '80%:',K, '75%:',L, '70%:',M, '65%:',N)
print('your Deadlift percentages are:', '95%:',O, '90%:',P, '85%:',Q, '80%:',R, '75%:',S, '70%:',T, '65%:',U)
print('your Overhead percentages are:', '95%:',V, '90%:',W, '85%:',X, '80%:',Y, '75%:',Z, '70%:',AA, '65%:',AB)
AC = ('95%:',A, '90%:',B, '85%:',C, '80%:',D, '75%:',E, '70%:',F, '65%:',G)
AD = ('95%:',H, '90%:',I, '85%:',J, '80%:',K, '75%:',L, '70%:',M, '65%:',N)
AE = ('95%:',O, '90%:',P, '85%:',Q, '80%:',R, '75%:',S, '70%:',T, '65%:',U)
AF = ('95%:',V, '90%:',W, '85%:',X, '80%:',Y, '75%:',Z, '70%:',AA, '65%:',AB)

nestdict = {'95%': { Overhead_Press: A, Bench: H, Squat: O, Deadlift: V },
'90%': { Overhead_Press: B, Bench: I, Squat: P, Deadlift: W },
'85%': { Overhead_Press: C, Bench: J, Squat: Q, Deadlift: X },
'80%': { Overhead_Press: D, Bench: K, Squat: R, Deadlift: Y },
'75%': { Overhead_Press: E, Bench: L, Squat: S, Deadlift: Z },
'70%': { Overhead_Press: F, Bench: M, Squat: T, Deadlift: AA },
'65%': { Overhead_Press: G, Bench: N, Squat: U, Deadlift: AB }}
lifting_table = pd.DataFrame(nestdict)
print(lifting_table)
