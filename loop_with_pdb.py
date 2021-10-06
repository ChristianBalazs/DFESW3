

import pdb
pdb.set_trace()

booksVar = ['Winnie the Pooh', 'War and Peace', '1984', 'My family and other animals', 'Boy', 'The Art of War', 'Of Mice and Men', 'Peter and James']

for bookItem in booksVar:
    if bookItem == '1984':
        print(bookItem + " is the only book in the list that can be cast into a number")
    else:
        print(bookItem)

