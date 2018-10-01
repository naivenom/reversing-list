# TL;TR
<a href="https://atenea.ccn-cert.cni.es/challenges?category=reversing">Challenge</a><br>
We start finding interesting strings at first. After we realize that the program receive 2 arguments looking at stack memory <code>3</code>.<br>
So if we put 2 arguments jle conditional doesn’t jump. Next we need path program to <code>jnz</code> conditional. Cool, after we enter in a function that retrieve the name of our computer in memory stack <code>ebp-204h</code>.<br>
We see a loop that compare our first argument with the name of our computer if it is correct go to <code>ret</code> and continue the program, if not exit. Next we see other important function because in this, compare the second argument and do some aritmetics operations for calculate the password. So the second argument is the password to solve this baby challenge. So --> <code>crypt0.exe name_pc password</code>.<br>
When our <code>eip</code> register retrieve <code>cmp</code> instruction to compare, we realize that the value of <code>edx</code> register is 0x4e so this is the correct first byte of password and <code>ecx</code> register is just our first char of second argument.<br>
So in the second lap we see that our second argument was just “N” or 0x4e and don’t put anything more so our <code>ecx</code> register is 0x0, but <code>edx</code> register is the second byte of password great!! We win then :)<br>
<code>flag{TRY_BRO}</code>


