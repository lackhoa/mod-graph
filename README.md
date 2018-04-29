# mod-graph
Creating graphs to do modulo calculation using graphviz and python

What you must have:
- python3
- graphviz
- Modify the external commands to suit your OS (default is Linux)

How to use the program:
- Modify the NUM constant to change the base
- Run the main.py using python3
- View the "mod_<base>.pdf" file

How to use the graph:
suppose you want to find (x mod 11):
- Initially, put your finger at vertex labeled "0"
- For each digit d in x:
    + Trace along one yellow arrow
    + Trace along d blue arrows
    + The label of the final vertex your finger is on is the answer.

Examples: view the files mod_11.pdf and other pdf files
