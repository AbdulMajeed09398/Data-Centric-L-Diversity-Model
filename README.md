# Data-Centric-L-Diversity-Model

This repository encloses implementation Codes/Functions used in the Data-centric L-diversity (DCLD) model (Synthetic data-aided anonymization model).

Main Modules of the proposed DCLD 
<br>
There are two key modules in the proposed DCLD model.
<br>
1- Data Pre-processing
<br>
In this module, the data to be anonymized is pre-processed to make it anonymization-ready. The key difference between pre-processing and underlying data is that it is free of different vulnerabilities. Although some methods employ pre-processing, only a few areas are improved. This work innovates the existing work and amalgamates synthetic data with real data to address the distribution imbalance problem. When the class imbalance problem is addressed then the constraints regarding SA values and distributions are effectively met whereas most of the existing methods do not fix this problem, leading to two crucial design problems (i.e., expose privacy or leave many records un-processed).**
<br>
2- Shallow Anonymization
<br>
In this module, minimal necessary anonymization is applied to curate high-quality data. Specifically, the pattern-friendly attributes are first identified using the customized implementation of random forest and are minimally generalized to yield privacy-preserved data. It is worth noting that privacy is not risked due to minimal generalization as there exists higher uncertainty in the SA column.
<br>
.....
Next, we provide the details of the implementation that can help the re-implementation of the proposed model.

**Dataset used in Experimentation**

Four real-world publicly available datasets have been used to evaluate the effectiveness of the proposed DCLD.

1-Adult

This is a reasonable-sized dataset encompassing US individuals' diverse information (demographics). The database and privacy community has widely used this dataset for experimentation purposes. This dataset in its original form is available at: http://archive.ics.uci.edu/dataset/2/adult. 

2- Stroke Prediction Dataset

This data set has been widely used in machine learning, particularly, in imbalanced learning problems. This dataset has been widely used in many AI competitions due to higher imbalance. This dataset in its original form is available at: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset. 

3- Census Income

This is the largest dataset encompassing the diverse information of individuals. The database and privacy community has widely used this dataset also for experimentation purposes. This dataset in its original form is available at:http://archive.ics.uci.edu/dataset/117/census+income+kdd. 

4- Diabetes 130-US Hospitals

This is also the largest dataset encompassing the diverse medical information of individuals that was fetched from the clinical care at 130 US hospitals and integrated delivery networks. The database and privacy community has used this dataset also for experimentation purposes. This dataset in its original form is available at:[https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008].

**Implementation process**

At the outset, it is imperative to install all required libraries. Depending upon the programming language, the necessary libraries should be included in the development environment.
Below we show a sample to install basic data processing libraries and installation procedures in Python.
<code>pip install name of library </code> i.e., <code>pip install numpy, pip install pandas, pip install scikit-learn, pip install scipy</code>.


