#!/bin/sh
# Init script for logstash
# Maintained by Elasticsearch
# Generated by pleaserun.
# Implemented based on LSB Core 3.1:
#   * Sections: 20.2, 20.3
#
### BEGIN INIT INFO
# Provides:          logstash
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description:
# Description:        Starts Logstash as a daemon.
### END INIT INFO

# Source function library.
. /etc/rc.d/init.d/functions

name=logstash
pidfile="/var/run/$name/$name.pid"

LS_USER=logstash
LS_HOME=/var/lib/logstash
LS_HEAP_SIZE="500m"
LS_JAVA_OPTS="-Djava.io.tmpdir=/tmp"
LS_LOG_DIR=/var/log/logstash
LS_LOG_FILE="${LS_LOG_DIR}/$name.log"
LS_CONF_DIR=/etc/logstash/
LS_OPEN_FILES=16384
LS_OPTS=""

[ -r /etc/sysconfig/$name ] && . /etc/sysconfig/$name

program="/usr/local/$name/bin/$name"
args="agent -f ${LS_CONF_DIR} -l ${LS_LOG_FILE} ${LS_OPTS}"

start() {

    if rh_status >/dev/null 2>&1 ; then
        return 0
    fi

    echo -n $"Starting $name: "
    JAVA_OPTS=${LS_JAVA_OPTS}
    HOME=${LS_HOME}
    export HOME JAVA_OPTS LS_HEAP_SIZE LS_JAVA_OPTS LS_USE_GC_LOGGING
    ulimit -n ${LS_OPEN_FILES}

    daemon --pidfile=${pidfile} --user $LS_USER "$program $args >> ${LS_LOG_FILE} 2>&1 &"

    retval=$?
    usleep 500000
    pid=`ps axo pid,command | grep -v "grep" | grep "logstash/runner.rb agent" | awk '{print $1}'`
    if [ -n "$pid" ]; then
        echo $pid > "$pidfile"
    fi
    echo
    return $retval
}

stop() {
    echo -n $"Stopping $name: "
    killproc -p $pidfile $name
    retval=$?
    echo
    [ $retval -eq 0 ] && rm -f $pidfile
    return $retval
}

rh_status() {
    status -p $pidfile $name
}

case "$1" in
    start)
        $1
        ;;
    stop)
        $1
        ;;
    status)
        rh_status
        ;;
    restart)
        stop
        start
        ;;
    *)
        echo "Usage: $0 {start|stop|status|restart}" >&2
        exit 3
    ;;
esac

exit $?
