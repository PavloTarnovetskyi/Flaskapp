#!/bin/bash
Public_IP=`terraform output public_ip | sed 's/.\\(.*\\)/\\1/' | sed 's/\\(.*\\)./\\1/'`
echo $Public_IP
sed -i -e "s/'\\(.*\\):9100'/'$Public_IP:9100'/g" /usr/local/etc/prometheus.yml
brew services restart prometheus