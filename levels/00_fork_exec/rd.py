#!/usr/bin/env python2.7
#
# Docker From Scratch Workshop
# Level 0 - starting a new process (no containment)
#
# Goal: We want our code to start a new linux process using the fork & exec model
#       i.e. running:
#                rd.py run /bin/sh
#            will fork a new process which will exec '/bin/sh', while the parent waits for it to finish.
#

from __future__ import print_function

import click
import os
import traceback


@click.group()
def cli():
    pass


def contain(command):
    # TODO: exec command, note the difference between the exec flavours
    #       https://docs.python.org/2/library/os.html#os.execv
    # NOTE: command is an array (first element is path/file, and the entire array is exec's args)

    os._exit(0)  # TODO: remove this after adding exec


@cli.command()
@click.argument('Command', required=True, nargs=-1)
def run(command):
    pid = 0  # TODO: replace this with fork() https://docs.python.org/2/library/os.html#os.fork
    if pid == 0:
        # This is the child, we'll try to do some containment here
        try:
            contain(command)
        except Exception:
            traceback.print_exc()
            os._exit(1)  # something went wrong in contain()

    # This is the parent, pid contains the PID of the forked process
    _, status = os.waitpid(pid, 0)  # wait for the forked child, fetch the exit status
    print('{} exited with status {}'.format(pid, status))


if __name__ == '__main__':
    cli()
