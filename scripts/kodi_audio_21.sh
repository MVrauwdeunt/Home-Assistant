secrets="../secrets.yaml"
user="$(grep ^kodi_user: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"
pass="$(grep ^kodi_pass: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"
ip="$(grep ^baldr_ip_address: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"

curl --user $user:$pass -v -H "Content-type: application/json" -X POST -d '{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"audiooutput.audiodevice","value":"surround21:CARD=Device,DEV=0"},"id":1}' http://$ip:80/jsonrpc