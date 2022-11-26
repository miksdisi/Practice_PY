import pandas as pd

# section 1, 2 ##################################################################################################

#prevent SettingWithCopyWarning message from appearing
pd.options.mode.chained_assignment = None
wage = pd.read_csv('C://Users//sivtc//Downloads//homework1//wage-1.csv')
# print(wage)
# wage1 = pd.DataFrame(wage_file)
# print(wage1)

# section 3 #####################################################################################################

for i in range(len(wage['gender'])):
    if wage['gender'][i] == 1:
        wage['gender'][i] = 'M'
    else:
        wage['gender'][i] = 'F'
# print(wage)

# section 4 #####################################################################################################

wage_M_total = wage.groupby('gender')['wage'].sum()['M']
count_M = wage.groupby('gender')['wage'].count()['M']
average_wage_M = wage_M_total/count_M
# print('average wage for men:', average_wage_M)
wage_F_total = wage.groupby('gender')['wage'].sum()['F']
count_F = wage.groupby('gender')['wage'].count()['F']
average_wage_F = wage_F_total/count_F
# print('average wage for women:', average_wage_F)

# section 5 #####################################################################################################

wage_counts = wage.value_counts() # checking for repetitive values
# print(wage_counts)

wage_dif = wage.nunique() # checking for different values
# print(wage_dif)

wage = wage.drop_duplicates(subset=['person_id'], ignore_index=True)
# print(wage)

# section 6 #####################################################################################################

# for i in range(len(wage)):
#     if wage['wage'][i] < 0:
#         wage['wage'][i] = None
# print(wage[17:34])
# desc_wage = wage.describe()
# print(desc_wage.replace({'wage': {995: 'does not make sence'}, 'person_id': {0 : 'does not make sence'}}))
wage = wage.loc[wage['wage'] > 0]
wage = wage.sort_values('person_id', ignore_index=True)
# print(wage.describe())          # this string prints describe
# print(wage[17:34])
print(wage)
# print(len(wage))

# section 7 #####################################################################################################

bonus = pd.read_csv('C://Users//sivtc//Downloads//homework1//bonus-1.csv', sep=';')
# bonus = bonus.fillna(0)
# print(bonus)

# section 8 #####################################################################################################

b_w = wage.merge(bonus, how='outer', on='person_id')
b_w = b_w.fillna(0)
# print(b_w)
# total = b_w['wage']*12 + b_w['bonus']
wage['total'] = b_w['wage']*12 + b_w['bonus']
print(wage)

# section 9 #####################################################################################################

wage.to_csv('C://Users//sivtc//Downloads//homework1//df_result//df_result.csv', sep=';', index=False)