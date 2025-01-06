from lab1 import Caesar, alphabet
preprocess = Caesar.preprocessing

rus_alphabet = alphabet
# print(preprocess('МАМА Я В ДУБАЕ. аЛЁ42'))

text = 'Я был разбужен спозаранку Щелчком оконного стекла. Размокшей \
каменной баранкой В воде Венеция плыла. Все было тихо, и, однако, Во \
сне я слышал крик, и он Подобьем смолкнувшего знака Еще тревожил \
небосклон'

# def k_gramms
preprocessed_text = preprocess(text)
import numpy as np


def get_k_gramms_entries(text: str, k: int):
    k_gramms =  [text[i : i + k] for i in range(len(text) - k + 1)]
    
    n = len(k_gramms)
    # print('n', n, k_gramms)
    k_gramms_freq = {gramm: text.count(gramm)/n for gramm in set(k_gramms)}

    return dict(sorted(k_gramms_freq.items(), key=lambda x: x[1], reverse=True))

# s = 'разбиениеби'
# example_text = preprocess(s) 
# k_gramms_freq_dict = get_k_gramms_entries(example_text, 2)
# # calculate_entropy_and_language_norma()
# print(k_gramms_freq_dict)

# grams = k_grams(text, k)
# frequences = Counter()



def get_k_gramms_frequency_dict(text: str):
    '''Метод для получения частотного словаря для данного текста'''
 
    k_interval = range(1, 5+1)
    k_gramms_dict = {key: {} for key in k_interval}

    for k in k_interval:
        gramm_dict = {}
        for bias in range(k):
            for i in range(bias, len(text)-k+1, k):
                k_gramm = text[i:i+k]
   
                if all(symbol in rus_alphabet for symbol in k_gramm):
                    if k_gramm not in gramm_dict: gramm_dict[k_gramm] = 1
                    else: gramm_dict[k_gramm] += 1
                
        k_gramms_dict[k] = gramm_dict
     
    for k in k_gramms_dict:
        k_gramms_dict[k] = dict(sorted(k_gramms_dict[k].items(), key=lambda x: x[1], reverse=True))
        n = sum(list(k_gramms_dict[k].values()))

        # if k == 2: 
            # print(f'n: {n}, dict: {k_gramms_dict[k]}')
        for key in k_gramms_dict[k]:
           
            frequency = k_gramms_dict[k][key]/n
            k_gramms_dict[k][key] = frequency
    
    return k_gramms_dict

# dict_ans = get_k_gramms_frequency_dict(example_text)

# print(dict_ans[2])
# for k in k_gramms_dict:
#     print('--------------')
#     print(k_gramms_dict[k])



def calculate_entropy_and_language_norma(k: int, k_gramm_dict: list): 
   entropy = -sum(k_gramm_freq*np.log2(k_gramm_freq) for k_gramm_freq in k_gramm_dict)
   lang_norma = -sum(k_gramm_freq*np.log2(k_gramm_freq)/k for k_gramm_freq in k_gramm_dict)

   return entropy, lang_norma


k_gramms_dict = get_k_gramms_frequency_dict(preprocessed_text)

entropy_dict = {}
lang_norma = []
for k in range(1, 5+1):
    entropy, lang_norma_value = calculate_entropy_and_language_norma(k, k_gramms_dict[k].values())
    entropy_dict[k] = entropy
    lang_norma.append(lang_norma_value)

# calculate_entropy(k_gramms.values())

import matplotlib.pyplot as plt

def k_entropy_graphic(k, lang_norma):

    plt.plot(k, lang_norma, label='Энтропия', color='b', marker='o')  # Кривая с маркерами
    
    for i in range(len(k)):
        plt.text(k[i], lang_norma[i], f'{lang_norma[i]:.2f}', ha='center', va='bottom', fontsize=10)

    plt.xlabel('k')
    plt.ylabel('Языковая норма')
    plt.title('Зависимость между k и языковой нормой')
    plt.xticks(k)  
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()


def display_graphic():
    k_entropy_graphic(list(entropy_dict.keys()), lang_norma)
    


def entropy_lang_norm_interface():
    for k in range(1, 5+1):
        entropy, lang_norma_value = calculate_entropy_and_language_norma(k, k_gramms_dict[k].values())
        entropy_dict[k] = entropy
        print('---------------------------------------------')
        print(f'k: {k}, энтропия: {round(entropy, 3)}, языковая норма: {round(lang_norma_value, 3)}')
# entropy_lang_norm_interface()
