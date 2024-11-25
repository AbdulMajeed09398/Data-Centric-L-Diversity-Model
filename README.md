# Data-Centric-L-Diversity-Model

This repository encloses implementation Codes/Functions used in the Data-centric L-diversity model (Synthetic data-aided anonymization model).

Main Modules of the proposed DLD  **
<br>
There are two key modules in the proposed DLD model.
<br>
1- Data Pre-processing
<br>
In this module, the data to be anonymized is pre-processed to make it anonymization-ready. The key difference between pre-processing and underlying data is that it is free of different vulnerabilities. Although some methods employ pre-processing, only a few areas are improved. This work innovates the existing work and amalgamates synthetic data with real data to address the distribution imbalance problem. When the class imbalance problem is addressed then the constraints regarding SA values and distributions are effectively met whereas most of the existing methods do not fix this problem, leading to two crucial design problems (i.e., expose privacy or leave many records un-processed).**
<br>
2- Shallow Anonymization
<br>
In this module, minimal necessary anonymization is applied to curate high-quality data. Specifically, the pattern-friendly attributes are first identified using the customized implementation of random forest and are minimally generalized to yield privacy-preserved data. It is worth noting that privacy is not risked due to minimal generalization as there exists higher uncertainty in the SA column.
<br>
