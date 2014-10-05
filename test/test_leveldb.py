
# coding:utf-8

import unittest
import itunesremote.leveldb
import itunesremote.itunescontrol

class test_leveldb(unittest.TestCase):
    def setUp(self):
        itunesremote.leveldb.plyvel.destroy_db('testdb')
        self.db = itunesremote.leveldb.DataBase()
        self.itunes = itunesremote.itunescontrol.controlitunes()
    def test_dbtest(self):
        self.db.writemusic(osaobject=self.itunes, debug=True)
        print(self.db.readmusic())
unittest.main()
