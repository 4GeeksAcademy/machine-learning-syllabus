# -*- coding: utf-8 -*-
"""seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HN6LoNzjMhrFHvfiJPf73afNnpquTYTd

## Importing required libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats

"""## Load the datasets from Git directly"""

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

titanic.head(2)

# Regions data
# https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv

# Province data
# https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv

# Total data
# https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv


regions_df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")

province_df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv")

total_df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")

# Renaming columns for the sake of readability
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
    'note_en': 'notes in english',
    'codice_provincia': '',
    'denominazione_provincia': 'province name',
    'sigla_provincia': 'province abbreviation'
    
}

# Function for renaming columns and reformmating the date
def preprocess_df(df):
    df.rename(columns = new_column_names_dict, inplace = True)
    df['date'] = pd.to_datetime(df.date).apply(lambda x: x.date())
    df['date'] = pd.to_datetime(df.date)
    
    return df

regions_df = preprocess_df(regions_df)

regions_df.tail(2)

province_df = preprocess_df(province_df)

province_df.columns = ['date', 'state', 'region code', 'region name', 'province code', 'province name',
       'province abbreviation', 'latitude', 'longitude', 'total cases',
       'notes in italian', 'notes in english']

province_df.tail(2)

total_df = preprocess_df(total_df)
total_df.tail(2)

"""## Barplot using Seaborn

### For total cases
"""

# Get all the unique dates
dlist =  pd.to_datetime(total_df['date']).apply(lambda x: x.date()).unique()
# print(len(dlist))

plot_ = sns.barplot(dlist, total_df['total cases'])
for ind, label in enumerate(plot_.get_xticklabels()):
    if ind % 25 == 0:  # every 25th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.show()

"""## For number of positive cases"""

plot_ = sns.barplot(dlist, total_df['total positives'])
for ind, label in enumerate(plot_.get_xticklabels()):
    if ind % 25 == 0:  # every 25th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.show()

"""## For change in number of positive cases"""

plot_ = sns.barplot(dlist, total_df['total positive change'])
for ind, label in enumerate(plot_.get_xticklabels()):
    if ind % 25 == 0:  # every 25th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.show()

"""### Multiple subplots using Seaborn"""

f_list = ['date', 'state', 'notes in italian', 'notes in english']

# Filter out the columns that we do not need
col_list = [i for i in total_df.columns if i not in f_list]

print(col_list)

num_plots = len(col_list)
total_cols = 3
total_rows = num_plots//total_cols
fig, axs = plt.subplots(nrows=total_rows, ncols=total_cols,
                        figsize=(6*total_cols, 6*total_rows), constrained_layout=True)

index = 0
for col in col_list:
    
    row = index //total_cols
    pos = index % total_cols
    
    plot_ = sns.barplot(dlist, total_df[col], ax=axs[row][pos])
    
    for ind, label in enumerate(plot_.get_xticklabels()):
        if ind % 25 == 0:  # every 25th label is kept
            label.set_visible(True)
        else:
            label.set_visible(False)
    
    index += 1

plt.show()
plt.tight_layout()

"""## Scatterplot using Seaborn
 
A scatterplot is perhaps the most common example of visualizing relationships between two variables. Each point shows an observation in the dataset and these observations are represented by dot-like structures. The plot shows the joint distribution of two variables using a cloud of points.

To draw the scatter plot, we’ll be using the relplot() function of the seaborn library. It is a figure-level role for visualizing statistical relationships. By default, using a relplot produces a scatter plot.
"""

total_df.head(2)

sns.relplot(x="total positives", y="new positives", data = total_df)
plt.show()

"""### Next, if we want to see the tag associated with the data, we can use the below code:"""

sns.relplot(x="total positives", y="new positives", hue = "date", data = total_df)
plt.show()

"""In the above plot, the hue semantic is categorical. That’s why it has a different color palette. If the hue semantic is numeric, then the coloring becomes sequential."""

sns.relplot(x="total positives", y="new positives", hue = "deceased", data = total_df)
plt.show()

"""### We can also change the size of each point:"""

sns.relplot(x="total positives", y="new positives", size = "deceased", data = total_df)
plt.show()

"""## Plotting Categorical Data

## Boxplot using seaborn

Another kind of plot we can draw is a boxplot which shows three quartile values of the distribution along with the end values. Each value in the boxplot corresponds to actual observation in the data. Let’s draw the boxplot now-
"""

sns.catplot(x="region code", y="total cases", data = regions_df)
plt.show()

"""Since we can see that the plot is scattered, so to handle that, we can set the jitter to false. Jitter is the deviation from the true value. So, we’ll set the jitter to false by using another parameter."""

sns.catplot(x="region code", y="total cases", jitter = False,  data=regions_df)
plt.show()

# Only last five rows, we can also use tail() method
#total_df['date'][-5:]

sns.catplot(x="region code", y="total cases", kind = "box", data = regions_df)
plt.show()


r_df = regions_df[['region code', 'region name']].copy()

print(r_df.drop_duplicates().sort_values('region code'))

#print(regions_df[['region code', 'region name']])

"""## Hue Plot
Next, if we want to introduce another variable or another dimension in our plot, we can use the hue parameter just like we used in the above section. Let’s say we want to see the gender distribution in the plot of education and avg_training_score
"""

sns.catplot(x="region code", y="total cases", hue = "province abbreviation", data=province_df)
plt.show()

"""## Violin Plot using seaborn
We can also represent the above variables differently by using violin plots. Let’s try it out
"""

titanic.columns

sns.catplot(x="embark_town", y="fare", hue = "who", kind = "violin", data=titanic)
plt.show()

"""The violin plots combine the boxplot and kernel density estimation procedure to provide richer description of the distribution of values. The quartile values are displayed inside the violin. We can also split the violin when the hue semantic parameter has only two levels, which could also be helpful in saving space on the plot. Let’s look at the violin plot with a split of levels."""

sns.catplot(x="embark_town", y="fare", hue = "alive", kind = "violin", split = True, data=titanic)
plt.show()

sns.catplot(x="embark_town", y="fare", hue = "sex", kind = "violin", split = True, data=titanic)
plt.show()

sns.catplot(x="embark_town", y="fare", hue = "alone", kind = "violin", split = True, data=titanic)
plt.show()

"""## Swarm plot
Using swarm plot we can visualize higher dimension relationships
"""

sns.catplot(x="embark_town", y="fare", hue="who",
            col="sex", aspect=.9,
            kind="swarm", data=titanic)
plt.show()

sns.catplot(x="embark_town", y="age", hue="who",
            col="class", aspect=.9,
            kind="swarm", data=titanic)
plt.show()

sns.catplot(x="embark_town", y="age", hue="sex",
            col="who", aspect=.9,
            kind="swarm", data=titanic)
plt.show()

sns.catplot(x="embark_town", y="age", hue="sex",
            col="alone", aspect=.9,
            kind="swarm", data=titanic)
plt.show()

"""# Barplot using seaborn

Barplot operates on the full dataset and obtains the mean value by default.

"""

sns.catplot(x="region code", y="total cases", kind = "bar", data = regions_df)
plt.show()

"""## Visualizing the Distribution of a Dataset 

Whenever we are dealing with a dataset, we want to know how the data or the variables are being distributed. 

Distribution of data could tell us a lot about the nature of the data

### Plotting Univariate Distributions

One of the most common plots you’ll come across while examining the distribution of a variable is distplot. 

By default, distplot() function draws histogram and fits a Kernel Density Estimate.
"""

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

titanic.head()

sns.distplot(titanic['age'])
plt.show()

"""This clearly shows that the majority of people are in their late twenties and early thirties.

## Histogram using Seaborn 

Another kind of plot that we use for univariate distribution is a histogram. 

A histogram represents the distribution of data in the form of bins and uses bars to show the number of observations falling under each bin. 

We can also add a rugplot in it instead of using KDE (Kernel Density Estimate), which means at every observation, it will draw a small vertical stick.
"""

sns.distplot(titanic['fare'], kde=False, rug = True)
plt.show()

sns.distplot(titanic['age'], kde=False, rug = True)
plt.show()

"""## Plotting Bivariate Distributions 

Apart from visualizing the distribution of a single variable, we can see how two independent variables are distributed with respect to each other. 

Bivariate means joint, so to visualize it, we use jointplot() function of seaborn library. 

By default, jointplot draws a scatter plot. 
"""

sns.jointplot(x="total positives", y="deceased", data=total_df);
plt.show()

"""## Hexplot using Seaborn 

Hexplot is a bivariate analog of histogram as it shows the number of observations that falls within hexagonal bins. 

This is a plot which works with large dataset very easily. 

To draw a hexplot, we’ll set kind attribute to hex. Let’s check it out now.
"""

sns.jointplot(x="total positives", y="deceased", kind="hex", data=total_df)
plt.show()

"""## KDE Plot using Seaborn"""

sns.jointplot(x="total positives", y="deceased", kind="kde", data=total_df)
plt.show()

"""### Heatmaps using Seaborn

Heatmaps are graphical representations in which each variable is represented as a color.
"""

corrmat = total_df.corr()
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(corrmat, vmax=.8, square=True)
plt.show()

"""### Visualizing Pairwise Relationships in a Dataset

We can also plot multiple bivariate distributions in a dataset by using pairplot() function of the seaborn library. 

This shows the relationship between each column of the database. 

It also draws the univariate distribution plot of each variable on the diagonal axis. 

"""

sns.pairplot(total_df)
plt.show()

"""### References
https://towardsdatascience.com/dynamic-subplot-layout-in-seaborn-e777500c7386

"""