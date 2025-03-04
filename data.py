import requests
API_KEY = ''
API_KEY_decode = requests.utils.unquote(API_KEY)
API_KEY_decode


url = ''
search_Se = ''
srch_wrd = ''

parameter = {'ServiceKey': API_KEY_decode, 'searchSe': search_Se, 'srchwrd': srch_wrd }
result = requests.get(url, params = parameter)
print(result)#응답코드 확인, 4xx 클라이언트 에러, 5xx 서버에러
xml_data = result.text
xml_data


#!pip install xmltodict