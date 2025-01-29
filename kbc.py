amount=0
questions=[
    ['Who is known as the Father of the Indian Constitution?', 'Mahatma Gandhi', 'Dr. B. R. Ambedkar', 'Jawaharlal Nehru', 'Sardar Patel', 2],
    ['Which planet is known as the Red Planet?', 'Venus', 'Mars', 'Jupiter', 'Saturn', 2],
    ['Who wrote the Indian National Anthem, "Jana Gana Mana"?', 'Bankim Chandra Chatterjee', 'Rabindranath Tagore', 'Subhas Chandra Bose', 'Sarojini Naidu', 2],
    ['What is the capital of France?', 'Berlin', 'London', 'Paris', 'Rome', 3],
    ['Which is the largest continent by area?', 'Africa', 'Asia', 'North America', 'Europe', 2],
    ['Who invented the telephone?', 'Alexander Graham Bell', 'Thomas Edison', 'Nikola Tesla', 'Guglielmo Marconi', 1],
    ['Which gas is most abundant in Earth\'s atmosphere?', 'Oxygen', 'Nitrogen', 'Carbon dioxide', 'Hydrogen', 2],
    ['Who was the first woman Prime Minister of India?', 'Sarojini Naidu', 'Indira Gandhi', 'Pratibha Patil', 'Sonia Gandhi', 2],
    ['What is the smallest unit of life?', 'Atom', 'Cell', 'Molecule', 'Tissue', 2],
    ['Which is the longest river in the world?', 'Amazon River', 'Nile River', 'Yangtze River', 'Mississippi River', 2],
    ['Which country is known as the Land of the Rising Sun?', 'China', 'Japan', 'South Korea', 'Thailand', 2],
    ['What is the chemical symbol for water?', 'CO2', 'O2', 'H2O', 'NH3', 3],
    ['Who is the author of "The Discovery of India"?', 'Rabindranath Tagore', 'Mahatma Gandhi', 'Jawaharlal Nehru', 'Sardar Patel', 3],
    ['Which Indian city is known as the Silicon Valley of India?', 'Mumbai', 'Hyderabad', 'Bengaluru', 'Pune', 3],
    ['Which organ in the human body is responsible for pumping blood?', 'Lungs', 'Liver', 'Heart', 'Brain', 3]
]

levels =  [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,  # 1.6 lakh
    320000,  # 3.2 lakh
    640000,  # 6.4 lakh
    1250000, # 12.5 lakh
    2500000, # 25 lakh
    5000000, # 50 lakh
    10000000 # 1 crore
]
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Up coming question is for {levels[i]} Rs: /n ")
    print(question[0])
    print(f"1.{question[1]}                 2.{question[2]}")
    print(f"3.{question[3]}                 4.{question[4]}")
    answer=int(input("Enter your answer:"))
    if answer==question[-1]:
        print("Correct answer")
        amount=levels[i]
    else:
        print("game over")
        break
if (amount<10000):
        print("amount won 0 Rs")
elif(10001<amount<320000):
        print("amount won 10000 Rs")
elif(320000<amount<10000000):
        print("amount won 320000 Rs")
elif(amount==10000 or amount==320000):
        print(f"amount won {amount} Rs")
elif(amount==10000000):
        print(f"YOU HAVE WON THE JACKPOT 🥳")
      