# Video Game EDA
## By Kiana Gonzalez-Rodholm
### Project Summary
This project will focus on video game sales by performing an exploratory data analysis along with predictive modeling to gather information for future game designs. Some of the business problems that will be addressed include: What makes a great video game? What console is the higher selling console or platform? Which games had the highest sales? Can we predict what games might do well in the future? Did the 2020 pandemic affect sales positively or negatively?

The data is a csv file that was pulled off Kaggle, containing video game data for games that sold over 100,000 copies. There are 16,598 records of games and include features for each game including platform, genre, publisher, year of release, and different sales brackets.

### Methods and Findings
Some of the methods used for this analysis included using the matplotlib, seaborn, and plotly packages to create various visualizations from the data. I went to the model building phase where I made a linear regression model and a clustering algorithm to group the games into different classes. Outside of Python I used Tableau to further create more professional looking visualizations that would be reflective of my findings.

I discovered that out of all the genres, the most profitable were action and sports. When it came to platform, most users tended to buy games that were found on the PS2, but with Xbox360, Wii, PS3, and DS close behind. When looking over time, there was a huge spike in gaming sales from 2000-2015, peaking in 2008. The data does show a drop in game sales in 2020, but it is possible that the results of this study did not fully account for the full year. Overall, the distribution of sales was not surprising, with North America leading the way in sales of all genres, followed by Europe and then Japan. Other than Wii Sports, some of the other top selling games were Super Mario Bros., Mario Cart Wii, Wii Sports Resort, and Pokémon Red/Blue. Out of all the publishers, Nintendo was number one, followed by Electronic Arts, Activision, and Sony.

After these initial findings I created a linear regression model which revealed an accuracy of 99%. I then decided to go a different route by creating a clustering algorithm to group the various sales of games into four different clusters. This could then be used to analyze each cluster individually to compare further as to what did well and what did not.

### Future Aplication
I believe some future uses that can stem from this project include a deeper dive into the modeling process. To try out more models with more parameter adjustments to find something that can work better without any overfitting. Some additional applications would be once more data is released following the pandemic, more analysis can be done in order to find out exactly how much the gaming industry was affected by the pandemic.
