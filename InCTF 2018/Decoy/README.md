# Write-up - Decoy
We open the binary with IDA and we realize that the binary gets an input from stdin. Also the input password needs a 44 lenght value so we start with something like that <code>aaaaaaaaaaabbbbbbbbbbbcccccccccccddddddddddd</code>. We set a breakpoint here <code>0x0040341F</code> and patch this instruction with <code>jnz</code>.<br>
After the <code>fgets</code> function call we will analyze important functions.
## sub_4018D9
We are in this part of lenght <code>bbbbbbbbbbb</code> because of this instruction <code>movzx  eax, byte ptr [eax]</code> move <code>0x62</code> byte. 
Here <code>cmp dl, al</code> we realize that this compare with the first byte of hardcoded key <code>(mv|GLp+Gv+</code> xored, with our input byte xored two times so we need resolve this:
<pre><code>input[0] = ?
xor1 = 0xb
xor2 = 0x13
al = 0x28
</code></pre>
The first input should be <code>0x30</code> or 0 if we want that this comparation is equal to <code>al</code> register. After all iteration we will have <code>0und_Th3_n3</code> so we have currently this --> <code>aaaaaaaaaaa0und_Th3_n3cccccccccccddddddddddd</code>

## sub_401AB9
Next part we enter in this function and we realize that corresponds to the first part of the flag as it uses <code>aaaaaaaaaaa</code>. 
In this instruction <code>cmp bl, al</code> we see that this compare with the first byte of hardcoded key <code>}[2waHmrgxj</code> with our input <code>0x61</code> + two bytes, so this <code>0x63</code>. Also with + four bytes after sixth iteration. We need resolve this:
<pre><code>0x63-0x2 = 0x61 (our input)
0x7d-0x2 = 0x7b or { (correct input)
</code></pre>
We get <code>{Y0u_Finctf</code> and the correct will be <code>inctf{Y0u_F</code>. We have currently this --> <code>inctf{Y0u_F0und_Th3_n3cccccccccccddddddddddd</code><br>
In <code>sub_4018A0</code> function we enter into and we realize that there is an <code>IsDebuggerPresent</code> so we just need patch the instruction with <code>jnz</code>.

## sub_401E73
Next function we see that correspond with this part of lenght password <code>ddddddddddd</code>. 
In this code we need that <code>eax</code> register will be 0 after <code>strncmp</code> function call.
<pre><code>lea     eax, [ebp+var_2A]
mov     [esp+48h+Str2], eax ; Str2
lea     eax, [ebp+var_1F]
mov     [esp+48h+Str1], eax ; Str1
call    strncmp
mov     [ebp+var_14], eax
</code></pre>
Str1 is hardcoded string <code>{`I5z%u5dL~</code> and Str2 is our input <code>0x64</code> + one byte, so this <code>0x65</code>.
<pre><code>0x65-0x1 = 0x64 (our input)
0x7b-0x1 = 0x7a or z (correct input)
</code></pre>
The string will be <code>z_H4y$t4cK}</code>. We have currently this --> <code>inctf{Y0u_F0und_Th3_n3cccccccccccz_H4y$t4cK}</code>

## sub_4024C3
In last function we see that our input starts from the end towards the beginning so we replace this part <code>ccccccccccc</code> with <code>ABCDEFGHIJK</code>. To resolve this problem we have a key <code>7D 15 41 1E 70 39 66 55 39 5D 6E</code> and other xored value:
<pre><code>First:
0x4a+0x1 = 0x4b (our input)
0x7d-0x1 = 0x7c or | (correct input)
Second:
xor = 0x4b^0x7d                               #0x4b = input and 0x7d second value of key.
R= 0x15^0x7d = 0x68 or h (correct input)      #0x15 third value of key.
Third:
xor = 0x49^0x15                               #0x49 = input and 0x15 third value of key.
R= 0x41^0x15 = 0x54 or T (correct input)      #0x41 third value of key.
And so on...
</code></pre>
Finally we get this string value <code>3dl3_In_Th|</code> so the flag is: <code>inctf{Y0u_F0und_Th3_n33dl3_In_Th|z_H4y$t4cK}</code><br>
<b>PKTeam</b>
