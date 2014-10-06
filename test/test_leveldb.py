
# coding:utf-8

import unittest
import itunesremote.leveldb
import itunesremote.itunescontrol

class test_leveldb(unittest.TestCase):
    def setUp(self):
        itunesremote.leveldb.plyvel.destroy_db('testdb')
        self.db = itunesremote.leveldb.DataBase(dbname='testdb')
        self.itunes = itunesremote.itunescontrol.controlitunes()
    def test_dbtest(self):
        self.db.writemusic(osaobject=self.itunes, debug=True)
        keys, vals = self.db.readmusic()
        print(vals[14])
        #for val in vals:
        #    print(val['musicname'])
unittest.main()
