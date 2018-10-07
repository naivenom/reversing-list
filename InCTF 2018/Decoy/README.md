# Write up
We open the binary with IDA and we realize that the binary get a input from stdin. Also the input flag needs a 44 lenght value so we start with something like that <code>aaaaaaaaaaabbbbbbbbbbbcccccccccccddddddddddd</code>. We set a breakpoint here <code>0040341F</code> and path this instruction with <code>jnz</code>.<br>
After the <code>fgets</code> function call we enter an important function.
## sub_4018D9

