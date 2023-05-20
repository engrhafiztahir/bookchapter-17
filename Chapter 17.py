#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Create a new list
cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]
#length = len(cities) # This is a integer value, we cannot cocatenate it. 
#length = str(length) # Convert the interget data into string
#print("The length of the list is " + length)
Cities = str(cities[0:3])
print("The slice of the list is " +Cities)


# In[14]:


# Careate a new list
numbers = [1,2,3,4,5,6,7,8] # This is interget list
length = len(numbers) 
numbers = str(numbers)
print("The list is " +numbers)
print(type(numbers))


# In[32]:


numbers = [1,2,3,4,5,6,7,8]
lengh = len(numbers)
print(length)
sliced_list = numbers[1:]
print(sliced_list)


# In[48]:


# Create a new string list
Countries = ["Canada", "U.S.A", "U.K" ,"India" ,"Pakistan" ,"Japan" ,"China"]
length = len(Countries)
print(length)
Countries.remove("Canada")
Countries.remove("U.S.A")
print(Countries)


# In[61]:


#Poping the list
countries = ["Canada", "U.S.A", "U.K" ,"India" ,"Pakistan" ,"Japan" ,"China"]
American_countries = []
american_countries = countries.pop(0)
American_countries.append(american_countries)
print(countries)
print(American_countries)


# In[ ]:





# In[ ]:




