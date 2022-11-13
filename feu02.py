import sys 

operators = ["/","*","%","+","-"]
open_priority = ["[","("]
close_priority = ["]",")"]


def operation(calcul):
    #delete priority
    if type(calcul) == str:
        return calcul
    open_index=-1
    number_priority = 0
    calcul_result = calcul[:]
    decalage_len = 0
    for i in range(len(calcul)):
        if calcul[i] in close_priority:
            number_priority += 1
        if open_index != -1 and number_priority == 0: 
            del calcul_result[open_index+decalage_len:i+1+decalage_len]
            temp = operation(calcul[open_index+1:i])
            if type(temp) == str : 
                calcul_result.insert(open_index+decalage_len,temp)
                decalage_len += open_index-i-1
                decalage_len += 1
            else : 
                calcul_result = calcul_result[:open_index+decalage_len] + temp + calcul_result[open_index+decalage_len:]
                decalage_len += open_index-i-1
                decalage_len += len(temp)
            open_index = -1
        if calcul[i] in open_priority:
            if open_index == -1 : open_index = i
            number_priority -= 1

    
    decalage=0
    calcul_result_bis = calcul_result[:]

    for operator in operators :
        i = 0
        while i < len(calcul_result):
            if calcul_result[i] == operator:
                if operator == "*":
                    temp = int(calcul_result[i-1]) * int(calcul_result[i+1])
                    calcul_result = calcul_result[:i-1] + [str(temp)] + calcul_result[i+2:]
                    i-=1
            if calcul_result[i] == operator:
                if operator == "%":
                    temp = int(calcul_result[i-1]) % int(calcul_result[i+1])
                    calcul_result = calcul_result[:i-1] + [str(temp)] + calcul_result[i+2:]
                    i-=1
            if calcul_result[i] == operator:
                if operator == "/":
                    temp = int(int(calcul_result[i-1]) / int(calcul_result[i+1]))
                    calcul_result = calcul_result[:i-1] + [str(temp)] + calcul_result[i+2:]
                    i-=1
            if calcul_result[i] == operator:
                if operator == "+":
                    a = calcul_result[:i]
                    b = calcul_result[i+1:]
                    if len(a) == 1 and len(b) == 1:
                        return [int(calcul_result[:i][0]) + int(calcul_result[i+1:][0])]
                    else :
                        return [int(operation(calcul_result[:i])[0]) + int(operation(calcul_result[i+1:])[0])]
            if calcul_result[i] == operator:
                if operator == "-":
                    a = calcul_result[:i]
                    b = calcul_result[i+1:]
                    if len(a) == 1 and len(b) == 1:
                        return [int(calcul_result[:i][0]) - int(calcul_result[i+1:][0])]
                    else :
                        return [int(operation(calcul_result[:i])[0]) - int(operation(calcul_result[i+1:])[0])]
            i += 1
    return (calcul_result)

argv = sys.argv[1].split(" ")
result = operation(argv)
if type(result) == str:
    print(result)
else :
    print(result[0])