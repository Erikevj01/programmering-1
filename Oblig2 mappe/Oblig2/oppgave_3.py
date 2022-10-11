# Lager en liste av bøkene til Tolkien.
tolkien_books = ['The Hobbit', 'Farmer Giles of Ham', 'The Fellowship of the Ring', 'The Two Towers',
                 'The Return of the King', 'The Adventures of Tom Bombadil', 'Tree and Leaf']

# Printer ut de to første og to siste bøkene i listen.
print(f"De to første bøkene:\n{tolkien_books[0]}\n{tolkien_books[1]}\n\nDe to siste bøkene:\n{tolkien_books[5]}\n{tolkien_books[6]}")

# Legger til de to bøkene som ble utgitt etter hans død med append.
tolkien_books.append("The Silmarillion")
tolkien_books.append("Unfinished Tales")

# Endrer verdiene for de tre bøkene i Lord of the Rings trilogien.
tolkien_books[2] = "Lord of the Rings: The Fellowship of the Ring"
tolkien_books[3] = "Lord of the Rings: The Two Towers"
tolkien_books[4] = "Lord of the Rings: The Return of the King"

# Sorterer listen direkte med .sort og printer listen.
tolkien_books.sort()
print(f"\nSortert liste av Tolkien bøkene:\n{tolkien_books}")