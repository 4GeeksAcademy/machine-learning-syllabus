# -*- coding: utf-8 -*-
"""matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fx7BgZHOlie01rxVcByK6div5a6Gux_x
"""

import matplotlib.pyplot as plt

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline # For showing plots with in Jupyter cells

plt.show() # For showing the plots with in a Python script

"""# Approach for creating plots

## Functional approach
"""

import numpy as np

x = np.linspace(0, 10, 20) # Generate 20 data points between 0 and 10
y = x **2  # Generate array 'y' from square of 'x'


plt.plot(x,y)
plt.show()

"""#### Now that we have a plot, let’s go on to name the x-axis, y-axis, and add a title using .xlabel(), .ylabel() and .title()"""

plt.plot(x,y)
plt.title("First plot")
plt.xlabel('X Label')
plt.ylabel(' Y Label')
plt.show()

"""# Using subplot() method"""

# plt.subplot(nrows, ncols, plot_number)

plt.subplot(2,2,1)
plt.plot(x,x, 'red')

plt.subplot(2,2,2)
plt.plot(x,y, 'black')

plt.subplot(2,2,3)
plt.plot(y,x, 'green')

plt.subplot(2,2,4)
plt.plot(y,y, 'orange')
plt.show()

"""# Object oriented Interface"""

# Let’s create a blank Figure using the .figure() method.

fig = plt.figure()
ax = fig.add_axes([0.1, 0.2, 0.8, 0.9])
plt.show()

# let’s plot our x and y arrays on it:
fig = plt.figure()
ax = fig.add_axes([0.1, 0.2, 0.8, 0.9])
ax.plot(x,y, 'purple')
plt.show()

# Using .set_xlabel(), .set_ylabel() and .set_title()

fig = plt.figure()
ax = fig.add_axes([0.1, 0.2, 0.8, 0.9])

ax.plot(x,y, 'purple')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title("First plot using Object Oriented Approach")
plt.show()

"""### Multiple Figures"""

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

#Now lets plot our x and y arrays on the axes that we have created

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x,y)
axes2.plot(y,x)
plt.show()

"""# Exercise 1

### Quick Exercise: Now that we have our plot ready, see if you can set the title, the x and y labels for both axes.
"""

#Exercise 1 Solution:
fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.set_xlabel('X Label Axes 1')
axes1.set_ylabel('Y Label Axes 1')
axes1.set_title("First Axes Title")

axes2.set_xlabel('X Label Axes 2')
axes2.set_ylabel('Y Label Axes 2')
axes2.set_title("Second Axes Title")

axes1.plot(x,y)
axes2.plot(y,x)

plt.show()

"""# Using subplots in OO Aproach"""

# Empty canvas pf 3 by 3 subplots
fig, axes = plt.subplots(nrows=3, ncols=3)

# Avoid overlapping using tight_layout() method

# Empty canvas pf 3 by 3 subplots
fig, axes = plt.subplots(nrows=3, ncols=3)
plt.tight_layout()

# Plot x and y in the above canvas using the index position

# Empty canvas pf 3 by 3 subplots
fig, ax = plt.subplots(nrows=3, ncols=3)

ax[0,0].plot(x,x)
ax[0,2].plot(x,y)
ax[2,0].plot(y,x)
ax[2,2].plot(y,y)

plt.tight_layout()

"""# Exercise 2: Try to set the title and  x and y labels of the above axes that are plotted"""

# Exercise 2 solution

# Empty canvas pf 3 by 3 subplots
fig, ax = plt.subplots(nrows=3, ncols=3)

ax[0,0].plot(x,x)
ax[0,0].set_xlabel('X Label Axes 1')
ax[0,0].set_ylabel('Y Label Axes 1')
ax[0,0].set_title("First Axes Title")


ax[0,2].plot(x,y)
ax[0,2].set_xlabel('X Label Axes 2')
ax[0,2].set_ylabel('Y Label Axes 2')
ax[0,2].set_title("Second Axes Title")

ax[2,0].plot(y,x)
ax[2,0].set_xlabel('X Label Axes 3')
ax[2,0].set_ylabel('Y Label Axes 3')
ax[2,0].set_title("Third Axes Title")

ax[2,2].plot(y,y)
ax[2,2].set_xlabel('X Label Axes 4')
ax[2,2].set_ylabel('Y Label Axes 4')
ax[2,2].set_title("Fourth Axes Title")


plt.tight_layout()

"""### Figure size, aspect ratio, and DPI"""

fig = plt.figure(figsize=(2,2), dpi = 100)

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
plt.show()

# Same thing with subplots()

fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(8,8), dpi = 100)

ax[0,0].plot(x,x)
ax[0,2].plot(x,y)
ax[2,0].plot(y,x)
ax[2,2].plot(y,y)

plt.tight_layout()
plt.show()

fig.savefig('my_figure.png')

"""# Displaying the image"""

import matplotlib.image as mpimg

plt.imshow(mpimg.imread('my_figure.png'))

"""# Legends"""

fig = plt.figure(figsize=(8,6), dpi = 60)
ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2, label= "X Square plot")
ax.plot(x, x**3, 'red', label= "X Cube plot")
ax.legend()

"""# Plot appearance

# Useful links for list of options

### [link1](https://matplotlib.org/api/markers_api.html)

### [link2](https://matplotlib.org/2.0.1/api/lines_api.html)
"""

fig = plt.figure(figsize=(8,6), dpi = 60)
ax = fig.add_axes([0,0,1,1])

ax.plot(x, y, color='purple', linewidth=3, linestyle="--", marker='o', markersize=8)

"""### Plot range
### we can choose to show only plots between 0 to 1 of the x axis, and 0 to 5 of the y axis
"""

fig = plt.figure(figsize=(8,6), dpi = 60)
ax = fig.add_axes([0,0,1,1])
ax.plot(x, y, color='purple', lw=3, ls="--")
ax.set_xlim([0,7])
ax.set_ylim([0,50])

"""# Specilized plots

### Histogram
"""

# Histogram
x = np.random.randn(1000)
plt.hist(x)
plt.show()

"""### Time series (Line plot)"""

import datetime
x = np.array([datetime.datetime(2018, 9, 28, i, 0) for i in range(24)])
y = np.random.randint(100, size=x.shape)

plt.plot(x,y)
plt.show()

"""### Scatter plots"""

fig, ax = plt.subplots()
x = np.linspace(-1, 1, 50)
y = np.random.randn(50)
ax.scatter(x, y)
plt.show()

"""### Bar graphs"""

import pandas as pd
my_df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
#print(my_df)
my_df.plot.bar()
plt.show()

"""# Matplotlib with Pandas

## Graphs applied to Covid19 dataset
"""

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 500) #SHOW UP TO 500 COLUMNS
pd.set_option('display.max_rows', 500) #SHOW UP TO 500 ROWS

df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")

new_column_names_dict = {
    'data': 'date',
    'stato': 'state',
    'codice_regione': 'region code',
    'denominazione_regione': 'region name',
    'lat': 'latitude',
    'long': 'longitude',
    'ricoverati_con_sintomi': 'hospitalized_with_symptoms',
    'terapia_intensiva': 'intensive care',
    'totale_ospedalizzati': 'total hospitalized',
    'isolamento_domiciliare': 'home isolation',
    'totale_positivi': 'total positives', 
    'variazione_totale_positivi': 'total positive change',
    'nuovi_positivi': 'new positives',
    'dimessi_guariti': 'discharged healed',
    'deceduti': 'deceased',
    'totale_casi': 'total cases',
    'tamponi': 'tampons',
    'casi_testati': 'total tests',
    'note_it': 'notes in italian',
    'note_en': 'notes in english'
}


df.rename(columns = new_column_names_dict, inplace = True)
df.head()
df['date'] = pd.to_datetime(df.date).apply(lambda x: x.date())
df['date'] = pd.to_datetime(df.date)

df.tail(100)

"""## Date vs Total cases"""

total_df = df.groupby(by=['date'])['total cases'].sum()
total_df.plot()
plt.title("Date vs Total cases")
plt.xlabel('Date')
plt.ylabel('Total cases')
plt.show()

"""## Using Log scale"""

total_df.plot(logy=True)
plt.title("Date vs Total cases")
plt.xlabel('Date')
plt.ylabel('Total cases')
plt.show()

"""## Bar chart"""

total_s = df.groupby(by=['region name'])['new positives'].sum()

total_s.plot.bar(stacked=True)
plt.title("Region vs Total cases")
plt.xlabel('Region')
plt.ylabel('Total cases')
plt.show()

total_s.plot.barh()
plt.title("Region vs Total cases")
plt.xlabel('Total cases')
plt.ylabel('Region')
plt.show()

"""## Pie chart"""

total_s.plot.pie(figsize=(16,16))
plt.title("Total cases by region")
plt.show()

"""## Line plot"""

total_c = df.groupby(by=['date'])['new positives'].sum()
total_c.plot.line()
plt.title("Date vs New daily cases")
plt.xlabel('Date')
plt.ylabel('New cases')
plt.show()

#pd.to_datetime(df['date'].tail().to_list()[0]).date()

date_val = df['date'][len(df['date']) - 1]
mask = df['date'] == date_val
f_df = df[mask]

#f_df.head()

f_df = f_df[['region name', 'deceased']]
f_df.plot.bar(x='region name', y='deceased')
plt.title("Region vs Deceased")
plt.xlabel('Region')
plt.ylabel('Deceased')
plt.show()

import datetime
total_df = df.groupby(by=['date'])['total cases'].sum()

x = np.array([datetime.datetime(i) for i in total_df['date']])
y = df['']

plt.plot(x,y)
plt.show()

"""## Useful reference links

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html

https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
"""