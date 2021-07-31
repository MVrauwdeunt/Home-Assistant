secrets="/config/secrets.yaml"
user="$(grep ^kodi_user: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"
pass="$(grep ^kodi_pass: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"
ip="$(grep ^baldr_ip_address: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"

curl --user $user:$pass -H 'Content-Type: application/json' -d '{ "jsonrpc": "2.0", "method": "Player.Open", "params": { "item": { "partymode": "music" } }, "id": 1 }' 'http://'$ip':80/jsonrpc'