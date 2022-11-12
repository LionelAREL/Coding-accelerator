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
            #print("calcul_result",calcul_result,decalage_len)
            del calcul_result[open_index+decalage_len:i+1+decalage_len]
            #print("calcul_result-del",calcul_result)
            temp = operation(calcul[open_index+1:i])
            if type(temp) == str : 
                #print("temp1",temp,decalage_len,open_index,i)
                calcul_result.insert(open_index+decalage_len,temp)
                decalage_len += open_index-i-1
                decalage_len += 1
                #print("temp1_after",calcul_result)
            else : 
                #print("temp2",temp,decalage_len)
                calcul_result = calcul_result[:open_index+decalage_len] + temp + calcul_result[open_index+decalage_len:]
                decalage_len += open_index-i-1
                decalage_len += len(temp)
            #print("calcul_result_after",calcul_result)
            open_index = -1
        if calcul[i] in open_priority:
            if open_index == -1 : open_index = i
            number_priority -= 1

    
    # print(calcul_result)
    decalage=0
    calcul_result_bis = calcul_result[:]

    for operator in operators :
        i = 0
        while i < len(calcul_result):
            if calcul_result[i] == operator:
                if operator == "*":
                    # print(calcul_result[i-1])
                    #print(calcul_result[i+1])
                    temp = int(calcul_result[i-1]) * int(calcul_result[i+1])
                    # print("ttemp",temp)
                    calcul_result = calcul_result[:i-1] + [str(temp)] + calcul_result[i+2:]
                    # print("resullt",calcul_result)
                    i-=1
            if calcul_result[i] == operator:
                if operator == "%":
                    # print(calcul_result[i-1])
                    #print(calcul_result[i+1])
                    temp = int(calcul_result[i-1]) % int(calcul_result[i+1])
                    # print("ttemp",temp)
                    calcul_result = calcul_result[:i-1] + [str(temp)] + calcul_result[i+2:]
                    # print("resullt",calcul_result)
                    i-=1
            if calcul_result[i] == operator:
                if operator == "/":
                    # print(calcul_result[i-1])
                    # print(calcul_result[i+1])
                    temp = int(int(calcul_result[i-1]) / int(calcul_result[i+1]))
                    # print("ttemp",temp)
                    calcul_result = calcul_result[:i-1] + [str(temp)] + calcul_result[i+2:]
                    # print("resullt",calcul_result)
                    i-=1
            if calcul_result[i] == operator:
                if operator == "+":
                    a = calcul_result[:i]
                    b = calcul_result[i+1:]
                    #print(a,b)
                    if len(a) == 1 and len(b) == 1:
                        #print("123",a,b)
                        return [int(calcul_result[:i][0]) + int(calcul_result[i+1:][0])]
                    else :
                        #print("456",operation(calcul_result[:i])[0],operation(calcul_result[i+1:])[0])
                        return [int(operation(calcul_result[:i])[0]) + int(operation(calcul_result[i+1:])[0])]
            if calcul_result[i] == operator:
                if operator == "-":
                    a = calcul_result[:i]
                    b = calcul_result[i+1:]
                    #print(a,b)
                    if len(a) == 1 and len(b) == 1:
                        #print("123",a,b)
                        return [int(calcul_result[:i][0]) - int(calcul_result[i+1:][0])]
                    else :
                        #print("456")
                        return [int(operation(calcul_result[:i])[0]) - int(operation(calcul_result[i+1:])[0])]
            i += 1
    return (calcul_result)


import sys 
argv = sys.argv[1].split(" ")
result = operation(argv)
if type(result) == str:
    print(result)
else :
    print(result[0])