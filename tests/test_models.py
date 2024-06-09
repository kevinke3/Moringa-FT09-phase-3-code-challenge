import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "Kevin")
        self.assertEqual(author.name, "Kevin")

    def test_article_creation(self):
        article = Article(1, "Flatiron", "Challenge", 1, 1)
        self.assertEqual(article.title, "Flatiron")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Null")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Null")

if __name__ == "__main__":
    unittest.main()
