#!/bin/bash

if [ -z "$1" ] ; then
  echo 'Project name is empty'
  exit 1
fi

PROJECT_NAME="$1"
SCALA_VERSION="${2-2.11.7}"
SCALATEST_VERSION="${3-2.2.4}"

mkdir $PROJECT_NAME
cd $PROJECT_NAME

cat > build.sbt << EOF
name := "$PROJECT_NAME"

scalaVersion := "$SCALA_VERSION"

libraryDependencies += "org.scalatest" %% "scalatest" % "$SCALATEST_VERSION" % "test"
EOF

mkdir -p src/{main/{scala,resources},test/{scala,resources}}

cat > .gitignore << EOF
target/
EOF
