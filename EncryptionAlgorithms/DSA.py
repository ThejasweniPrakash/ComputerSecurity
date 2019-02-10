
# coding: utf-8

# In[20]:


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa


# In[21]:


#signing
private_key = dsa.generate_private_key(key_size=2048,backend=default_backend())
data = b"this is some data I'd like to sign"
signature = private_key.sign(data,hashes.SHA256())
print(signature)


# In[22]:


#veryfying
public_key = private_key.public_key()
if public_key.verify(signature,data,hashes.SHA256()):
    print("Signatures verified")
else:
    print("Incorrect signature")

