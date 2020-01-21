#!/bin/bash
#
# Copyright (c) 2014 RONDHUIT Co.,Ltd.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

RHCOM_JAR=$(ls lib/RONDHUIT-COMMONS-*.jar)
SLF4J_JAR=$(ls lib/slf4j-api-*.jar)
SLF4J_JAR=${SLF4J_JAR}:$(ls lib/slf4j-jdk14-*.jar)

VECTOR_FILE=vectors.txt
while getopts f: OPT
do
  case $OPT in
    "f" ) VECTOR_FILE="$OPTARG" ;;
  esac
done

java -cp ${RHCOM_JAR}:${SLF4J_JAR}:classes com.rondhuit.w2v.demo.Distance ${VECTOR_FILE}
