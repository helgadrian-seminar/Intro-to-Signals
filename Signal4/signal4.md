# Signal 4

This signal is composed of meta data for the first 30 lines which are not required for this demo. 
You will therefore need to ignore these when reading the data in. 
The remaining lines have 5 columns but these do not represent seperate fields they are all the same signal. 
The values of the signal go from left to right, up to down. 
So you will need to read lines individually and add each value of the line to the same list then concatonate all 
the lists together into the full signal.
I suggest using Python's default open statement for this perhaps using a with statement and a for loop for economy.
If you don't know what those are ask.

The time step for this data is a uniform 20 Hz so you can translate the array indecies into values of time and 
if you wish determine the nyquest frequency to plot the fourier domain.
