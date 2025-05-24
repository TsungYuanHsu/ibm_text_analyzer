givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer:
    def __init__(self, text):
        self.text = text.replace('!', '').replace(',', '').replace('?', '').replace('.', '')
        self.text = self.text.lower()

    def freqAll(self):
        string_list = self.text.split(' ')
        dic = {}
        for word in string_list:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        return dic

    def freqof(self, word):
        if word not in self.text:
            return 0
        else:
            return self.freqAll()[word]

given_string = TextAnalyzer(givenstring)
print(given_string.text)


print(given_string.freqAll())

count_aaa = given_string.freqof('aaa')
print(f'Count of "aaa" is {count_aaa}')

count_diam = given_string.freqof('diam')
print(f'Count of "diam" is {count_diam}')
