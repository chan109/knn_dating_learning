Hen use a dating app to date someone. After using it a while, she found there are three types of people: didn't like, ok charming and very charming.

She hopes have a date with someone charming.

But how?
She collects a dateset where every data point has numbers of features which are
    - frequent flight mileage obtained annually
    - percentage of time spent on playing video game
    - ice umed p-cram litres consr week.

Find a classifier to find the Hen's impression of a person.

Steps to implement the algorithm:

precessing data
1. Import data into a proper format.
2. Normalizing data into a small range.
3. Draw image to show the correlationship of the features. (making sure the features are somehow correlated)

Tagging dataset for training and testing
4.divide into two part, one for training and another one for testing.

5.Calculate each test' data distance to every training data.
6.Fine the k nearest neighbours of each test data and read-off their labels.
7.Assign the most frequently encounted label to the test data.
8. Calcuate and minimize the error rate.
