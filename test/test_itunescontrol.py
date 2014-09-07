# coding:utf-8

import unittest
import itunesremote.itunescontrol

class test_itunescontrol(unittest.TestCase):

    def setUp(self):
        self.controlitunes = itunesremote.itunescontrol.controlitunes()
        self.controlitunes.play()

    def test_albuminfo(self):
        print('albuminfo')
        print(self.controlitunes.albuminfo())

    def test_artistinfo(self):
        print('artistinfo')
        print(self.controlitunes.artistinfo())

    def test_trackinfo(self):
        print('trackinfo')
        print(self.controlitunes.trackinfo())

    def test_pause(self):
        print('pause')
        self.controlitunes.pause()
        self.assertEqual(self.controlitunes.status(), "stopped")

    def test_play(self):
        print('play')
        self.controlitunes.play()
        self.assertEqual(self.controlitunes.status(), "playing")

    def test_volume(self):
        print('volume')
        self.controlitunes.volume(30)
        self.controlitunes.volume(50)
        self.controlitunes.volume(100)

    def test_next(self):
        print('next track')
        self.controlitunes.nexttrack()

    def test_prev(self):
        print('prev track')
        self.controlitunes.prevtrack()

    def test_stop(self):
        print('stop')
        self.controlitunes.stop()

if __name__ == '__main__':
    unittest.main()
