tolkien_books = ['Farmer Giles of Ham', 'Lord of the Rings: The Fellowship of the Ring',
                 'Lord of the Rings: The Return of the King', 'Lord of the Rings: The Two Towers',
                 'The Adventures of Tom Bombadil', 'The Hobbit', 'The Silmarillion', 'Tree and Leaf',
                 'Unfinished Tales']

lotr_trilogy_books = []

# Tar inn listen fra forrige oppgave og oppretter en tom liste.

for lotr_trilogy_books in tolkien_books:
    if "Lord of the Rings:" in lotr_trilogy_books:
        print(lotr_trilogy_books)

# Benytter for løkken til å legge til alle bøkene fra LOTR trilogien inn i den tomme listen og skriver den ut.
