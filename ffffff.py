#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.datasets import load_iris
iris_dataset=load_iris()
print("Keys of iris_dataset:\n",iris_dataset.keys())


# In[ ]:


print("Keys of iris_dataset:\n",iris_dataset.keys())


# In[ ]:


print(iris_dataset['DESCR'][:193]+"\n...")


# In[ ]:


print("Tarhet names:",iris_dataset['target_names'])


# In[ ]:


print("Target names:",iris_dataset['target_names'])


# In[ ]:


print("Feature names:\n",iris_dataset['feature_names'])


# In[ ]:


print("Type of data:",type(iris_dataset['data']))


# In[ ]:


print("Shape of data:",iris_dataset['data'.shape])


# In[ ]:


print("First five rows of data:\n",iris_dataset['data'][:5])


# In[ ]:


print("Type of target:",type(iris_dataset['target']))


# In[ ]:


print("Shape of target:",iris_dataset['target'.shape])


# In[ ]:


print("Target:\n",iris_dataset['target'])

