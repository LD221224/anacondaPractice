import googletrans

translator = googletrans.Translator()

str1 = '행복하세요'
result1 = translator.translate(str1, dest='en', src='auto')
print(f'{str1} => {result1.text}')

str2 = 'I am happy'
result2 = translator.translate(str2, dest='ko', src='en')
print(f'{str2} => {result2.text}')

lang = googletrans.LANGUAGES
# print(lang) 
# 사용 가능한 언어 출력