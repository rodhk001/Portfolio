# Covid Vaccine Analysis Project
## By Kiana Gonzalez-Rodholm

### Project Summary
This project takes data from the status of people who were vaccinated, partially vaccinated, and not vaccinated for COVID 19 from different countries and provides visual and statistical analysis using R. The main business question was to see how the US compared to other countries when it came to vaccination numbers. Some analysis techniques used were CDF and PMF graphs, histograms, pareto and lognormal distribution curves, scatterplots, and correlation charts. There was also a regression model built to see if predicting where the vaccination rates will go was also conducted and presented.

### Findings
I found through my analysis that a lognormal model is a good fit for the distribution of this data. I also found that although slow to start, the US has exponentially grown in vaccine distribution compared to other countries. When comparing different variables together to find correlation, I discovered that total vaccinations and people fully vaccinated are positively correlated and statistically significant. This is to be expected because the higher number of people that are fully vaccinated means that more people had one or two shots, and therefore contribute to the total number of vaccinations. 

### Future Application
Future work that can be done to further continue this analysis would be to better handle the outliers and Nan values in the data. Another great asset would be to get more up to date data, since this set only went up to 2020 and had missing or incomplete data due to the vaccine not being available yet.
