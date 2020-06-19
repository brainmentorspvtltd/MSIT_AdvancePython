
>> > def1 = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
>> > def2 = "Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under the GNU General Public License (GPL). This tutorial gives enough understanding on Python programming language."
>> > words1 = def1.split()
>> > words2 = def2.split()
>> > words1
['Python', 'is', 'an', 'interpreted,', 'high-level,', 'general-purpose', 'programming', 'language.', 'Created', 'by', 'Guido', 'van', 'Rossum', 'and', 'first', 'released', 'in', '1991,', "Python's", 'design', 'philosophy', 'emphasizes', 'code', 'readability',
    'with', 'its', 'notable', 'use', 'of', 'significant', 'whitespace.', 'Its', 'language', 'constructs', 'and', 'object-oriented', 'approach', 'aim', 'to', 'help', 'programmers', 'write', 'clear,', 'logical', 'code', 'for', 'small', 'and', 'large-scale', 'projects.']
>> > words2
['Python', 'is', 'a', 'general-purpose', 'interpreted,', 'interactive,', 'object-oriented,', 'and', 'high-level', 'programming', 'language.', 'It', 'was', 'created', 'by', 'Guido', 'van', 'Rossum', 'during', '1985-', '1990.', 'Like',
    'Perl,', 'Python', 'source', 'code', 'is', 'also', 'available', 'under', 'the', 'GNU', 'General', 'Public', 'License', '(GPL).', 'This', 'tutorial', 'gives', 'enough', 'understanding', 'on', 'Python', 'programming', 'language.']
>> > set1 = set(words1)
>> > set2 = set(words2)
>> > intersection = set1.intersection(set2)
>> > union = set1.union(set2)
>> > intersection
{'and', 'code', 'van', 'by', 'Python', 'is', 'programming', 'Rossum',
    'general-purpose', 'language.', 'interpreted,', 'Guido'}
>> > union
{'use', 'Rossum', 'object-oriented,', 'for', 'aim', 'logical', 'object-oriented', 'under', 'This', '1991,', 'design', 'clear,', 'approach', 'programming', 'with', 'programmers', 'interpreted,', 'of', 'significant', 'available', 'help', 'code', 'constructs', 'small', 'whitespace.', 'in', 'Guido', 'GNU', 'Perl,', 'Like', 'projects.', 'Public', 'released', 'language', 'by', 'a', 'van', 'its',
    'on', 'notable', 'readability', 'created', 'General', 'emphasizes', 'was', 'Its', 'the', 'an', 'gives', 'first', 'enough', 'It', '(GPL).', "Python's", 'language.', 'source', 'and', 'interactive,', 'tutorial', 'also', 'large-scale', 'high-level,', 'philosophy', 'high-level', '1990.', 'Python', 'Created', 'write', 'understanding', 'to', 'is', 'general-purpose', '1985-', 'during', 'License'}
>> > len(intersection)
12
>> > len(union)
75
>> > len(intersection) / len(union) * 100
16.0
>> >  # stopwords
...
>> >
>> > search = "nova sandwich maker"
>> > product_name = "" >> >
>> >
>> >
>> > product_name = "Nova 2 SLICE SANDWICH MAKER Grill  (Black & Steel)"
>> > words1 = search.split()
>> > words2 = pro
product_name property(
>> > words2=pro
product_name property(
>> > words2=product_name.split()
>> > set1=set(words1)
>> > set2=set(words2)
>> > set1
{'maker', 'nova', 'sandwich'}
>> > set2
{'(Black', 'SLICE', 'SANDWICH', 'Steel)', 'Grill', '2', '&', 'MAKER', 'Nova'}
>> > words2=product_name.lower().split()
>> > set2=set(words)
Traceback(most recent call last):
  File "<stdin>", line 1, in < module >
NameError: name 'words' is not defined
>> > set2=set(words2)
>> > set2
{'maker', 'sandwich', '2', 'grill', '(black', '&', 'nova', 'steel)', 'slice'}
>> > union=set1.union(set2)
>> > intersection=set1.intersection(set2)
>> > len(intersection) / len(union) * 100
33.33333333333333
>> > new_search_term="window air conditioner"
>> > words3=new_search_term.split()
>> > set3=set(words3)
>> > set3
{'conditioner', 'window', 'air'}
>> > union=set3.union(set2)
>> > intersection=set3.intersection(set2)
>> > len(intersection) / len(union) * 100
0.0
