#!/bin/bash

PROD=( PROD1 PROD2 PROD3 PROD4  )
STAG=( STAGING1 STAGING2 STAGING3 STAGING4 )

## DATES
fedate=`date +%m%d%Y`
fsdate=`date +%m%d%Y --date="1 week ago"`
enddate=`date +%m/%d/%Y`
startdate=`date +%m/%d/%y --date="1 week ago"`

## RESPONSE

for i in "${PROD[@]} ${STAG[@]}"
do

    curl "http://server.domain.com/lib/page1.php?startdate=$startdate&enddate=$enddate&dataclass=SPEED&environment=$i" -o $i-response-$fsdate-$fedate.png

done

for i in "${PROD[@]}"
do
	curl "http://server.domain.com/lib/page2.php?startdate=$startdate&enddate=$enddate&dataclass=REQUESTS&environment=$i" -o $i-requests-$fsdate-$fedate.png

done

for i in "${STAG[@]}"
do
	curl curl "http://server.domain.com/lib/page3.php?startdate=$startdate&enddate=$enddate&dataclass=REQUESTS&environment=$i" -o $i-requests-$fsdate-$fedate.png

done

