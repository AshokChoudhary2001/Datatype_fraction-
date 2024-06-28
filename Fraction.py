#!/usr/bin/env python
# coding: utf-8

# In[35]:


class fraction : 
    
    """
    A class to represent a fraction and perform arithmetic and comparison operations.

    Attributes:
    ----------
    numerator : int
        The numerator of the fraction.
    denominator : int
        The denominator of the fraction.

    Methods:
    -------
    __add__(other):
        Adds two fractions.
    __sub__(other):
        Subtracts one fraction from another.
    __mul__(other):
        Multiplies two fractions.
    __truediv__(other):
        Divides one fraction by another.
    __eq__(other):
        Checks if two fractions are equal.
    __lt__(other):
        Checks if one fraction is less than another.
    __le__(other):
        Checks if one fraction is less than or equal to another.

    
    Created by : Ashok Choudhary 
    """
    
    def __init__(self , n , d ):
        self.num = n 
        self.den = d 
        
    def __str__(self):
        return "{}/{}".format(self.num , self.den)
        
    def __add__(self ,other): 
        temp_num = self.num * other.den + self.den *other.num  
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num , temp_den)
        
    def __sub__(self ,other):
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num ,temp_den)
    
    def __mul__(self,other):
        
        temp_num = self.num *other.num
        temp_den = self.den *other.den 
        return "{}/{}".format(temp_num ,temp_den)
    
    def __truediv__(self,other):
        
        temp_num = self.num * other.den 
        temp_den = self.den * other.num 
        
        return "{}/{}".format(temp_num,temp_den)
    
    def __eq__ (self ,other):
        
        if self.num == other.num and self.den == other.den:
            return True
        else :
            return False 
        
    def __lt__ (self , other):
        
        decimal1 = self.num /self.den
        decimal2 = other.num /other.den 
        if decimal1 < decimal2 :
            return True 
        else:
            return False
        
    def __le__(self ,other):
        
        decimal1 = self.num /self.den 
        decimal2 = other.num / other.den
        
        if decimal1 <= decimal2 :
            return True 
        else:
            return False 
        
    def __ge__(self ,other ):
        
        decimal1 = self.num/self.den 
        decimal2 = other.num / other.den 
        
        if decimal1 >= decimal2 :
            return True 
        else :
            return False 
    
    def __ne__(self ,other ):
        
        dec1 = self.num / self.den 
        dec2 = other.num / other.den
        
        if dec1 != dec2:
            return True
        else : 
            return False 
            


# In[29]:





# In[34]:





# In[32]:





# In[ ]:




