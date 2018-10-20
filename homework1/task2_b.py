#Task 2 - (b) mono-aplhpabetic substitution

import operator
ciphertext = 'qsgxsogubouuoxztqdatoxgukzlbaquowpqjapolnalaholhsgwutanolhkpsgpzxxggbgbolhgqqolhoqpmkbdqzxrgbajadxknukwqamtdglkzhszlbgwsgwawnjoqsoqptghpsalholhbkjlmzqhglgwattdvzpqappsgsabhkqoqplgxrloxgtdpqwaohsqglgbkzqalbjaphkolhqkhofgqsgsgbhgskhamtkjjoqsoqpsgaboqjkztbqjopqoqpgtuwkzlbalbtkkrziolsgwuaxgjoqspzxsaizyytgbgeiwgppoklqsaqpsgxkztblkqsgtimzwpqolhkzqtazhsolhalbjsglpsgsabhkqoqpsgabbkjlalbjaphkolhqkmgholahaoloqjapfgwdiwkfkrolhqkuolbqsaqqsgsgbhgskhsabzlwkttgboqpgtualbjapolqsgaxqkuxwajtolhajadmgpobgpattqsopqsgwgjaphglgwattdawobhgkwuzwwkjolqsgjadjsgwgfgwpsgjalqgbqkpglbqsgsgbhgskhqkalbapqsgbkzmtgbzipktbogwpjgwgatjadphgqqolhzialbjatrolhkuuqkkqsgwiawqpkuqsghwkzlbatoxgpkklxangqkqsgxklxtzpoklqsaqoqjapafgwdbouuoxztqhangolbggb'
alphabet = list('abcdefghijklmnopqrstuvwxyz')
english_freq_spaced = list('etainohdsglrwucfypbmvkzxj-') #This took some trial and error
english_freq = [i for i in english_freq_spaced if i != " "]
result = {}
for a in alphabet:
    result[a] = ciphertext.count(a)
sorted_result = sorted(result.items(), key = lambda kv: kv[1], reverse=True)
freq = [i[0] for i in sorted_result]
print(freq)
decipher = {}
for i in range(0, 26):
    decipher[freq[i]] = english_freq[i]
print(decipher)
text_list = list(ciphertext)
plaintext_list = [decipher[i] for i in text_list]
plaintext = ''.join(plaintext_list)
print(plaintext)

