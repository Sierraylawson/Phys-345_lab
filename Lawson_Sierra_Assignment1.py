#!/usr/bin/env python
# coding: utf-8

# # Assignment 1: Initialization & Practice
# 
# **Course:** PHYS 345 - Computational Physics
# 
# **Due Date:** 1/21/2026
# 
# ---

# ## 1. Objective
# 
# The goal of this "zeroth" assignment is to ensure your computational workbench is fully functional and give you exampl. You will verify your Python installation, familiarize yourself with the Jupyter interface, and perform a basic physical calculation using variables and the `math` library.

# ## 2. Python Fundamentals: Data Types
# 
# Before we dive into physics, we must understand how Python stores information. Every variable has a **type**. The most common types you will use are:
# 
# * **int**: Integers (e.g., `5`, `-10`, `10**23`)
# * **float**: Floating-point numbers/Decimals (e.g., `3.14`, `1.0`, `6.626e-34`)
# * **str**: Strings/Text (e.g., `"Electron"`, `"Force"`)
# * **bool**: Boolean/Logic (`True` or `False`)
# 
# **Task:** Run the cell below to see how Python identifies these types.

# In[1]:


a = 10
b = 10.0
c = "Computational Physics"
d = (5 > 2)

print(f"a is {type(a)}")
print(f"b is {type(b)}")
print(f"c is {type(c)}")
print(f"d is {type(d)}")


# ## 3. The Floating-Point Reality
# 
# In physics, we deal with extreme scales. However, computers represent decimal numbers (floats) using binary. This leads to **precision errors**. 
# 
# **Task:** Run the cell below. You might expect the result to be exactly `True`. Is it?

# In[2]:


result = (0.1 + 0.2)
print(f"Value of 0.1 + 0.2: {result}")
print(f"Is it equal to 0.3? {result == 0.3}")

print("\nTIP: In physics simulations, never use '==' to compare two floats. ")
print("Instead, check if they are 'close enough' using: math.isclose(a, b)")


# ## 4. Environment Verification
# 
# In the cell below, we will check if your environment has the core libraries installed.
# 
# **Task:** Run the following cell. If you see version numbers for NumPy and Matplotlib, your installation is successful.

# In[3]:


import sys
import numpy as np
import matplotlib
import math

print(f"Python version: {sys.version}")
print(f"NumPy version: {np.version.version}")
print(f"Matplotlib version: {matplotlib.__version__}")
print("\nSuccess! Your environment is ready.")


# ## 5. Problem 1: Escape Velocity
# 
# The escape velocity ($v_e$) is the minimum speed needed for a free, non-propelled object to escape from the gravitational influence of a massive body. The formula is:
# 
# $$ v_e = \sqrt{\frac{2GM}{R}} $$
# 
# Where:
# 
# * $G$ is the gravitational constant ($6.674 \times 10^{-11} \, \text{m}^3\text{kg}^{-1}\text{s}^{-2}$)
# * $M$ is the mass of the planet (For Earth: $5.972 \times 10^{24} \, \text{kg}$)
# * $R$ is the radius of the planet (For Earth: $6.371 \times 10^6 \, \text{m}$)
# 
# (Note that you can view the LaTeX and markdown code for this equation by double-clicking on the cell, or any of the other text cells.)

# ## 6. Implementation
# 
# **Task:** Complete the Python code below to calculate the escape velocity for Earth, to 2 decimal places.

# In[4]:


# 1. Define your constants
from math import sqrt
G = 6.67430e-11    # m^3 / (kg * s^2)
M = 5.972e24 
R = 6.371e6


# 2. Perform the calculation
# There are two ways of implementing the square root. 
v_e = sqrt((2*G*M)/R)

# 3. Print the result with units
print(f"The escape velocity of Earth is approximately {v_e}    m/s.")


# ## 7. Problem 2: Pendulum
# Calculate the period of a pendulum with Length = 2.5 m, to 4 decimal places. 
# $$T = 2 \pi \sqrt{L/g}$$

# In[5]:


#Make sure to comment your code. 
L = 2.5
g = 9.8
pi = 3.14
T = 2*pi*(sqrt(L/g))

print(f"Pendulum Period: {T}   seconds")


# ## 8. Problem 3: Packages and trigonometry
# Calculate the horizontal distance a projectile will travel, its range R, with an initial velocity of 20 m/s and angle of 45 degrees.  
# 1. You can derive the equation or look it up, but make sure you either show your work, or cite a source. This is good practice for writing lab reports.
# 2. Note that you will need to convert to radians to do the calculation. 

# In[6]:


#sin(2theta)-> sin(90)-> 1
v = 20
O = 45
g = 9.8

R = ((v**2)/g)

print (f"The projectile will travel {R} meters")


# ## 9. Submission Checklist
# 
# Before you push this to GitHub, ensure you have:
# 
# 1. Changed the "Kernel" to your Anaconda environment.
# 2. Selected **Kernel > Restart & Run All** to ensure the code executes sequentially without errors.
# 3. Saved the notebook with the naming convention: `LastName_FirstName_Assignment1.ipynb`.
# 4. Committed and pushed to your course repository.
# 
# --- 
# *End of Assignment 1*
