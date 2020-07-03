from sys import exit

class Calculator:
    def __init__(self, calculation):
        self.calculation = calculation # store the expression

    def user_input(self):
        ''' Breakdown of expression into array of list '''
        calculation_array = [] # final list of operands and operators in order
        number = "" # to store number e.g. '283+10+1/32' ==> ['283','+','10','','1','/','32']
    
        for i in range(len(self.calculation)):
            if self.calculation[i].isnumeric() or self.calculation[i]=='.': # to check value at ith idex is Numeric?
                number = number + self.calculation[i] # so '2','8','3' ==> '283'
                if i == len(self.calculation)-1:
                    calculation_array.append(float(number)) # put 283 into final list of array
            else: # store operators
                if number == "":
                    calculation_array.append(self.calculation[i])
                else:
                    calculation_array.append(float(number))
                    calculation_array.append(self.calculation[i])
                    number = ""         # make number string blank, so we can again store the number         
        #send the final list of operands and operators to calculator function
#        print('calculation_array: ', calculation_array)
#        print('number: ', number)
        return self.calculator(calculation_array)

    def check_operators(self, exp_list):
        ''' To check if there is consecutive operatotrs in expression '''
        operators = ["%", "^", "+", "-", "*", "/"]
        for i in range(len(exp_list)):
            if (exp_list[i] in operators) and (exp_list[i+1] in operators):
                return False
        return True

    def solve(self, calculate):
        ''' Sorting the order of operations '''
        operators = {"^": 5, "%": 4, "/": 3, "*": 2, "+": 1, "-": 1} #put operators in heirarchy
        bodmas_index = [] # indices of operators in order
        for i in range(len(calculate)):
            if calculate[i] in operators: # if operator is available in calculation
                if len(bodmas_index) == 0:
                    bodmas_index.append(i)
                else:
                    for x in range(len(bodmas_index)):  # for each of the values stored in bodmas_index
                        if operators[calculate[i]] < operators[calculate[bodmas_index[-1]]]:
                            bodmas_index.append(i)
                            break
                        elif operators[calculate[i]] > operators[calculate[bodmas_index[x]]]:
                            bodmas_index.insert(x, i)  # insert the index value
                            break
                        elif operators[calculate[i]] == operators[calculate[bodmas_index[x]]]:
                            if calculate[i] == "+" or calculate[i] == "-":
                                bodmas_index.append(i)
                                break
                            else:
                                bodmas_index.insert(x + 1, i)
                                break
                        else:
                            continue
#                print('bodmas_index', bodmas_index)
        
        ''' All operations will be performed here '''
        while len(bodmas_index) != 0:
            if calculate[bodmas_index[0]] == '^':
                currentCalculation = float(calculate[bodmas_index[0] - 1]) ** float(calculate[bodmas_index[0] + 1])
            elif calculate[bodmas_index[0]] == '%':
                currentCalculation = float(calculate[bodmas_index[0] - 1]) % float(calculate[bodmas_index[0] + 1])
            elif calculate[bodmas_index[0]] == '/':
                try:
                    currentCalculation = float(calculate[bodmas_index[0] - 1]) / float(calculate[bodmas_index[0] + 1])
                except ZeroDivisionError:
                    print("Divide by 0.")
                    print("Exiting..........")
                    exit()

            elif calculate[bodmas_index[0]] == '*':
                currentCalculation = float(calculate[bodmas_index[0] - 1]) * float(calculate[bodmas_index[0] + 1])
            elif calculate[bodmas_index[0]] == '+':
                currentCalculation = float(calculate[bodmas_index[0] - 1]) + float(calculate[bodmas_index[0] + 1])
            else:
                currentCalculation = float(calculate[bodmas_index[0] - 1]) - float(calculate[bodmas_index[0] + 1])
    
            calculate[bodmas_index[0]-1] = currentCalculation
            calculate.pop(bodmas_index[0]+1)
            calculate.pop(bodmas_index[0])
    
            for i in range(len(bodmas_index)):
                if bodmas_index[i] > bodmas_index[0]:
                    bodmas_index.insert(i, bodmas_index[i] - 2)
                    bodmas_index.pop(i + 1)
    
            bodmas_index.pop(0)
    
        return calculate[0]

        
    def Bracket_pairs(self, calcu):
        ''' Pairs the bracket '''
        start_bracket_index_array = []
        end_bracket_index_array = []
        bracket_pairs = {}
    
        for i in range(len(calcu)):
            if calcu[i] == '(':
                start_bracket_index_array.append(i)
            elif calcu[i] == ')':
                end_bracket_index_array.append(i)
    
        ''' Finds the innermost brackets so that they can be solved first. Only returns one pair of brackets at a time. '''
        for i in range(len(start_bracket_index_array) - 1, -1, -1):
            for j in range(len(end_bracket_index_array)):
                if end_bracket_index_array[j] < start_bracket_index_array[i] or end_bracket_index_array[j] in bracket_pairs.values():
                    continue
                else:
                    bracket_pairs[start_bracket_index_array[i]] = end_bracket_index_array[j]
                    break
            break
        if len(bracket_pairs) != 0:
            return bracket_pairs

    
    def calculator(self, calc_list):
        key = self.check_operators(calc_list)
        if key==True:
            try:
                brackets = self.Bracket_pairs(calc_list) # find brackets pair
                answer = [] #save answer after 1 bracket solve
                
                if brackets is None:
                    return float(self.solve(calc_list))
                else:
                    start_bracket_index = list(brackets.keys())[0]
                    end_bracket_index = brackets[start_bracket_index]
                    answer.append(self.solve(calc_list[start_bracket_index + 1:end_bracket_index]))
                    calc_list = calc_list[:start_bracket_index] + answer + calc_list[end_bracket_index + 1:]
                    return self.calculator(calc_list)
            except TypeError:
                print("Please check your expression")
        else:
            print("Please check your expression Again")


def again():
    print('[1]. Insert Expression','[2]. Expression from File', '[3]. View History', '[4]. Help Menu','[5]. Exit', sep='\n')
    key = int(input(' --> '))
    if key==5:
        print('Thank you for using calculator !', 'Exited !!','','', sep='\n')
        exit()
    return key

key = again()
record1 = []
record2 = []

while key!=5:   
    if key==1:
        
        expression = input('Insert expression: ')
        c = Calculator(expression)
        answer = round(c.user_input(),7)
        if c.user_input() != None:
            print('Solution of {} = {}'.format(expression,answer))
            record1.append(answer)
        else:
            print("There is some mistake in expression")     
        key = again()
  
    if key==2:
        f = open("Input_File.txt","r")
        contents = f.readlines()
        print('Contents in file: {}'.format(contents))
        choice = int(input("Select your expression: "))
        c = Calculator(contents[choice])
        if c.user_input() != None:
            print('Solution of {} ='.format(contents[choice]), round(c.user_input(),7))
            record2.append(round(c.user_input(),7))
        else:
            print("There is some mistake in expression")
        f.close()
        key = again()
              
    if key==3:
        print('It is under construction please explore other options.')
        print(record1)
        print(record2)
        key = again()
    
    if key==4:
        help1=('1. The application solves a complex mathematical equations from basic maths containing fractions, mixed fractions, addition, subtraction, multiplication, division, modulus & exponent.  Ex. - (4.2 + 567 - 231 * 0.34 / 22) * (2.3 ^ 0.078847) % 2')
        help2=('2. Memory related functions for saving the calculation results, recalling them, adding number from memory value, subtracting from memory value and clearing memory value.')

        print('HELP MENU:', help1, help2, sep='\n')
        print('Press Y to continue or any key to exit')
        response = str(input(' --> '))
        ip=(response.upper())
        if ip=='Y' or ip=='y':
            print("let's go")
        else:
            exit()
        key = again()
        
    if key>5 or key<1:
        print('\nInvalid Choice...Please select correct choice\n')
        key = again()
        

