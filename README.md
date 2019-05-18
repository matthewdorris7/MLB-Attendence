# MLB-Attendence

Analyzing trends with Nationals Park attendance to see if there was any predictive power on the attendance at games

# Data

Web Scraped the data from basebballreference.com for games at Nationals park over the last 8 years. The ataset consisted of the date, time of the game, day of the week, and temperature.

# Regression Trees

The response variable, attendance, is continuous, and I wanted to characterize the average behavior of attendance as a function of both the categorical and numerical predictors. Regression trees split the predictor space into regions based on the other variables, so the response variable is well represented in each region. These regions are used to make decisions on the data and can be very useful for predictions.

# Data Analysis

When predicting attendance, the day of the week is the most important variable, followed by month, time, and temperature, respectively.

**Please see ResearchPaperAttendance. pdf for further detail
