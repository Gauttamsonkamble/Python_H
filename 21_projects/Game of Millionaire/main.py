
questions = [
            ["who is shahrukh khan?","Doctor","Engineer","Actor","writer",3],
            ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
            ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
            ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
            ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
            ["What is the square root of 64?", "8", "10", "6", "12", 1],
            ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
            ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
            ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
            ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
            ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
            ]

prizes = [10000, 15000, 20000,25000, 30000, 350000, 40000,45000,50000,55000,60000]

i = 0

for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    print()

    # check whether answer is correct or not

    a = int(input("Enter your answer . 1 for a | 2 for b | 3 for c | 4 for d "))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, The Correct answer was {question[5]} \n")
        print(" Better luck next time..!")
        break
    print(f"You won {prizes[i]}")
    i+=1