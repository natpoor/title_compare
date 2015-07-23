# title_compare
Simplified bag of words, compares two titles (string types), returns a rough measure of similarity (0-99).

Python 2.7

Compares two strings (like titles or sentences) and returns a weight (integer), 0-99, indicative of how similar or not the two strings are. The weighting is, clearly, weighted, so if one string is short and is found in the other, the weight can be high. For example, 'My Title' and 'My Second Title' would return a large value, but 'My Title: Not Too Long Subtitle' and 'My Title: This Is The Other Part Here About This New One' would not. That is, the checker does not get much in the way of context for the strings, that's up to you. 

Will not be accurate with strings of only words in the drop_words list (returns 0).

Along the way it converts the strings to lists and then sets (to get rid of duplicate words).

Originally used to compare Kickstarter project titles, so it runs fine on relatively short strings. May do poorly on long strings (that is, may be slow). 

Originally run within a double loop, somewhat like 'for i in xrange(0, len(data)-1)' and then next 'for j in xrange(i+1, len(data))'. Then I compared data[i]['string_X'] against data[j]['string_X'] in order to compare across string_X in the data (from a CSV originally).

Note if you are doing a comparision where there might be multiple matches, you might want to have a temporary max value catcher for the returned weight, and then use the highest one (or some other comletely different thing).

Requires regex (import re).

Input:   Two string-type objects.

Returns: One integer-type object, range 0-99.

For Python 2.7, coded and run originally on OSX 10.10. Not tested on other platforms but isn't too fancy.

YMMV.
