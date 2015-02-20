def title_compare(stringA, stringB):
'''
Compares two strings (like titles or sentences) and returns a weight (integer), 0-99, indicative of how similar 
or not the two strings are. The weighting is, clearly, weighted, so if one string is short and is found in the other,
the weight can be high. For example, 'My Title' and 'My Second Title' would return a large value, but 
'My Title: Not Too Long Subtitle' and 'My Title: This Is The Other Part Here About This New One' would not. 
That is, the checker does not get much in the way of context for the strings, that's up to you. 
Will not be accurate with strings of only words in the drop_words list (returns 0).
Along the way it converts the strings to lists and then sets (to get rid of duplicate words).
Originally used to compare Kickstarter project titles, so it runs fine on relatively short strings. May do poorly
on long strings (that is, may be slow). 
Originally run within a double loop, somewhat like 'for i in xrange(0, len(data)-1)' and then next
'for j in xrange(i+1, len(data))'. Then I compared data[i]['string_X'] against data[j]['string_X'] in order to
compare across string_X in the data (from a CSV originally).
Note if you are doing a comparision where there might be multiple matches, you might want to have a temporary
max value catcher for the returned weight, and then use the highest one (or some other comletely different thing).
Requires regex (import re).
Input:  Two string-type objects.
Output: One integer-type object, range 0-99.
Python 2.7, coded and run originally on OSX. Not tested on other platforms.
YMMV.
Originally by Nathaniel Poor, Feb 2015.'''

	# regex variable.
	drop_chars = re.compile('[\W_]+', re.UNICODE) # \W is non-alphanumeric but not _ so also _, c/o Stackoverflow: 
		# http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python

	# List of common words to drop.
	# If the two strings are ONLY these words, the compare returns zero which is not accurate.
	drop_words = ('the', 'of', 'and', 'or', 'a', '') # Catches if some have an empty entry in the list.

	# Make them both lower case.
	stringA = stringA.lower()
	stringB = stringB.lower()

	# Drop non-alphanumerics like - : , . ! / ? etc., with the regex.
	# This can leave 's' from apostrophe s, etc. That may or may not be what you want.
	stringA = drop_chars.sub(' ', stringA)
	stringB = drop_chars.sub(' ', stringB)

	# Break the now-cleaned strings into lists, using the space character as the splitting point.
	listA = stringA.split(' ')
	listB = stringB.split(' ')

	# Drop the 'drop words' from the lists.
	listA = [x for x in listA if x not in drop_words] # This is a great little Python approach.
	listB = [x for x in listB if x not in drop_words]

	# Make each unique, duplicates cause issues with counting.
	listA = set(listA) # Yes these are now sets, not lists.
	listB = set(listB) 

	# Do checking here, first directly compare, then compare individual words.
	if listA == listB:
		weight = 99 # Because you can't be 100% sure! (That is, some elements were cleaned out.)
	else:
		weightA = 0
		for wordA in listA:
			for wordB in listB:
				if wordA == wordB:
					weightA += 1
		if len(listA) != 0: # Check if a string is only the common removed words (like conjunctions).
			weightA = (float(weightA) / len(listA)) * 99
		else:
			return 0
		weightB = 0
		for wordB in listB:
			for wordA in listA:
				if wordB == wordA:
					weightB += 1
		if len(listB) != 0: # Check if a string is only the common removed words (like conjunctions).
			weightB = (float(weightB) / len(listB)) * 99
		else:
			return 0
		weight  = int(float(weightA + weightB) / 2)

#	print 'Weight is:', weight # If you want to see the weight while here.
	return weight
# End title_compare

