# Imperialism remake
# Copyright (C) 2014 Trilarion
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import glob, os
from PySide import QtCore, QtGui
from client import audio

if __name__ == '__main__':
    app = QtGui.QApplication([])

    window = QtGui.QWidget()
    window.show()

    search_mask = os.path.join('artwork', 'music', 'soundtrack', '*.ogg')
    soundtrack_files = glob.glob(search_mask)
    print(soundtrack_files)

    player = audio.Player()
    player.set_song_list(soundtrack_files)
    player.start()
    player.title_changed.connect(print)

    app.exec_()
