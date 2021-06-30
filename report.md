# PFAL1
                                                                   LINEAR REGRESSION 
                                                                      
This is my first year [project](https://bit.ly/3h452Kv) in the Data Science Bachelor at [Mohamed 6 Polytechnic University](https://www.um6p.ma/en). The project is an introduction to the machine learning alrgorithms in which
I was asked to find the regression line that suits my dataset in order to estimate the price of a car for a given mileage.

In this project, I mainly used the gradient descent algorithm that helps you find the local minimum of a function. Finding the minimum means finding the best regression line.
In other words, it means that once you hit the minimum of the cost function (by training) then you actually found the best line so that the error is optimized which means 
that the difference between the actual price (of the training dataset) and the estimated price(given from our line) is the smallest. 
By that you'll be finding the variables(a and b) of your line ax+b and you'll be able to estimate new prices of different mileages.

More importantly, the gradient descent has some important parameters that are not given by default and that should actually be tested in order to find them
which are the learning rate as well as the number of iterations. Learning rate is the how big or small your alogirthm will be scaling your function and the number of iterations is 
the number of times your alorgithm will loop to learn. Both of these parameters are very important and can be found using a test function that keeps trying 
different learning rates and different numbers of iterations.

This project helped me get used to numpy arrays as well as the matplotlib library that helped me to visualize the data cloud and the regression line in different ways. I also tried 
to visualize the 3D cost function. Moreover, I got used to excel tables and its manipulation in Python using pandas.
In addition, I've worked on a program that estimates the price of a given mileage using pickle and the tkinter library that allows you to use popups,windows and buttons 
for a better interactive experience.

This project seemed easy at the begining but I did my best to fully understand every thing I type in my code so I can benefit from it as much as possible . I faced some
difficulties concerning the overflow of my algorithm caused by the huge numbers of my dataset that made me discover the normalization and standardization and its different types.

At the end I decided to write different verions of my program by applying the different solutions that I found after reading various articles, watching videos and of course
surfing on the stackoverflow website.

Last but not least, I really thank my team mate Marouane SAKAI with whom I worked on this project as well as my supervisor Noureddine Hamid and Nouredine Ouhaddou that helped and guided me in this journey.

                                                                      About the programs

Language: Python

Libraries: Matplotlib, Numpy, Pandas, Tkinter, Pickle

Structure: Two programs and a text file. The first program contains the gradient descent algorithm that finds the slope and the intercept of my linear function. At the end the 
program saves the two variables in the text file that can be used later to estimate new prices. The second program is for estimating, it contains the tkinter program that displays the window where you're supposed to enter the mileage of the car and then click to find the estimated price.

- linear_regression.py :
Ran in terminal/command line using this format:  ** python linear_regression.py [Location of the .xlsx dataset] [Type of normalization: "Normalized" / "Not Normalized"] **
(Be sure to close the data cloud when shown so the calculations start)

-


The repository contains two versions:

- In the first one we used a normalization of the type min/max in order to visualize the data Cloud / Linear Regression but the actual slope and intercept (used for estimating) are actually calculated in a normal way using a trick we invented (at least it's working for our dataset) in order to reduce the numbers so we can avoid the overflow. However, the trick was actually to multiply by a 10^(-4)/10^(-1) and then after finding the slope/intercept multiply it by 10^(-3)/10 (This trick was actually used before discovering the normalization). The other program in the two versions is slightly similar (The one used to estimate).

- In the second one we used a normalization of the type log/exp to visualize the data cloud/ Linear regression  and to calculate the slope and the intercept that were directly used to estimate. This time the estimting program takes a mileage x but uses log(x) and then returns exp(result). So for a mileage x : **y = exp(a*log(x) + b)**
