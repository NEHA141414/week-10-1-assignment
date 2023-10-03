#!/usr/bin/env python
# coding: utf-8

# Q-1. What is Statistics ?

# Ans-1 STATISTIC module is a handy tool for performing basic statistical operations without the need for additional external libraries .Howerver ,for more advanaced or specialized statistical analyses ,you might need to use other libraries like Numpy ,Scipy ,or pandas ,which offer a broader range of functionalities.

# Q-2 Define the different types of statistics and give an example pf when each type might be used.

# Ans-2 There are two tyes of statistics.
# 1.) DESCRIPTIVE :- This statistics are used to summarize and describe the main features of a dataset .They provide a clear and concise summary of the main.
# EXAMPLE :-
# 1. MEAN : The average value of a dataset.
# 2. MEDIAN : The middle value in a dataset when arranged in ascending order.
# 3. MODE : The most frequently occurring value in a dataset.
# 4. RANGE : The difference between the highest and lowest values in a dataset.
# 5. STANDARD DAVIATION : A measure of the spread or dispersion of data points around the mean .
# 
# 2.) INFERENTIAL STATISTICS :- Inferential statistic are used to make predictions , inferences , or draw conclusions about a larger population based on a sample of data .They involve hypothesis testing and estimating population parameters.
# EXAMPLE :
# 1. HYPOTHESIS TESTING : Assessing if there is a significant difference or relationship between variable in a population .
# 2. REGRESSION ANALYSIS : Examining the relationship between one dependent variable and one or more independent variable.
# 3. CONFIDENCE INTERVALS : Estimating the range of value likely to contain the true population parameter.
# 4. ANOVA(ANALYSIS OF VARIANCE): Comparing maens of multiple groups to see if they are significantly different .

# Q-3 What are the different types of data and how do they differ from each other ? Provide an example of each type of data.

# Ans-3 There are four main type of data :
# 
# 1. NOMINAL DATA : Nominal data consists of categories with no inherent order or ranking .It only allows for labeling or ctegories items.
# Example : Colors ,gender, types of fruits etc .
# 2. ORDINAL DATA : Ordinal data represent categories with a meaningful order or ranking ,but the intervals between them are not consistent or meaningful.
# Example: Education levels( e.g., High school, bachelors , masters phd) etc
# 3. INTEVAL DATA : Inteval data have consistent intervals beetween values ,but there's no true zero points. This maens that you can performs addition and subtraction , but not meaningful multiplication or division.
# Example : Temerature in celsius or fahrenheit.
# 4. RATIO DATA : Ratio data have a true zero points meaning that its possible to perform all basic arithmetic operations. This type of data provide the most information .
# Example : age ,height ,weight ,income etc

# Q-4 Categories the following dataset with respect to quantative and qualitative data types :

# QUANTATIVE DATASET : 1. Height data of a class.
#                      2. Number of mangoes exported by a form .
#                    
# QUALITATIVE DATASET : 1. Grading in exam.
#                       2. Color of mangoes.

# Q-5 Explain the concept of levels of measurment and give an example of a variable for each level .

# Ans-5 The level of measurement, also knowns as the scale of measurment ,refers to the way in which data is measured or categorized .It define the properties of the data and the mathematical operations that can be applied to it.
# there are mainly four levels of measurment : 1. Nominal ,2. Ordinal , 3. Interval ,4.Ratio.

# Q-6 Why is it important to understand the level of measurment when analyzing data ? Provide an example to illustrate your answer.

# Ans-6 Understand the level of measurement is crucial when analyzing data because it dterrmines the types of statistical analyses that can be appropriately applied .Using the wrong analysis for a given level of measurement can lead to incorrect conclusions and misleading interpretations.
# Illustrate: 
#           suppose we have a dataset containing information about different types of cars , including their colors and the order in which they were manufactured .we will focus on two variables "color" and "manufacturing order".
#  1. COLOR(Nominal level): This variable represents the color of cars ,, which is at the nominal level of measurement.
#  2. MANUFACTURING ORDER(Ordinal level): This varaible represent the order in which is at the ordinal level of measurement .

# Q-7 How nominal data type is different from ordinal data type.

# Ans-7 NOMINAL DATA: Nominal data involves categories or labels that do not have any inherent order or ranking .The categories are distinct and mutually exclusive but they do not have a meaningful numerical value associated with them.
# ORDINAL DATA: Ordinal data involves categories with a meaningful order or ranking .While there is an order , the intervals between the categories are not consistant or meaningful.
# 
# DIFFERENCE :The key difference between nominal and ordinal data lies in the presence of meaningful order in ordinal data .While nominal data only categories without any inherent order , ordinal data adds the aspect of meaningful ranking .This means you can says one category is "higher" or "lower" than another , but you cannot determine the exact interval between them .

# Q-8 Which type of plot can be used to display data in terms of range?

# Ans-8 A plot that can effectively display data in terms of range is a BOXPLOT (also known as a whisker plot or box-and-whisker plot).
#     A BOXPLOT provides a visual representation of the distribution of a dataset and highlights the central tendency ,spread ,and any potential outliers .It specifically shows the minimum , first quartile (Q1) ,median(Q2) ,tjird quartile(Q3) ,and maximum

# Q-9 Describe the difference between descriptive and inferential statistics .Give an example of each type of statistics and explain how they are used.

# Ans-9 DESCRIPTIVE STATISTICS : Descriptive statistics involve methods for summarizing and describing the main features of dataset. They provides a clear and concise summary of the main characteristics of the data , allowing for easy interpretation .
# EXAMPLE : Consider a class of students and thier exam scores. Descriptive statistics would be used to calulate the mean score ,find the most comman score (mode) ,and determine how spread out the scores are(e.g. using standard deviation).
# 
# USAGE: 1. Provides a snapshot or summary of a dataset.
#        2. Helps in understanding the central tendency ,spread ,and shape of the data distribution.
#        
#        
# INFERENTIAL STATISTICS: Inferential statistics are used to make predictions , inferences , or draw conclusions about a larger population based on a sample of data .They involve hypothesis testing and estimating population parameters.
# 
# EXAMPLE : Suppose you want to know if a new drug is effective in reducing blood pressure .You might conduct an experiment on a sample of patients and use inherential statistics to determine if the observed effects are likely to apply to the broader population.
# 
# USAGE: 1. Allow us to draw conclusions about a population based on a sample.
#        2. Provides estimates of population parameters with confidence intervals.
#        
# DIFFERENCE : Descriptive statistics are used to summarize and understand data , providing a snapshot of its features while inferrential statistics are employed to make predictions about larger populations based on sample data .Both types of statistics play critical roles in various fields ,including science ,business ,social science ,and more.

# Q-10 What are some common measures of central tendency and variability used in statistics ? Explain how each measure can be used to describe a dataset.

# Ans-10 Here are some common measures and how they can be used:
# 
# MEASURES OF CENTRAL TENDENCY:
# 
# 1. MEAN : The mean is the average of sets of values .It's calculated by adding up all the values and dividing by the total numbers of values.
# 2. MEDIAN : The median is the middle value in a dataset when the data is ordered from lowest to highest.It's not affected by extreme values (outliers).
# 3. MODE : The mode is the value that occurs most frequently in a dataset.
# 
# MEASURES OF VARIABILITY:
# 
# 1. RANGE : The range is the difference between the highest and lowest values in a dataset .
# 2. VARIANCE and STANDARD DEVIATION : Variance measures the average squared difference of each data points from the mean .Standard deviation is the square root of the variance.
# 3. INTERQUARTILE RANGE(IQR) : The IQR is the range between the first quartile (Q1) and the third quartile(Q3) in a dataset.
# 

# In[ ]:




