##Overview

Welcome aboard. The goal of this package is to quantitatively evaluate the
 similarity between two blocks of text using only standard python
  packages. Once I came to terms with the fact that Levenshtein 
  distance and other such well-tested algorithms were out of reach 
  for a homebaked package, I turned towards an ensemble modelling 
  approach. Ie, that similarity is a combination of factors. The 
  two components that made it into my final product were set 
  similarity and subset similarities. The former refers to how much 
  the set of distinct 'words' contained in the text overlaps with 
  the corresponding set of the second text. The latter studies how 
  many strings of words > 1 word long are identical in both blocks.
  
  In conclusion, we've got a symmetric text comparing tool. From my 
  experimention, scores about ~0.7 are strong similarities. The scores 
  also scale more rapidly at lower text lengths (harsher penalties on 
  mismatches).
  

##How to Get Started
#Browser Test
#URL Request
```python
import requests

text1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
text2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."

r = requests.post('http://127.0.0.1:5000/', data={'text1':text1, 'text2':text2})

print(r.text)
```
##Assumptions
The prompt has a clear focus on **words** so I've removed some common 
puncuation though this could be expanded. I've also made the bold 
assumption that any space is a single space. Lastly, typos constitute 
a different word. There is no inference to the user's intent.
##Known Bugs
There is no handling present for multiple consecutive spaces.

##Next Steps
The first opportunity for improvement would we weight tuning in two places. 
In the subset similarity evaluation, common strings of differing 
length carry the same value (line 60 in stringscore.py). One *might* 
want to assign higher value to larger string similarities. An immediate 
issue that will arise with this is how that value scales when the 
two texts vary in size dramatically. This may pose a symmetry problem.
 The second weighting opportunity is the final ensemble evaluation 
 (line 105 in stringscore.py) that was initially decided off of my 
 own intuition but should be further tuned. Another test can also be 
 added where common words are removed and only words of *value* 
 are compared between the two blocks.
