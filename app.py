from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    player_codes = ['PQPR2GQGJ', '8V2C00VUP', '9R2VVJJP0', '8CYYRV8GR', 'RU2V8U9Q', '22YPCPUC', 'CYQ2G2J2', '2VJ0VPU8L', 'CVGJ9999', 'GQ90ULQV', 'R09CUULU', 'UPVVPQJR', '22PYCCGGY', '90U9UQ9LP', '22RJ8QJUJ', 'UY8CPGYJ', 'V9QQLUUR', 'CLQG0Q0P', '8PQRPJ9UP', 'JUGJJP8P', 'RCVCJYUY', '99CPPQY9G', '802L000RR', 'Q8GVR9V0C', '8cp8pvg0j', '9vurryuy9', 'u2yv080g', 'jpjcccy8', '8QQCUQ0LL', '2CU9Q0VRG', '9l88c99uq', 'l98ugu2c9', 'yr980qcu2', 'qv8uj9y9', '2R89P0VP0', '2yyy8j0cgl', 'Y9CQJ20LU']

    player_data = []
    total_trophies = 0
    for player_code in player_codes:
        player_name, trophies = get_player_info(player_code)
        if player_name and trophies is not None:
            player_data.append((player_name, trophies))
            total_trophies += trophies

    return render_template('index.html', player_data=player_data, total_trophies=total_trophies)

def get_player_info(player_tag):
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjVjNjUyOTY1LTA3ZDItNDVjYS1hN2E3LTdjYTE2M2EyMDAzYyIsImlhdCI6MTcxODgwMzI1Mywic3ViIjoiZGV2ZWxvcGVyLzUyZjc0ZjZhLWNjNDctZmZlOS1iNTEyLTQzZTlmYzQyODdlZSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMS4zNi45LjU2Il0sInR5cGUiOiJjbGllbnQifV19.iyLGUuV5U-HBF467xOQ0pzWTJvVh7geaHuetALAhEYuaUF9U01P17iZPed8maw1IYbPnnFNMEFkXUHhtYm6COA'

    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f'https://api.brawlstars.com/v1/players/%23{player_tag}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'name' in data:
            player_name = data['name']
        else:
            player_name = player_tag
        if 'trophies' in data:
            trophies = data['trophies']
        else:
            trophies = 0
    elif response.status_code == 404:
        print(f"Error retrieving data for player {player_tag}: {response.status_code} - {response.text}")
        player_name = None
        trophies = None
    else:
        print(f"Error retrieving data for player {player_tag}: {response.status_code} - {response.text}")
        player_name = None
        trophies = None
    return player_name, trophies

if __name__ == '__main__':
    app.run()