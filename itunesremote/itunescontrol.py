# coding:utf-8
from subprocess import Popen PIPE
import os

class controlitunes(object):

    def itunesctrl(cmd):
        execute = Popen(["osascript", "-"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        res, err = execute.communicate(cmd)
        return res

    def play(self, name=None):
        return itunesctrl('tell application "iTunes" to play')

    def pause(self):
        return itunesctrl('tell application "iTunes" to pause')

    def stop(self):
        return itunesctrl('tell application "iTunes" to stop')

    def next(self):
        return itunesctrl('tell application "iTunes" to next track')

    def prev(self):
        return itunesctrl('tell application "iTunes" to previous track')

    def vol(self, value):
        cmd = """osascript -e 'tell application "iTunes" to set sound volume to '"""+str(value)
        return itunesctrl('tell application "iTunes" to set sound volume to '+str())
        os.system(cmd)

    def playlist(self):
        pass

