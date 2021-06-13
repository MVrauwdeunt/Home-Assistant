secrets="../secrets.yaml"
user="$(grep ^kodi_user: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"
pass="$(grep ^kodi_pass: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"
ip="$(grep ^baldr_ip_address: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"

curl --user $user:$pass --header 'Content-Type: application/json' --data-binary '{ "jsonrpc": "2.0", "method": "Player.Open", "params": { "item": { "partymode": "music" } }, "id": 1 }' 'http://'$ip':80/jsonrpc'