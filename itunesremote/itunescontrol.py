# coding:utf-8
from subprocess import Popen, PIPE
import os

class controlitunes(object):

    def _itunesctrl(self, cmd):
        
        if hasattr(cmd, "encode"):
            cmd = cmd.encode("utf-8")
        
        osa = Popen(["osascript", "-"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        res, err = osa.communicate(script)
        
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
        return self._itunesctrl('tell application "iTunes" to artist of current track as string')

    def trackinfo(self):
        return self._itunesctrl('tell application "iTunes" to name of current track as string')

    def status(self):
        return self._itunesctrl('tell application "iTunes" to player state as string').split()[0]

    def play(self, name=None):
        return self._itunesctrl('tell application "iTunes" to play')

    def positionlengthinfo(self):
        return self._itunesctrl('tell application "iTunes" set hoge to time of current track')

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

    def playlist(self):
        pass

