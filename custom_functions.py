import json
import requests
import numpy as np


def get_omdb_data(movie_name, release_year):
    movie_name_formatted = movie_name.replace(' ', '+')

    api_key = '21dc3090'
    url = 'http://www.omdbapi.com/?apikey=' + api_key
    search_response = requests.get(url, params={
        'y': release_year,
        't': movie_name_formatted,
    })

    search_response_decoded = search_response.text.encode(
        'utf-8').decode('utf-8')
    search_response_json = json.loads(search_response_decoded)

    if search_response_json['Response'] == 'True':

        return search_response_json
    else:

        return np.nan
