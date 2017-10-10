def right_justify(str_to_justify):
    whitespace_len = 70 - len(str_to_justify)
    right_justified_answer = ""
    
    for i in range(whitespace_len):
        right_justified_answer = right_justified_answer + " "

    right_justified_answer = right_justified_answer + str_to_justify
    print right_justified_answer

right_justify("allen")

