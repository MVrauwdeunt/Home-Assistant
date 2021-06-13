secrets="../secrets.yaml"
user="$(grep ^kodi_user: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"
pass="$(grep ^kodi_pass: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"
ip="$(grep ^baldr_ip_address: $secrets | sed 's/^[^:]*: //' | sed 's/ //g')"

curl --user $user:$pass --header 'Content-Type: application/json' --data-binary '{"jsonrpc": "2.0", "method": "Player.Stop", "params": { "playerid": 0 }, "id": 1}' 'http://'$ip':80/jsonrpc'