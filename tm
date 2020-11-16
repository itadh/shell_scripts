#!/bin/bash

socket_file=/var/tmux_sessions/shared_session
/bin/tmux -S $socket_file attach -t jz || (rm -f $socket_file && /bin/tmux new -s jz -S $socket_file)

