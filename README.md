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

This is a reasonable-sized dataset encompassing US individuals' diverse information (demographics). The database and privacy community have widely used this dataset for experimentation purposes. Its original form is available at http://archive.ics.uci.edu/dataset/2/adult. 

2- Stroke Prediction Dataset

This data set has been widely used in machine learning, particularly in imbalanced learning problems. Due to its higher imbalance, it has also been widely used in many AI competitions. This dataset in its original form is available at https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset. 

3- Census Income

This is the largest dataset encompassing the diverse information of individuals. The database and privacy community has widely used this dataset also for experimentation purposes. This dataset in its original form is available at:http://archive.ics.uci.edu/dataset/117/census+income+kdd. 

4- Diabetes 130-US Hospitals

This is also the largest dataset encompassing the diverse medical information of individuals fetched from the clinical care at 130 US hospitals and integrated delivery networks. The database and privacy community have also used this dataset for experimentation purposes. This dataset in its original form is available at [https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008].

**Implementation process**


At the outset, it is imperative to install all required libraries. Depending upon the programming language, the necessary libraries should be included in the development environment.
Below we show a sample to install basic data processing libraries and installation procedures in Python.
<code>pip install name of library </code> i.e., <code>pip install numpy, pip install pandas, pip install scikit-learn, pip install scipy</code>.

Below, we provide the code information that can help understand the implementation and reproduce the results.

| File Name | Description of implementation | Output files/information
| ------------- | ------------- | ------------- |
| Arrange_Attributes.py  | Remove direct identifiers and arrange the remaining attributes  | Data with QIDs and SA only (The last column is SA)  |
| Missing_Values_Imputation (When duplicate Removal is needed ).py  | Clean the data from basic vulnerabilities (missing values, outliers, duplicates, etc.)  |Data with basic vulnerabilities fixed  |
| Missing_Values_Imputation (When duplicate Removal is not needed ).py  | Clean the data from basic vulnerabilities (missing values, outliers, etc.)  |Data with basic vulnerabilities fixed   |
| Missing_Values_Imputation (When duplicate Removal is not needed ).py  | Clean the data from basic vulnerabilities (missing values, outliers, etc.)  |Data with basic vulnerabilities fixed   |
| Imbalance_Ratio_Computing_Records Analysis.py  | Analyze the imbalance w.r.t. SA & find the # of records needed for balance  |Imbalance ratio information, and size of Dnew required for data balancing  |
| Interface_Program_SD_Generation.py  | Generating synthetic data[^1] to balance the distribution of rare SA value  | Synthetic data with identical structure to real data  |
| Data_Balancing_by_Adding_Dnew.py  | Generating balancing data by mixing Dnew and real data (only augmenting the rare SA class)  | Balanced and clean dataset (Most vulnerabilities are fixed)  |
| Feature_Scores  (Best value Combinations are Desirable).py  | Identifying pattern friendly QIDs from the data  | Scores of the QIDs w.r.t. pattern information  |
| KLDCriteria_Aware_Clustering.py  | Clustering data as per k and l value  | Clustered data where the size of each cluster is at least k and every cluster is 2-diverse  |
| QIDs-Values_Replacements.py  |Generalized data with lower level generalization | Generalized data where the functional relationship between real and anonymized data is high |

[^1]: The open-source implementation was used with slight modifications (https://github.com/sdv-dev/CTGAN). 
[^2]: The information/details about the generalization heirarchies (https://www.sciencedirect.com/science/article/pii/S2667305323000923). 



The file <code> generalization_mappings.json </code>  provides a generalized hierarchy information sample for QIDs that can assist in generalization when called from the main program. Further information regarding the construction of heirarchies can be learned from a recent study[^2]. The file <code> requriements.txt </code>  provides the Python libraries that are required to execute the code.

**Citing DCLD**

If you use the DCLD implementation, please cite the following work:

[1] Citation will be added soon.

