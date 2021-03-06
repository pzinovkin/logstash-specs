###############################
# Default settings for logstash
###############################

# Override Java location
#JAVACMD=/usr/bin/java

# Set a home directory
#LS_HOME=/usr/local/logstash

# Arguments to pass to java
#LS_HEAP_SIZE="256m"
#LS_JAVA_OPTS="-Djava.io.tmpdir=$HOME"

# Logstash filter worker threads
#LS_WORKER_THREADS=1

# pidfiles aren't used for upstart; this is for sysv users.
#LS_PIDFILE=/var/run/logstash/logstash.pid

# user id to be invoked as; for upstart: edit /etc/init/logstash.conf
#LS_USER=logstash

# logstash logging
#LS_LOG_FILE=/var/log/logstash/logstash.log
#LS_USE_GC_LOGGING="true"

# logstash configuration directory
#LS_CONF_DIR=/etc/logstash/

# Open file limit; cannot be overridden in upstart
#LS_OPEN_FILES=2048
