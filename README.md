# Multi-Armed Bandit selection

# Description
This package is a possible implementation of the UCB1 selector. This selector can be used for Algorithm selection. 

Here it is used with random variables having different distributions and from data in a CSV file.

## Example
Here is an example of run with four random variables.

![screen](screen.png "Example using four random variables")
 
## Paper
The algorithm developed here is from:

    Auer, P., Cesa-Bianchi, N., & Fischer, P. (2002). Finite-time analysis of the multiarmed bandit problem. Machine learning, 47(2-3), 235-256.


## Prerequisites
This package needs Tkinter. Optional : Matplotlib 

## Uses
Launch the package:

    python -m Bandit


## Using your data files

In order to use your own csv file, you must format yur csv file as follow:
    
    The first line contains the names of the variable/Algorithm
    All the other lines contains the value of the variable/algorithm in the same column.

An example is provided [here](http://cop2ai.com/1.csv).

## using any kind of files

For using this code with any kind of file, you can use your own file reader and then use the MachineList class having a list of the values as argument.






