import unittest

from pypika.queries import Query, Table


class CommentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.table_abc = Table("abc")

    def test_delete_with_query_comment(self):
        q = Query.from_(self.table_abc).delete().comment("Deleting all rows from abc table")
        self.assertEqual('-- Deleting all rows from abc table\nDELETE FROM "abc"', str(q))

    def test_delete_with_table_comment(self):
        q = Query.from_(self.table_abc.comment("Base abc table")).delete()
        self.assertEqual('DELETE FROM -- Base abc table\n"abc"', str(q))

    def test_delete_with_query_and_table_comment(self):
        q = (
            Query.from_(self.table_abc.comment("abc main table"))
            .delete()
            .comment("High level delete query")
        )
        self.assertEqual(
            '-- High level delete query\nDELETE FROM -- abc main table\n"abc"',
            str(q)
        )