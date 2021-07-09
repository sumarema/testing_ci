# randomizer
Printing Random Numbers 
<h2>Usage</h2>
In Linux/MacOS:
execute script:
<p>python3 randomizer.py</p>

<h3> Explanation</h3>
<p>Random numbers can be generated using multiple ways.
I have created 2 methods for this.</p>
<h4>Method 1:</h4>
<h5>Using Secrets Module:</h5>
<p>secrets.choice will basically selects randomly one element
from provided list in this case we are providing list of numbers
from 1 to 10(Avoiding 0). Secrets will be helpful if we are going
to use the lib for any security related stuff</p>
<h4>Method 2:</h4>
<h5>Using Random Module:</h5>
<p>random.randrange will also do the same thing. It selects a
number from specified list.</p>