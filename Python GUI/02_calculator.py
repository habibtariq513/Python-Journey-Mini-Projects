from tkinter import *

first_num = second_num = operator = None 

# ====================================== Functions ====================================== 

def get_digit(digit):
    current = result_lable['text']
    new = current + str(digit)
    result_lable.config(text=new)

def get_operator(op):
    global first_num, operator
    first_num = int(result_lable['text'])
    operator = op
    result_lable.config(text='')

def get_result():
    global first_num, second_num, operator
    second_num = int(result_lable['text'])

    if operator == '+':
        result_lable.config(text=str(first_num + second_num))
    elif operator == '-':
        result_lable.config(text=str(first_num - second_num))
    elif operator == '*':
        result_lable.config(text=str(first_num * second_num))
    else:
        if second_num == 0:
            result_lable.config(text='Error')
        else:
            result_lable.config(text=str(round((first_num / second_num), 2)))
    
def clr_fun():
    result_lable.config(text='')

# ====================================== Main Window ======================================

root = Tk()
root.title('Calculator')
root.geometry('333x387')
root.resizable(0, 0)                                # Disable maximize button
root.configure(background='black')

# ====================================== Result Label ======================================

result_lable = Label(root, text='', fg='white', bg='black', font=('Verdana', 30, 'bold'))
result_lable.grid(row=0, column=0, pady=(20,30), columnspan=5, sticky=W)

# ====================================== Number Buttons ======================================

btn_9 = Button(root, text='9', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(9))
btn_9.grid(row=1, column=3, padx=(0,10), pady=(0,10))  

btn_8 = Button(root, text='8', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(8))
btn_8.grid(row=1, column=2, padx=(0,10), pady=(0,10))  

btn_7 = Button(root, text='7', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(7))
btn_7.grid(row=1, column=0, padx=(0,10), pady=(0,10))
  
btn_6 = Button(root, text='6', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(6))
btn_6.grid(row=2, column=3, padx=(0,10), pady=(0,10))  

btn_5 = Button(root, text='5', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(5))
btn_5.grid(row=2, column=2, padx=(0,10), pady=(0,10))  

btn_4 = Button(root, text='4', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(4))
btn_4.grid(row=2, column=0, padx=(0,10), pady=(0,10))  
  
btn_3 = Button(root, text='3', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(3))
btn_3.grid(row=3, column=3, padx=(0,10), pady=(0,10))  
  
btn_2 = Button(root, text='2', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(2))
btn_2.grid(row=3, column=2, padx=(0,10), pady=(0,10))  

btn_1 = Button(root, text='1', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(1))
btn_1.grid(row=3, column=0, padx=(0,10), pady=(0,10))  

btn_0 = Button(root, text='0', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_digit(0))
btn_0.grid(row=4, column=0, padx=(0,10), pady=(0,10))  
   
btn_equal = Button(root, text='=', bg='grey', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command=get_result)
btn_equal.grid(row=4, column=3, padx=(0,10), pady=(0,10))

# ====================================== Operation Buttons ======================================

mul_sign = Button(root, text='x', bg='yellow', fg='black', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_operator('*'))
mul_sign.grid(row=1, column=4, padx=(0,10), pady=(0,10))  

div_sign = Button(root, text='/', bg='yellow', fg='black', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_operator('/'))
div_sign.grid(row=2, column=4, padx=(0,10), pady=(0,10))  

sum_sign = Button(root, text='+', bg='yellow', fg='black', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_operator('+'))
sum_sign.grid(row=3, column=4, padx=(0,10), pady=(0,10))  

sub_sign = Button(root, text='-', bg='yellow', fg='black', font=('Verdana', 14, 'bold'), height=2, width=5, command=lambda: get_operator('-'))
sub_sign.grid(row=4, column=4, padx=(0,10), pady=(0,10))

clr_sign = Button(root, text='C', bg='Red', fg='white', font=('Verdana', 14, 'bold'), height=2, width=5, command= lambda: clr_fun())
clr_sign.grid(row=4, column=2, padx=(0,10), pady=(0,10))

root.mainloop()