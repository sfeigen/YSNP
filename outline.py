''' 
Outline 

Twitter

Set up twitter account / dummy account to test
Get API keys and configs
Put config in .gitignore

Import Tweepy to handle the Twitter stream
On data, grab text and username
Send text to Alg.
Crunch.
On finish, reply to username with new text

Rules

str >= 50 passes, send message with text
str > 10 && str < 50 = modifier(), check()
str =< 10 fails, send message of sadness

Alg

Regex full strings and compute to rand letter
Toggle multiplier for following values:
[a-z][A-Z]   = False
[0-9]        = False
ascii.whitespace? <- find this = False
ascii.symbols? <- find this = False

Compute: len(str) * multiplier = val
(so min length is 13)
Check val: Pass, Fail, modifier()
Returns to Tweet

Modifier

Regex redundant values to amp multiplier
Add extra values only if necessary

Icebox
return correct horse battery staple

'''