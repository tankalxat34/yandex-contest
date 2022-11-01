with open(".\\input.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()


pre_answer = ""
answers = []
end_answer = "-1"

pre_symbols = ""

dict_count_of_letters = dict()
for symbol in content:
    pre_answer += symbol



    # try:
    #     dict_count_of_letters[symbol] += 1
    # except Exception:
    #     dict_count_of_letters[symbol] = 1

    

print(answers)