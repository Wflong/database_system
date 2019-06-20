#!/bin/sh
LANG="en_US.UTF-8"

echo "=========Installing the system...=========="

if [ ! -d "/opt/gsql" ]; then
    mkdir /opt/gsql
fi

cp -rf ../../../gsql/*      /opt/gsql/
cp -rf /opt/gsql/bin/system/gsql.sh     /usr/local/bin/
mv /usr/local/bin/gsql.sh          /usr/local/bin/gsql
chmod a+x /usr/local/bin/gsql
echo "export PATH=$PATH:/usr/local/bin/" >> /etc/profile
source /etc/profile

chmod a+wr /opt/gsql/databases
chmod a+wr /opt/gsql/config/*

echo "=========The system install succefully!===="
