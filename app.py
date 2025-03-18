from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL base da PokeAPI
POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    pokemon_name = request.args.get('name').lower()  
    if not pokemon_name:
        return jsonify({'error': 'Pokémon name is required'}), 400

    response = requests.get(f'{POKEAPI_URL}/{pokemon_name}')
    if response.status_code != 200:
        return jsonify({'error': 'Pokémon not found'}), 404

    data = response.json()
    pokemon_info = {
        'name': data['name'].capitalize(),
        'image': data['sprites']['front_default'],
        'types': [t['type']['name'] for t in data['types']],
        'abilities': [a['ability']['name'] for a in data['abilities']],
        'height': data['height'] / 10, 
        'weight': data['weight'] / 10   
    }
    return jsonify(pokemon_info)

if __name__ == '__main__':
    app.run(debug=True)