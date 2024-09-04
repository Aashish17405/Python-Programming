import numpy as np
import pandas as pd
# a={'California':100000,'America':45761,'India':1468956}
# b={'California':100,'America':None,'India':146}
# p=pd.DataFrame({'population':a,'area':b})
# p['density']=round(p['population']/p['area'],2)
# print(p.dropna())
# print(p.fillna(method='bfill'))
# print(p.fillna(method='ffill'))
# print(p.fillna(method='bfill',axis=0))



# p.iloc[0]=10
# print(p)
# rng=np.random.RandomState(42)
# a=pd.DataFrame(rng.randint(0,10,(3,4)),columns=['A','B','C','D'])
# print(a.loc[1])
# s=pd.Series([1,2,4,5],columns=['A','B','C','D'])
# print(a.loc[1]+s)


index=[('California',2000),('California',2010),('New York',2000),('New York',2010),('Texas',2000),('Texas',2010)]
populations=[33871648,37253956,18976457,19378102,20851820,25145561]
index=pd.MultiIndex.from_tuples(index)
pop = pd.Series (populations, index=index)
pop=pop.reindex(index)
# print(pop[:,2010])
# popp=pop.unstack()
# print(popp)
# print(popp.stack())
pop_df=pd.DataFrame({'total':pop,'under18':[1564848,546465465,7899321,1654775,16546,97874]})
print(pop_df)
f=pop_df['under18']/pop_df['total']
print(f)