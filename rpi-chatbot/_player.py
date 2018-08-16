import subprocess as sp
from _logging import logger

class _Player:
    cmd_for_mp3 = 'mpg123-pulse -q -'
    cmd_for_wav = 'aplay -q -'
    cmd_kill_pulseaudio = 'pulseaudio --kill'

    def play_bytes(self, fd, _format='mp3', kill=True):
        if _format == 'mp3':
            cmd = self.cmd_for_mp3
        elif _format == 'wav':
            cmd = self.cmd_for_wav
        else:
            raise AssertionError('Only support mp3 or wav format.')

        process = sp.Popen(cmd.split(' '), stdin=fd, stdout=sp.PIPE)
        retcode = process.wait()
        if retcode:
            logger.error('%s failed with %d', cmd[0], retcode)

        if kill:
            p = sp.Popen(self.cmd_kill_pulseaudio.split(' '))
            p.wait()

simple_player = _Player()
