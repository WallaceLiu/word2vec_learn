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

if [ -z $1 ]; then
  echo "Usage: ./demo-word2vec.sh <solrcore> -a <analyzer (default is org.apache.lucene.analysis.standard.StandardAnalyzer)> -f <vectors file (default is vectors.txt)>"
  echo "  ex) ./demo-word2vec.sh ldcc -a org.apache.lucene.analysis.ja.JapaneseAnalyzer -f vectors_ld.txt"
  exit 1
else
  SOLRCORE=$1
  shift
fi

ANALYZER=org.apache.lucene.analysis.standard.StandardAnalyzer
VECTOR_FILE=vectors.txt
while getopts a:f: OPT
do
  case $OPT in
    "a" ) ANALYZER="$OPTARG" ;;
    "f" ) VECTOR_FILE="$OPTARG" ;;
  esac
done

LUCENE_JAR=$(ls lib/lucene-core-*.jar)
LUCENE_JAR=${LUCENE_JAR}:$(ls lib/lucene-analyzers-common-*.jar)
LUCENE_JAR=${LUCENE_JAR}:$(ls lib/lucene-analyzers-kuromoji-*.jar)
RHCOM_JAR=$(ls lib/RONDHUIT-COMMONS-*.jar)
SLF4J_JAR=$(ls lib/slf4j-api-*.jar)
SLF4J_JAR=${SLF4J_JAR}:$(ls lib/slf4j-jdk14-*.jar)

java -cp ${LUCENE_JAR}:${RHCOM_JAR}:${SLF4J_JAR}:classes com.rondhuit.w2v.demo.LuceneCreateVectors -index solrhome/${SOLRCORE}/custom/index -output ${VECTOR_FILE} -field body -analyzer ${ANALYZER} -cbow 1 -size 200 -window 8 -negative 25 -sample 0.0001 -iter 15 -min-count 5
