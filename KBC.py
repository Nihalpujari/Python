QnA=[
    ["Which planet is known as the Red Planet?", "A) Earth B) Mars C) Jupiter D) Venus", "B"],
    ["What is the capital of India?", "A) Mumbai B) Delhi C) Kolkata D) Chennai", "B"],
    ["Which ocean is the largest?", "A) Atlantic B) Indian C) Arctic D) Pacific", "D"] ,
    ["What is the chemical symbol for water?", "A) H2O B) O2 C) CO2 D) HO", "A"],
    ["Which country is home to the Great Barrier Reef?", "A) USA B) Australia C) Canada D) India", "B"],
    ["Which is the longest river in the world?", "A) Amazon B) Nile C) Yangtze D) Mississippi", "B"],
    ["Who invented the telephone?", "A) Albert Einstein B) Thomas Edison C) Alexander Graham Bell D) Nikola Tesla", "C"],    
    ["What is the tallest mountain in the world?", "A) Mount Kilimanjaro B) K2 C) Mount Everest D) Mount Fuji", "C"],
    ["Which continent is the Sahara Desert located in?", "A) Asia B) Africa C) South America D) Australia", "B"],
    ["Which bird is often associated with delivering babies in folklore?", "A) Owl B) Sparrow C) Eagle D) Stork", "D"],
    ["What is the national currency of Japan?", "A) Yen B) Won C) Dollar D) Rupee", "A"],
    ["Which country gifted the Statue of Liberty to the USA?", "A) Germany B) France C) Italy D) Spain", "B"],
    ["Which is the smallest country in the world by area?", "A) Monaco B) Vatican City C) Luxembourg D) San Marino", "B"],
    ["What is the freezing point of water?", "A) 0°C B) 50°C C) 100°C D) -10°C", "A"],
    ["Who was the first man to walk on the moon?", "A) Yuri Gagarin B) Neil Armstrong C) Buzz Aldrin D) Michael Collins", "B"]
]

levels=[1000,2000,3000,5000,10000,20000,30000,50000,100000,1000000,2500000,5000000,10000000,20000000,50000000,10000000]

score=0
for i in range(0,15):
    q=QnA[i]
    print("Question for :",levels[i],"Rs/n")
    print(q[0])
    print(q[1])
    reply=input('enter your option(A,B,C,D): ').upper()
    if(reply==q[-1]):
        print('correct')
        score=levels[i]
        if(score==10000000):
            print("congo you have won the jackpot 100000000 Rs")
            break
    else:
        print('incorrect,game over')
        print("your score is",score)
        break
