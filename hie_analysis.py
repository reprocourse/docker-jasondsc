import pandas as pd
from statsmodels.formula.api import OLS
from statsmodels.formula.api import logit
from statsmodels.formula.api import MNLogit

hie = pd.read_csv('1-longitudinal-minimal-data-set-V2.csv', na_values='nd')
print(hie.columns.values)

## Loop through all 6 timepoints and compute model
for i in range(1,7):
    formula= "outcome ~ 1 + " + " + " .join([hie.columns.values[2+i] , hie.columns.values[8+i]])
    print(formula)
    model1 = MNLogit.from_formula(formula,hie, missing='drop').fit()
    print(model1.summary())

## try computing an average model for the values above
hie['avg_NSE']= hie[hie.columns.values[range(3,9)]].mean(axis=1)
hie['avg_copeptin']=hie[hie.columns.values[range(9,15)]].mean(axis=1)
model1 = MNLogit.from_formula("outcome ~ avg_NSE + avg_copeptin +1",hie, missing='drop').fit()
print(model1.summary())

## compute same models but control for gestational period and birth type
for i in range(1,7):
    formula= "outcome ~ 1 + gestational_age + delivery_mode +" + " + " .join([hie.columns.values[2+i] , hie.columns.values[8+i]])
    print(formula)
    model1 = MNLogit.from_formula(formula,hie, missing='drop').fit()
    print(model1.summary())

## compute same models but for Apgar 5 min variable
for i in range(1,7):
    formula= "Apgar_5min ~ 1 + " + " + " .join([hie.columns.values[2+i] , hie.columns.values[8+i]])
    print(formula)
    model1 = OLS.from_formula(formula,hie, missing='drop').fit()
    print(model1.summary())

## compute same models but for  Apgar 10 min variable
for i in range(1,7):
    formula= "Apgar_10min ~ 1 + " + " + " .join([hie.columns.values[2+i] , hie.columns.values[8+i]])
    print(formula)
    model1 = OLS.from_formula(formula,hie, missing='drop').fit()
    print(model1.summary())
