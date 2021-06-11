# Compress-String

>11 June 2021 03:48 PM

This question was a difficult for me to wrap my head around. 😅

***Question: Given a string lowercase alphabet s, eliminate consecutive duplicate characters from the string and return it.***

I think how it works is by pushing all the repeated letters to the end of a list and then printing out the list only till where the pointer has stopped. It's still a little confusing to me so I've been printing it at different places and seeing how it's working. 

Another solution I really liked and thought was easier to understand was one where you create a new list with the first letter of the string in the list. Then you iterate from the second letter onwards and if the last value in the list is the same as the iterated alphabet then you continue with the loop or else you append it the resulting list. I'll add creds to that code.
