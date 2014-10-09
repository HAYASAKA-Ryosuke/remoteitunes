#coding: utf-8
import plyvel

class DataBase:
    import json
    
    def __init__(self, dbname=None):
        if dbname is None:
            self.leveldb = plyvel.DB('./musicdb/', create_if_missing=True)
        else:
            self.leveldb = plyvel.DB('./'+dbname+'/', create_if_missing=True)

    def _jsondump(self, iddata, albumname, artistname, musicname):
        jsondata = self.json.dumps({'iddata': iddata, 'albumname': albumname, 'artistname': artistname,'musicname': musicname})
        return jsondata.encode()

    def writemusic(self, iddata=None, musicname=None, albumname=None, artistname=None, osaobject=None, debug=False):
        if osaobject is None:
            writedata = self._jsondump(iddata=iddata, albumname=albumname, artistname=artistname, musicname=musicname) 
            self.leveldb.put(bytes(iddata), writedata)
        elif str(type(osaobject)) == str("<class 'itunesremote.itunescontrol.controlitunes'>"):
            ids, artists, albums, names = osaobject.get_playlist()
            with self.leveldb.write_batch() as wb:
                for iddata, albumname, musicname, artistname in zip(ids, albums, names, artists):
                    wb.put(iddata.encode(), self._jsondump(iddata=iddata, albumname=albumname, artistname=artistname, musicname=musicname))

    def readmusic(self, key=None):
        if key is None:
            keys=[]
            vals=[]
            for keydata, val in self.leveldb:
                keys.append(keydata)
                vals.append(self.json.loads(val.decode()))
            return keys, vals
        else:
            readdata = self.json.loads(self.leveldb.get(bytes(str(key).encode())).decode())
            return readdata

