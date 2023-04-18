---
title: "proposal"
author: "Julia Van Heeringen"
date: "9/28/2022"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

Title of the talk: Predicting NBA Final Four Teams

Name(s): Julia Van Heeringen and Louise Lalescu

A brief description of the research topic, including some background and why it is important and what we know/don’t know about it (knowledge gap):
  It is very common for people to design NBA playoff brackets based off of who they think will advance after each round and ultimately win the play-offs. However, the brackets are often designed without giving much thought to statistics or machine learning models. For this reason, we want to develop a classification algorithm that will predict which teams make it to the semi-finals. The gaps in our knowledge currently include what the major indicators of NBA Final Four are and how we can accurately predict which teams will make it to the semi-finals.

A brief description of the data required, and how would you get such data:
  The data that is needed is data for each team during the 2021-2022 season and the list of teams that made the final four during this season. Data for team totals can be found here: https://www.basketball-reference.com/teams/BOS/2023.html. Since this is only data for 1 team, we will have to download this for each of the 30 teams and then ultimately combined all of the data into one large dataframe. This data contains the total values of various game statistics such as points made, offensive rebounds, free throws, etc. for each player on the team. We would most likely have to sum the values for each player to create a dataframe of 30 rows (one row for each team), and then create a column for whether or not they made the final four, which we can research online.

A list of questions and corresponding analysis tasks you plan to do:
  The question we hope to answer is: which teams are predicted to make the final four? What are the most significant factors in making the final four? How accurately can out model predict which teams make it to the final four? The reason we chose final four and not the finals or the winners is because we were worried that our testing set would be too small.


