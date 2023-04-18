# Final project progress report
### ISTA421/INFO521

-------

Project: [Predicting Final Four NBA Teams]
Names:
- [Louise Lalescu]
- [Julia Van Heeringen]    

-------


## Instructions

You report should be a short summary of your project progress. This report is relevant to to us, your instructors, and probably to the rest of the class.

Please use this report as a chance to organize your thoughts about what you are trying to do with your project, and to get feedback on your ideas, and the approaches that you have tried so far.

## Submission

Please commit this file to your GitHub repo (progress.md) AND to D2L.


-------

### GitHub repo usage
_Describe the current structure of your repo, the number of commits, and the steps you have taken to ensure the reproducibility of your code_

We haven’t really been committing to the GitHub repo often since we are working with a colab notebook that saves automatically. We are going to try to update this repo with our current changes more often. We had some issues accessing the data from our google drive folder, but have figured out a way to make it reproducible for both of us to be able to run the code and read in the files from our own google drives.


### Summarize your data
_Describe the characteristics of your data, any transformations that you have considered, or potential issues that you have faced (e.g. missing data)_

We have a file for each team, which we had to read in and concatenate together to get one large file that contains all of the players from the 30 teams we selected. The last row in each of the files is totals rather than a row representing a player, so we may have to remove it and place it into its own dataframe with team totals. We have some players with NaN values and we suspect that these are players that never played, so we need to verify whether or not this is true so that we may consider dropping them to create a more accurate model of players.

### Describe your initial analysis strategy
_What was your initial plan?_

Our initial plan was detecting credit card fraud, but the column names were not descriptive enough to be able to identify features, so we changed our project to basketball data. We wanted to create a predictive model so we decided to predict which teams will make it to the final four. Our plan as of right now is to continue cleaning our data, create 2 data frames (one with all players and one with the players who actually played during the season), and then group by team so that we eventually have 2 data frames where each of the rows represent a team and their average aggregated data. From there, we plan to implement a logistic regression model on both data frames to see whether or not removing players who didn’t play as much impacts model accuracy.

### What you have tried so far?
_Describe your current implementation_

We are not ready to fit our model yet, as we struggled to read in our files from google drive and had to work on reformatting the data to fit our needs. We had some extra columns that didn’t match up and had to manipulate the data so that each time had identical columns. We completed this successfully and are now determining which players actually played.

### What worked and what did not
_Describe the challenges that you have faced so far and outline a few take-homes from your experience on this project_


### What you plan to do next...
_Please define explicit goals for each of the remaining weeks (before the presentation is due)_

- Week 1: Finish cleaning the data. Make the 2 player data frames and create a data frame that is grouped by team.
- Week 2: Fit and tune a logistic regression model. Possibly implementing another classification model as well.
- Week 3: Finalize model and draw conclusions.

### Author contributions
_Describe the contributions of each of the members to the current version of the project_


Student 1: [Julia Van Heeringen]
- [x ] Development of question / hypothesis;
- [ ] Data research: search for relevant data to contribute to question;
- [ ] Literature review;
- [ x] Analysis strategy;
- [ x] Analysis code;
- [ x] Code review;
- [ x] Work planning and organization;
- [ x] Improving teamwork and collaboration;
- [x] Testing code and procedures;
- [ ] Writing report.
- [ ] Additional comments: Equal efforts made on both parts. Excellent teamwork.

Student 2: [Louise Lalescu]
- [x ] Development of question / hypothesis;
- [x ] Data research: search for relevant data to contribute to question;
- [ ] Literature review;
- [ ] Analysis strategy;
- [ x] Analysis code;
- [x ] Code review;
- [ x] Work planning and organization;
- [ x] Improving teamwork and collaboration;
- [ ] Testing code and procedures;
- [ ] Writing report.
- [ ] Additional comments: Equal efforts made on both parts. Excellent teamwork.
