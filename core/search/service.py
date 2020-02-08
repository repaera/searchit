import json
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

# def read_bing_key():
#     bing_api_key = None

#     try:
#         with open('bing.key', 'r') as f:
#             bing_api_key = f.readline().strip()
#     except:
#         try:
#             with open('../bing.key', 'r') as f:
#                 bing_api_key = f.readline().strip()
#         except:
#             raise IOError('bing.key file not found!')

#     if not bing_api_key:
#         raise KeyError('Bing key not found.')

#     return bing_api_key

def run_query(search_terms):
    bing_key = settings.BING_KEY
    search_url = 'https://joineka.cognitiveservices.azure.com/bing/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': bing_key, 'BingAPIs-Market': 'en-ID'}
    params = {'q': search_terms, 'safeSearch': 'Moderate', 'textDecorations': True, 'textFormat': 'HTML', 'count': 15}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    return search_results



    # if search_results['webPages'] is None:
    #     HttpResponseRedirect('/')
    # else:
    # for result in search_results:
        # results.append({
        #     'title': result['webPages']['value']['name'],
        #     'link': result['webPages']['value']['url'],
        #     'summary': result['webPages']['value']['snippet'],
        # })
    # return results

# def main():
#     print("Bing search")
#     query_str = input("Enter a query to search for: ")
#     results = run_query(query_str)

#     for result in results:
#         print(result['title'])

# if __name__ == '__main__':
#     main()
