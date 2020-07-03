from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

#Header lines
headerline1="<-----------------------------------CALCULATOR GROUP 32----------------------------------->"
headerline2="Mathematical Expression Solver"
headerline3="Version 1.0.0.0"
headerline4="----------------------------------------------------------------------------------------------------"

helpline1 =('''
HELP MENU:
1. The application solves a complex mathematical equations from basic maths containing
fractions, mixed fractions, addition, subtraction, multiplication, division, modulus &
exponent. Ex. - (4.2 + 567 - 231 * 0.34 / 22) * (2.3 ^ 0.078847) % 2)
2. Memory related functions for saving the calculation results, recalling them, adding
number from memory value, subtracting from memory value and clearing memory value.
''')

class check():
    def __init__(self, expression):
        self.here = expression
    


    def error_post (self):
        error = Toplevel()
        error.title("error")
        error.geometry("500x100+100+100")
        check_expression = ("check_expression", self.expression)
        lebel1 = Label(error, text = check_expression,
                width = 500,
                anchor= NW,
                fg = "red",
                padx = 0,
                pady = 0)
        lebel1.pack()
        Back = Button(error, text = "Back",
                    fg = "black",
                    width = 20,
                    height = 3,
                    bd = 1,
                    bg = "#eee",
                    cursor = "hand2",
                    command = error.destroy)
        Back.pack()
        expression = ""

    def check_expression (self):
        def operators (self):
            for i in range(len(self.expression)):
                if (self.expression[i] in operators) and (self.expression[i+1] in self.operators):
                    error_post ()
        def brakets (self):
            openNum = 0
            closeNum = 0
            openParen = ("(")
            closeParen = (")")
            for i in range(len(self.expression)):
                if (self.expression[i] in openParen):
                    openNum = openNum+1
                if (self.expression[i] in closeParen):
                    closeNum = closeNum+1
            if openNum != closeNum:
                error_post ()

#Global variables are defined here
expression = ""
operators = ["+", "-", "/"]

Qrecord1 = []   # store Question for Insert expression option
Arecord1 = []   # store Answer for Insert expression option

#This is for insert expression option
def insert_expression():
    window=Toplevel()
    window.title("Calcualtor")
    window.geometry("500x500+100+100")
    
    # In order to prevent the window from getting resized we will call 'resizable' method on the window
    window.resizable(0, 0)
    
    # Let's now define the required functions for the insert expression option Calculator to function properly.
    def error_post ():
        global expression
        error = Toplevel()
        error.title("error")
        error.geometry("500x100+100+100")
        check_expression = ("check_expression", expression)
        lebel1 = Label(error, text = check_expression, width = 500, anchor= NW, fg = "Red").pack()
        button1 = Button(error, text = "Back", fg = "black", width = 20, height = 3, bd = 1, bg = "#eee",
                    cursor = "hand2",
                    command = error.destroy).pack()
        expression = ""
        input_text.set("")
        
    # 1. First is the button click 'botton_click' function which will continuously update the input field whenever a number
    #    is entered or any button is pressed it will act as a button click update.   
    def botton_click(item):
        global expression
        expression = expression + str(item)
        input_text.set(expression)
          
    # 2. Second is the button clear 'botton_clear' function clears the input field or previous calculations using the button "C"
    def botton_clear():
        global expression
        expression = ""
        input_text.set("")
    
    # 3. Third and the final function is button equal ("=") 'botton_equal' function which will calculate the expression
    #   present in input field. For example: User clicks button 2, + and 3 then clicks "=" will result in an output 5
    
    def botton_equal():
        global expression
        global operators
        for i in range(len(expression)):
            if (expression[i] in operators) and (expression[i+1] in operators):
                error_post()
                
        openNum = 0; closeNum = 0; openParen = ("("); closeParen = (")")
        for i in range(len(expression)):
            if (expression[i] in openParen):
                openNum = openNum+1
            if (expression[i] in closeParen):
                closeNum = closeNum+1
        if openNum != closeNum:
            error_post()

        result = str(eval(expression))
        input_text.set(result)
        
        global Qrecord1
        global Arecord1
        Qrecord1.append(expression) # store Question expression
        Arecord1.append(result)     # store Answer expression
        expression = ""             # clear previous expression and ready to take new expression
    
    def go_back():
        global expression
        expression = ""             # clear previous expression while going back to previous window
        window.destroy () 
    
    # In order to get the instance of the input field 'StringVar()' is used
    input_text = StringVar()
    
    Hline1 = Label(window, text = headerline1, padx = 1, pady = 1).pack()
    Hline2 = Label(window, text = headerline2, padx = 1, pady = 1).pack()
    Hline3 = Label(window, text = headerline3, padx = 1, pady = 1).pack()
    Hline4 = Label(window, text = headerline4, padx = 1, pady = 1).pack()
    
    # Once all the functions are defined then comes the main section where you will start defining
    # the structure of the calculator inside the GUI.

    # The first thing is to create a frame for the input field
    input_frame = Frame(window, width = 500, height = 100, bd = 0, highlightbackground = "BLUE", highlightcolor = "GREEN", highlightthickness = 5)
    input_frame.pack(side = TOP)

    # Then you will create an input field inside the 'Frame' that was created in the previous step.
    # Here the digits or the output will be displayed as 'right' aligned
    input_field = Entry(input_frame, font = ('calibri', 14, 'bold'), textvariable = input_text, width = 400, bg = "Sky blue", bd = 5, justify = RIGHT)
    input_field.grid(row = 0, column = 0)
    input_field.pack(ipady = 10) # 'ipady' is an internal padding to increase the height of input field
    
    # Once you have the input field defined then you need a separate frame which will incorporate all the
    # buttons inside it below the 'input field'
    btns_frame = Frame(window, width = 500, height = 400, bg = "blue")
    btns_frame.pack()
    
    # The first row will comprise of the buttons 'open & close parentheses ()''Clear (C)' and 'Divide (/)'

    Bopen = Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:botton_click("(")).grid(row = 0, column = 0, padx = 1, pady = 1)
    Bclose = Button(btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: botton_click(")")).grid(row = 0, column = 1, padx = 1, pady = 1)
    expo = Button(btns_frame, text = "**", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: botton_click("**")).grid(row = 0, column = 2, padx = 1, pady = 1)
    divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: botton_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
    
    # The second row will comprise of the buttons '7', '8', '9' and 'Multiply (*)'
    seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
    eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
    nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
    multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: botton_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
    
    # The third row will comprise of the buttons '4', '5', '6' and 'Subtract (-)'
    four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
    five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
    six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
    minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: botton_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
    
    # The fourth row will comprise of the buttons '1', '2', '3' and 'Addition (+)'
    one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
    two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
    three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
    plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: botton_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
    
    # The fifth row will comprise of the buttons '0', 'Decimal (.)', 'clear (c)' and 'Equal To (=)'
    zero = Button(btns_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: botton_click(0)).grid(row = 4, column = 0, columnspan = 1, padx = 1, pady = 1)
    point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: botton_click(".")).grid(row = 4, column = 1, padx = 1, pady = 1)
    clear = Button(btns_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: botton_clear()).grid(row = 4, column = 2, columnspan = 1, padx = 1, pady = 1)
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: botton_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
    
    # finally, the six row will comprise of the buttons 'Back', 'Exit'
    Back = Button(btns_frame, text = "Back", fg = "black", width = 20, height = 3, bd = 1, bg = "#eee", cursor = "hand2", command = lambda: go_back()).grid(row = 5, column = 0, columnspan = 2, padx = 1, pady = 10)
    Exit = Button(btns_frame, text = "Exit", fg = "black", width = 20, height = 3, bd = 1, bg = "#eee", cursor = "hand2", command = root.destroy).grid(row = 5, column = 2, columnspan = 2, padx = 1, pady = 10)

#This is for Expression from file
def open_file ():
    filename = Toplevel ()
    filename.title("From file")
    filename.geometry("400x200+100+100")
    filename.resizable(0, 0)
    
    def select_name ():
        file1 = filedialog.askopenfilename(initialdir="/",title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        with open(file1,'r') as UseFile:
            expression = UseFile.read()
            check_expression()
            try:
                answer = eval(expression)
            except:
                answer = "Wrong expression"    

        global Qrecord1
        global Arecord1
        Qrecord1.append(expression) # store Question expression
        Arecord1.append(answer)     # store Answer expression
        
        filename.destroy()
        
        result=Toplevel()
        result.title("From file")
        result.geometry("400x200+100+100")
        result.resizable(0, 0)
        
        lable1 = Label(result, text = "Expression is", anchor = NW, width = 10).grid(row = 0, column = 0)
        lable2 = Label(result, text = ":", anchor = NW, width = 1).grid(row = 0, column = 1) 
        lable3 = Label(result, text = expression, anchor = NW, width = 50,).grid(row = 0, column = 2)  
        lable4 = Label(result, text = "Output is", anchor = NW, width = 10).grid(row = 1, column = 0)
        lable5 = Label(result, text = ":", anchor = NW, width = 1).grid(row = 1, column = 1)
        lable6 = Label(result, text = answer, anchor = NW, width = 50).grid(row = 1, column = 2)
        
        button1 = Button(result, text ='Back', anchor=CENTER, width = 15,
                         fg = "black", height = 1, bd = 1, bg = "#eee",
                         cursor = "hand2", command = result.destroy)
        button2 = Button(result, text ='Exit', anchor=CENTER, width = 15,
                         fg = "black", height = 1, bd = 1, bg = "#eee",
                         cursor = "hand2", command = root.destroy)
        button1.grid(row = 3, column = 2,)
        button2.grid(row = 4, column = 2,)
            
    button1 = Button(filename, text ='Please click to select the file', width = 25,
                     fg = "black", height = 1, bd = 1, bg = "#eee",
                     cursor = "hand2", command = lambda:select_name())
    button2 = Button(filename, text ='Cancel', width = 15,
                     fg = "black", height = 1, bd = 1, bg = "#eee",
                     cursor = "hand2", command = filename.destroy)
    button1.grid(row = 1, column = 2, padx = 100, pady = 40)
    button2.grid(row = 4, column = 2, padx = 0, pady = 1)

#This is for history
def open_history ():
    history = Toplevel ()
    history.title("History")
    history.geometry("500x500+100+100")
    history.resizable(0, 0)
    
    Heading_frame = Frame(history, width = 500, height = 10, highlightbackground = "BLUE",highlightthickness = 1)
    Heading_frame.pack(side = TOP)
    label1 = Label(Heading_frame,text = "S.No", width = 4,).grid(row = 0, column = 0)
    label2 = Label(Heading_frame,text = ":", width = 1,).grid(row = 0, column = 1)
    label3 = Label(Heading_frame,text = "Expression", width = 45,).grid(row = 0, column = 2)
    label4 = Label(Heading_frame,text = ":", width = 1,).grid(row = 0, column = 3)
    label5 = Label(Heading_frame,text = "Result", width = 20,).grid(row = 0, column = 4)
    
    history_frame = Frame(history, width = 500, height = 440, highlightbackground = "#eee",highlightthickness = 1)
    history_frame.pack(side = TOP)
    r = 1
    n = 1
    for c in Qrecord1:
        label1 = Label(history_frame, text = r , width = 4, anchor = NW).grid(row = r, column = 0)
        label2 = Label(history_frame, text = ":", width = 1).grid(row = r, column = 1)
        label3 = Label(history_frame, text = c, width = 45, anchor = NW).grid(row = r, column = 2)
        label4 = Label(history_frame, text = ":", width = 1).grid(row = r, column = 3)
        r = r + 1
    r = 1
    for c in Arecord1:
        label5 = Label(history_frame, text = c, width = 20, anchor = NW).grid(row = r, column = 4)
        r = r + 1     
    button1 = Button(history, text = "OK", fg = "black",
                width = 5, height = 2, bd = 1, bg = "#eee",
                cursor = "hand2", command = history.destroy).pack(side = BOTTOM)
    
#This is for help menu
def open_help():
    help=Toplevel()
    help.title("Help Window")
    help.geometry("500x200+150+150")
    help.resizable(0, 0)
    lable1 = Label(help, text = helpline1, anchor = NW, width = 100).pack(side=TOP)  
    button1 = Button(help, text = "Ok", fg = "black", width = 5, height = 3, bd = 1, bg = "#eee", cursor = "hand2", command = help.destroy).pack(side=BOTTOM)

#Home menu
root = Tk()
root.resizable(0, 0)
root.title("Calcultor")
root.geometry("500x500+100+100")

label1 = Label(root, text = headerline1).grid(row = 0, column = 0)
label2 = Label(root, text = headerline2).grid(row = 1, column = 0)
label3 = Label(root, text = headerline3).grid(row = 2, column = 0)
label4 = Label(root, text = headerline4).grid(row = 3, column = 0)

button1 = Button(root, text = "[1]. Insert Expression", anchor = NW, width = 50, fg = "black", height = 1, bd = 1, bg = "#eee", cursor = "hand1", command = insert_expression).grid(row = 5, column = 0, padx = 1, pady = 1)
button2 = Button(root, text = "[2]. View History", anchor = NW, width = 50, fg = "black", height = 1, bd = 1, bg = "#eee", cursor = "hand2", command = open_history).grid(row = 6, column = 0, padx = 1, pady = 1)
button3 = Button(root, text = "[3]. Expression file", anchor = NW, width = 50, fg = "black", height = 1, bd = 1, bg = "#eee", cursor = "hand2", command = open_file).grid(row = 7, column = 0, padx = 1, pady = 1)
button4 = Button(root, text = "[4]. Help Menu", anchor = NW, width = 50, fg = "black", height = 1, bd = 1, bg = "#eee", cursor = "hand2", command = open_help).grid(row = 8, column = 0, padx = 1, pady = 1)
button5 = Button(root, text = "[5]. Exit", anchor = NW, width = 50, fg = "black", height = 1, bd = 1, bg = "#eee", cursor = "hand2", command = root.destroy).grid(row = 9, column = 0, padx = 1, pady = 1)

label5 = Label(root, text = "Group 32 Members -", width = 50, anchor = NW, padx = 0, pady = 1).grid(row = 11, column = 0, padx = 0, pady = 10)

icon1 = PhotoImage(file = "team.png",)
label6 = Label(root, image = icon1, bg = "#eee")
label6.place(x=70, y=250)

root.mainloop()
