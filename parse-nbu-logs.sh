#!/usr/bin/bash

## Get Yesterday
yesterday="$(/opt/sfw/bin/date -d 'yesterday' +%m%d%y)"


##create log.date file to grep
logfile="/opt/openv/netbackup/logs/bpbrm/log.$yesterday"

## need Errno = 2 or Errno = 5

function geterrors(){
        for i in 2 5
        do
        grep -i Errno\ =\ `echo $i` $logfile \
        | grep -i 'keyword0*'\
        | sed -e 's/sparse file //g' -e 's/file //g' \
        | cut -d " " -f8,13,14,15,16 \
        | sort -d
        done

        ## need to get Files that are skipped
        grep -i 'TRV' $logfile | grep -i 'keyword' | cut -d " " -f8,14-20
}

errorlog="/opt/openv/CO_logs/log.$yesterday"

## Out Files to CO_logs directory
geterrors > /opt/openv/CO_logs/log.$yesterday

cat $errorlog | mailx -s "Errno = 2|5: NBU" bmorrison@tld.edu 
