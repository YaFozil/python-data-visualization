#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
   
Data = {'Year': [2020,2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070],
        'n_phone': [114.5, 128.2, 138, 145, 148.9, 151.3, 152.8, 153.3 , 153.4, 153.3, 153.2  ]
       }
  
df = pd.DataFrame(Data,columns=['Year','n_phone'])
  
plt.plot(df['Year'], df['n_phone'], color='red', marker='o')
plt.title('Mobile phones per 100 people', fontsize=18,color='green')
plt.xlabel('Years 2020-2070', fontsize=14,color='blue')
plt.ylabel('Quantity of phones', fontsize=14,color='blue')
plt.legend(['Growth of usage'])
plt.grid(True)
plt.show()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
   
Data = {'Year': [2020,2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070],
        'n_phone': [1, 1.04, 1.05, 1.07, 1.13, 1.17, 1.19, 1.21 , 1.22, 1.23, 1.25  ]
       }
  
df = pd.DataFrame(Data,columns=['Year','n_phone'])
  
plt.plot(df['Year'], df['n_phone'], color='blue', marker='o')
plt.title('Electricity generation capacity per person', fontsize=18,color='green')
plt.xlabel('Years 2020-2070', fontsize=14,color='blue')
plt.ylabel('Kilowatt of electricity', fontsize=14,color='blue')
plt.legend(['Growth of usage'])
plt.grid(True)
plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
   
Data = {'Year': [2020,2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070],
        'n_kilowatt': [87.6, 88.6, 89.5, 91.4, 91.5, 92.7, 94.4, 95.2 , 96.2, 97.2, 97.8  ]
       }
  
df = pd.DataFrame(Data,columns=['Year','n_kilowatt'])
  
plt.plot(df['Year'], df['n_kilowatt'], color='red', marker='o')
plt.title('Population with access to electricity', fontsize=18,color='green')
plt.xlabel('Years 2020-2070', fontsize=14,color='blue')
plt.ylabel('percent of population', fontsize=14,color='blue')
plt.legend(['Index of access'])
plt.grid(True)
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import pandas as pd
   
Data = {'Year': [2020,2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070],
        'km': [5177.76, 5104.4, 5099.12,5121.88,5171.08,5238.63,5326.12,5430.82,5557.75,5713.8,5895.2]
       }
df = pd.DataFrame(Data,columns=['Year','km'])

New_Colors = ['green','blue','purple','brown','teal','yellow','red','black','orange']
plt.bar(df['Year'], df['km'], color=New_Colors)
plt.title('Total roads per person', fontsize=20,color='grey')
plt.xlabel('Years 2020-2070', fontsize=16,color='blue')
plt.ylabel('Kilometrs per million people', fontsize=16,color='blue')
plt.grid(False)
plt.show()


# In[5]:


import matplotlib.pyplot as plt
   
Country = ['2020','2030','2040','2050','2060','2070']
GDP_Per_Capita = [71, 84, 88, 92, 94, 96]

plt.bar(Country, GDP_Per_Capita)
plt.title('Sanitation, % with improved access (Percent)')
plt.xlabel('Years  2020-2070')
plt.ylabel(' % of population')
plt.show()


# In[7]:


import matplotlib.pyplot as plt


labels = '2020', '2040', '2030', '2050','2060','2070'
sizes = [8500, 191000, 71000, 361000, 571000,812000]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
ax1.legend(loc='lower right', title='Years')
plt.title('ICT Cyber Net Benefit, cumulative across time', fontsize=16,color='blue')
plt.show()


# In[3]:


import matplotlib.pyplot as plt


labels = '2020', '2030', '2040', '2050','2060','2070'
sizes = [18.7, 30.9, 39.5, 45.2,48.6, 49.9]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
ax1.legend(loc='lower right', title='Years')
plt.title('Population with access to Fixed Broadband Technology', fontsize=16,color='green')
plt.show()


# In[ ]:




