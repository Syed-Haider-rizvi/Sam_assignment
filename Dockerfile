#Installing Spark Master 

FROM robertlgtucker/pyspark-java8


MAINTAINER Akash Tawade<akashtawade932@gmail.com>


RUN	mvn -version \
&& ./build/mvn -DskipTests clean package \
RUN exit

CMD ["echo","Spark pushed..."]

