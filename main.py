import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

# Data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
print(df.columns.to_list())
df = df.drop_duplicates()

#Numerical Columns Cleaning
df['price'] = df['price'].astype(str).str.replace(",","").astype(float)
df['area'] = df['area'].astype(str).str.replace(",","").astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(",","").astype(int)

# Categorical Column Cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera':True,'not approved by rera':False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()

df= df.drop_duplicates()
print(df)



# Question1: Which is the costliest Flat in the dataset ?
costliest_flat  = df.loc[df['price'].idxmax()]
#print(costliest_flat)
print(f"The costliest flat is a {costliest_flat['bhk_count']} BHK {costliest_flat['flat_type']} located in {costliest_flat['locality']}, built by {costliest_flat['builder_name']}. It is priced at {costliest_flat['price']/10000000} cr and has an area of {costliest_flat['area']} sqft with a rate of {costliest_flat['rate_per_sqft']} per sqft. The flat is currently {costliest_flat['status']} and RERA approval status is {costliest_flat['rera_approval']}.")

# Question2: Which Locality has the highest average price?
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality}.")

#question3: which loatity has the highest rate per square foot?
highest_avg_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest average rate per square foot is {highest_avg_rate_locality}.")

# question4 : Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print(f"Ready-to-move properties cost more on average ({ready_to_move_avg_price}) than under-construction properties ({under_construction_avg_price}).")

else:
    print(f"Under-construction properties cost more on average ({under_construction_avg_price}) than ready-to-move properties ({ready_to_move_avg_price}).")

#question5: Do RERA approved properties command a price premium ?

rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
Not_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > Not_rera_approved_avg_price:
    print(f"RERA approved properties command a price premium on average ({rera_approved_avg_price}) compared to non-RERA approved properties ({Not_rera_approved_avg_price}).")

else:
    print(f"Non-RERA approved properties command a price premium on average ({Not_rera_approved_avg_price}) compared to RERA approved properties ({rera_approved_avg_price}).")    

#question6: How does area (sqft) impact property prices? 
sns.scatterplot(data=df, x='area', y='price')
plt.show()

#question7: Which bhk configuration is the most expensive ?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration on average is {most_expensive_bhk} BHK.")

#question8: which property type is costliest ?
costliest_property_type = df.groupby('flat_type')['price'].mean().idxmax()
print(f"The costliest property type on average is {costliest_property_type}.")

#question 9: Do certain builders price higher per sqft ?
higher_price_company  = df.groupby('company_name')['rate_per_sqft'].mean().idxmax()
print(f"The builder that charges the highest rate per square foot on average is {higher_price_company}.")

#question 10: are larger homes more expensive per sqft ?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.show()
