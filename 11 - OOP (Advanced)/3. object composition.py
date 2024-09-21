# Object composition is a class containing objects of other classes to reuse their functionality.
# It is used to build complex systems.

class Book:
    def __init__(self, book_id, name, author):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        return repr((self.book_id, self.name, self.author, self.reviews))

    def add_review(self, review_id, description, rating):
        self.reviews.append(Review(review_id, description, rating))


class Review:
    def __init__(self, review_id, description, rating):
        self.review_id = review_id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.review_id, self.description, self.rating))


Harry = Book(123, 'Harry Potter', 'J. K. Rowling')
print(Harry)

Harry.add_review(10, 'Great Book', 4)
Harry.add_review(101, 'Awesome', 5)
print(Harry)
