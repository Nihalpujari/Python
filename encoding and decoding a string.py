import random
import string


#generate ranndom letters
randoml=''.join(random.choices(string.ascii_letters, k=3))

#user input
main_word=str(input("enter the word to be encoded  "))

#encoding
fist_letter=main_word[0]
second_half=main_word[1:len(main_word)]
joined=second_half+fist_letter
final_ans=randoml+joined+randoml
print(final_ans)

#decoding
getting_ans=final_ans[3:-3]
last=getting_ans[-1]
decoded=last+getting_ans
finalll_ans=decoded[0:-1]
print(finalll_ans)