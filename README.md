# How to Install
Copy folder into prefered directory on your machine

## How to Use
1. Navigate to project directory in terminal/command-prompt
2. Run `python app.py` 
3. Follow onscreen instructions

## Test
1. Open terminal/command-prompt and navigate to project directory
2. Run `pip install pytest` to install the pytest python module
3. Run `pytest` to run the test suite

# Design Considerations for line.py
Input:
For the input I quickly found that floats made the design more difficult as converting floats to the python "Fractions" has challenges. Particularly around certain float values that don't repeat in base 10 but do in base 2 (such as 1/10 = 0.1). The Fraction.limit_denominator() helped approximate floats but there still is some information loss which results in some inaccurate results.

I could have restricted the input to just ints but I felt this limited the user. Results from bad floats (such as 0.1) were still close so as long as the user knew this could happen the function still works fine for most other floats.

Output:
While searching for the standard form definition some resources said that A and B must be non-zero. This would mean that vertical and horizontal lines aren't valid lines for standard form. I chose not to implement this as its not very intuitive while returning zero values for A or B and C (e.g. 8x + 0y = 0 >> 8x = 0) felt like it would make sense to the user. 

For choosing output I reasoned around three options:
1. String: simply a string of the form => "Ax+By=C"
2. Tuple: containing three values for A, B and C => (A,B,C)
3. Object: object that has variables A, B and C as well as extra functionality such as print string which would print the string representation

-The string is great for visualization but bad to work with if you need the A, B and C values.

-Tuple is better to work with but not as great for visualization.

-Object has the benefits of both the string option and the tuple option but requires the user to have knowledge on how to use it and what functionality it has.

I chose tuple as its the most useable, printing it in string form is quite easy (e.g. print(str(A)+"x + "+str(B)+"y = "+str(C)) ) and it doesn't need any knowledge to how a standard line object works. Also it's a lot less bloat for the object which would improve performance and memory usage. 
