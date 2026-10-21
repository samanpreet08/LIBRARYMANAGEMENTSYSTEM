books = {"101":"Harrry Potter","102":"Python Book"}
def search_book(q):
    if q in books:
        return books[q]
    for id , title in books.items():
        if q.lower() in title.lower():
            return title 
        return "Book not found"

search_book("101")