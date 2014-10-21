# coding:utf-8
from subprocess import Popen, PIPE
import os


class controlitunes(object):
    musicname = 'Nue'

    def get_playlist(self):
        artistnames = []
        albumnames = []
        musicfiles = []
        idnumber = []
        num = 0
        for root, dirname, filename in os.walk('/Users/hayasakaryosuke/Music/iTunes/iTunes Media/Music'):
            if len(filename) > 0:
                if filename[0] != '.DS_Store':
                    idnumber.append(str(num))
                    artistnames.append(root.split('/')[-2])
                    albumnames.append(root.split('/')[-1])
                    musicfiles.append(filename)
                    num += 1
        return idnumber, artistnames, albumnames, musicfiles

    def _itunesctrl(self, cmd):
        if hasattr(cmd, "encode"):
            cmd = cmd.encode("utf-8")
        osa = Popen(["osascript", "-"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        res, err = osa.communicate(cmd)
        if err:
            raise Exception(err)
        return res.decode("utf-8")

    def albuminfo(self):
        return self._itunesctrl('tell application "iTunes" to album of current track as string')

    def mute(self):
        return self._itunesctrl('tell application "iTunes" to set mute to true')

    def unmute(self):
        return self._itunesctrl('tell application "iTunes" to set mute to false')

    def artistinfo(self):
        data = self._itunesctrl('tell application "iTunes" to artist of current track as string')
        return data

    def trackinfo(self):
        return self._itunesctrl('tell application "iTunes" to name of current track as string')

    def status(self):
        return self._itunesctrl('tell application "iTunes" to player state as string').split()[0]

    def play(self, musicname=None):
        return self._itunesctrl('tell application "iTunes" to play track "' + str(self.musicname) + '"')

    def positionlengthinfo(self):
        return self._itunesctrl('tell application "iTunes" to time of current track')

    def positioninfo(self):
        return self._itunesctrl('tell application "itunes" to player position')

    def pause(self):
        return self._itunesctrl('tell application "iTunes" to pause')

    def stop(self):
        return self._itunesctrl('tell application "iTunes" to stop')

    def nexttrack(self):
        return self._itunesctrl('tell application "iTunes" to next track')

    def prevtrack(self):
        return self._itunesctrl('tell application "iTunes" to previous track')

    def volume(self, value):
        return self._itunesctrl('tell application "iTunes" to set sound volume to '+str(value))

    def playlist_album(self, debug=False):
        if debug is False:
            return self._itunesctrl('tell application "iTunes" to (get album of every track in playlist "ミュージック")').split(',')
        else:
            return self._itunesctrl('tell application "iTunes" to (get album of every track in playlist "test")').split(',')

    def playlist_name(self, debug=False):
        if debug is False:
            return self._itunesctrl('tell application "iTunes" to (get name of every track in playlist "ミュージック")').split(',')
        else:
            return self._itunesctrl('tell application "iTunes" to (get name of every track in playlist "test")').split(',')

    def playlist_id(self, debug=False):
        if debug is False:
            return list(map(str, self._itunesctrl('tell application "iTunes" to (get id of every track in playlist "ミュージック")').split(',')))
        else:
            return list(map(str, self._itunesctrl('tell application "iTunes" to (get id of every track in playlist "test")').split(',')))

    def playlist_artist(self, debug=False):
        if debug is False:
            return self._itunesctrl('tell application "iTunes" to (get artist of every track in playlist "ミュージック")').split(',')
        else:
            return self._itunesctrl('tell application "iTunes" to (get artist of every track in playlist "test")').split(',')
