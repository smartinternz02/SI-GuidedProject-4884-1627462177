# Natural Gas Price Detection Using Machine Learning Model

## Introduction
### Overview
Forecasting natural gas prices is a powerful and essential tool which has become more important for different stakeholders in the natural gas market, allowing them to make better decisions for managing the potential risk, reducing the gap between the demand and supply, and optimising the usage of resources based on accurate predictions.
 
### Purposed
Accurate natural gas price forecasting not only provides an important guide for effective implementation of energy policy and planning, but also is extremely significant in economic planning, energy investment, and environmental conservation. 
The aim of this project is to build data-driven machine learning models for natural gas price forecasting.

## Literature Survey
### Existing Problem
The poor track record of energy price forecasting models has encouraged analysts to turn to other sources of information about future energy prices, including most prominently, energy futures markets. Energy futures markets are 'hubs' that price and market natural gas. Walls (1995), examining several years of spot prices finds that, in general, gas futures are unbiased predictors of future spot prices whereas Herbet (1993) finds bias in natural gas futures prices where futures prices are greater than realised spot prices. Chinn et al (2005) finds futures prices to be unbiased predictors of future spot prices, with the exception of those in the natural gas market at the three month horizon and they slightly outperform time series models.
### Proposed Solution
Using the data set of prices provided from the 7th of January 1997 until 11th of august 2020, we will be trying to predict the prices of natural gas by testing through various machine learning models and providing a real-time web based GUI to ask the user to enter the desired date to predict the rate of the natural gas on that particular day. This study builds upon the existing literature by investigating the accuracy of various forecast methods until the best fit horizon is reached.

## Theoretical Analysis
### Block Diagram
![Image](https://github.com/suriya-1403/Natural-Gas-Price-Prediction-System/blob/main/Images/Technical%20Architecture.png)
### Software Designing
We will be using the following modules and softwares to help build the project:
- pandas 1.2.4
- matplotlib~ 3.4.2
- pydotplus~=2.0.2
- six~ 1.15.0
- ipython~ 7.24.1
- scikit-learn~=0.24.2
- seaborn~=0.11.1
- scipy~=1.6.3
- Jupyter Notebook
- Spyder
- IBM Watson Cloud along with Machine Learning module.

And for Deployment into internet we have used Azure.

## Experimental Investigations

The evaluation of the proposed approach is Natural gas price prediction by considering day, month, year on the dataset.
In this the project preprocessing and training of the data set is done by using a jupyter notebook.
After model building we build a web application using flask framework.

## Flow Chart
![Image](https://github.com/suriya-1403/Natural-Gas-Price-Prediction-System/blob/main/Images/Flow%20chart.png)

## Advantages and Disadvantages
| Prediction Model  | Advantages | Disadvantages |
| ------------- | ------------- | ------------- |
| TS models  | The model is relatively simple. It performs well in comparatively stable datasets. Provides good result in short and medium termed forecasts  | Hugely limited in long-term forecasting |
| Regression models  | A simple model, but the modeling speed is fast. Predicts reliably and can indicate the relationship and influence strength between independent variable and the dependent variable.  | In some cases, the choice and expression of factors are purely speculative and limited in application. |
| ANN based models  | It has a strong nonlinear fitting ability, simple self learning rules, and easy to perceive by a computer. It has strong robustness, memory ability, non linear mapping ability and strong self learning ability. | The interpretability of this model is poor and prone to overfitting |
| SVM based models  | It performs better in small sample problems with a basic algorithm and strong robustness | It is difficult to implant for large scale training samples. Sensitive to missing data, choice of parameters and kernel functions. |
| Decision Tree Based Models | The model has strong generalization ability,can be trained fast,and is not sensitive to missing data | If there is noise in the data it is prone to overfitting. |

## Application
Natural gas accounts for 1/4 of the global demand and roughly 1/3 of the US energy demand. After oil, Natural gas is the most dominant sort of energy. So, being about to improve natural gas demand prediction is extremely valuable.
The accurate prediction of energy price is critical to the energy market orientation, and it can provide a reference for policymakers and market participants. In practice, energy prices are affected by external factors, and their accurate prediction is challenging.Being able to forecast natural gas price benefits various stakeholders and has become a very valuable tool for all market participants in competitive natural gas markets. Machine learning algorithms have gradually become popular tools for natural gas price forecasting.

## Conclusion
It has always been a difficult task to predict the exact daily price of natural gas price. Many factors such as political events, general economic conditions, and traders’ expectations may have an influence on it. But here, based on the past and present traits, we were able to achieve up to 97% accuracy in predicting the price of any given date. Albeit, its impossible to predict unexpected scenarios such as acts of warfare or terrorism. But, the benefits of having reliable information of what the price of natural gas could be at any given time is paramount, it could make or break economies. And in this case, as this project points out data-driven machine learning models deserve all the attention it could ever garner and even more.

## Future Scope
The project has been built using 2 models of prediction namely the Decision Tree method and Random Forest method with the accuracy score of over 97% on both the models (97.4% on Decision Tree and 97.74% on Random Forest Method). By doing some further research and learning the accuracy can be uplifted upto 100% which would be an ideal prediction real- time application which would be much more helpful in the trading sector.

## Bibliography
- https://smartinternz.com/Student/guided_project_info/4885#
- https://docs.anaconda.com/anaconda/packages/pkg-docs/
- https://www.osti.gov/servlets/purl/908487
- https://towardsdatascience.com/natural-gas-spot-price-prediction-using-artificial-neural-network-56da369b2346
- https://publikationsserver.tu-braunschweig.de/servlets/MCRFileNodeServlet/dbbs_derivate_00027726/Beitrag299.pdf
- https://www.mdpi.com/1996-1073/12/9/1680/pdf
## UI Output Screenshots
![Image](https://github.com/suriya-1403/Natural-Gas-Price-Prediction-System/blob/main/Images/UI%20Image.png)

### Contributors
- [Suriyakrishnan Sathish](https://github.com/suriya-1403)
- [Mohamad Fasil Ansaary M](https://github.com/FasilCR7)
- [M V Namitha](https://github.com/MakamNamitha)
- [Joel Danie Johnson](https://github.com/Joeldanie)

