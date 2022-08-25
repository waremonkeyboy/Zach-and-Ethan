import pandas as pd
import numpy as np
A	=	1
B	=	2
C	=	3
D	=	4
E	=	5
F	=	6
G	=	7
H	=	8
I	=	9
J	=	10
K	=	11
L	=	12
M	=	13
N	=	14
O	=	15
P	=	16
Q	=	17
R	=	18
S	=	19
T	=	20
U	=	21
V	=	22
W	=	23
X	=	24
Y	=	25
Z	=	26
AA	=	27
AB	=	28
nestdict = {
'95%': { OverheadPress: A, Bench: H, Squat: O, Deadlift: V },
'90%': { OverheadPress: B, Bench: I, Squat: P, Deadlift: W },
'85%': { OverheadPress: C, Bench: J, Squat: Q, Deadlift: X },
'80%': { OverheadPress: D, Bench: K, Squat: R, Deadlift: Y },
'75%': { OverheadPress: E, Bench: L, Squat: S, Deadlift: Z },
'70%': { OverheadPress: F, Bench: M, Squat: T, Deadlift: AA },
'65%': { OverheadPress: G, Bench: N, Squat: U, Deadlift: AB }}
lifting_table = pd.DataFrame(nestdict)
print(lifting_table)
