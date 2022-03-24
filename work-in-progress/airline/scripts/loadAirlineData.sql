## creates schema for Airline (Flight Delay / On-time Performance) and loads sample data
##
## NOTE: script will DROP existing tables before creating new ones
##
## NOTE2: loading data from local csv is turned OFF by defult on mysql on mac
##
##   server side
##      SHOW GLOBAL VARIABLES LIKE 'local_infile';
##      SET GLOBAL local_infile=1;
##   client side
##      mysql --local-infile=1
##

USE airline;

## Load from csv
LOAD DATA LOCAL INFILE './airline/data/L_AIRLINE_ID.csv' INTO TABLE L_AIRLINE_ID FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (Code,Description);
LOAD DATA LOCAL INFILE './airline/data/L_AIRPORT.csv' INTO TABLE L_AIRPORT FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (Code,Description);
LOAD DATA LOCAL INFILE './airline/data/L_AIRPORT_ID.csv' INTO TABLE L_AIRPORT_ID FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (Code,Description);
LOAD DATA LOCAL INFILE './airline/data/On_Time_On_Time_Performance_2016_1.sample.csv' INTO TABLE On_Time_On_Time_Performance_2016_1 FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' IGNORE 1 ROWS (Year,Quarter,Month,DayofMonth,DayOfWeek,FlightDate,UniqueCarrier,AirlineID,Carrier,TailNum,FlightNum,OriginAirportID,OriginAirportSeqID,OriginCityMarketID,Origin,OriginCityName,OriginState,OriginStateFips,OriginStateName,OriginWac,DestAirportID,DestAirportSeqID,DestCityMarketID,Dest,DestCityName,DestState,DestStateFips,DestStateName,DestWac,CRSDepTime,DepTime,DepDelay,DepDelayMinutes,DepDel15,DepartureDelayGroups,DepTimeBlk,TaxiOut,WheelsOff,WheelsOn,TaxiIn,CRSArrTime,ArrTime,ArrDelay,ArrDelayMinutes,ArrDel15,ArrivalDelayGroups,ArrTimeBlk,Cancelled,CancellationCode,Diverted,CRSElapsedTime,ActualElapsedTime,AirTime,Flights,Distance,DistanceGroup,CarrierDelay,WeatherDelay,NASDelay,SecurityDelay,LateAircraftDelay,FirstDepTime,TotalAddGTime,LongestAddGTime,DivAirportLandings,DivReachedDest,DivActualElapsedTime,DivArrDelay,DivDistance,Div1Airport,Div1AirportID,Div1AirportSeqID,Div1WheelsOn,Div1TotalGTime,Div1LongestGTime,Div1WheelsOff,Div1TailNum,Div2Airport,Div2AirportID,Div2AirportSeqID,Div2WheelsOn,Div2TotalGTime,Div2LongestGTime);

