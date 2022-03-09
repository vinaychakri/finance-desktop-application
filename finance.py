import tkinter as tk
from tkinter import ttk
def amortization_schedule():
    screen1 = tk.Tk()
    screen.resizable(height='False',width='False')
    screen1.title(" Loan Amortization Schedule Table")
    screen1.iconbitmap("C:/Users/vinay/OneDrive/Desktop/iconfinder_pig_4634978.ico")
    #label = tk.Label(screen1, text="Loan Amortization Schedule", font=("Arial",30)).grid(row=0, columnspan=3)
    cols = ('Payment No', 'Payment Amount', 'Principal amount paid','Interest amount paid','Loan outstanding balance')
    listBox = ttk.Treeview(screen1, columns=cols, show='headings')
    for col in cols:
            listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=2)
    A = float(loan_amount_entry.get())
    Rn = float(annual_interest_entry.get())/(100*12)
    N = int(loan_period_entry.get())*12
    for n in range(1, (N+1), 1):
        Payment_amount = (A*Rn*((1+Rn)**N))/(((1+Rn)**N)-1)
        Principal_amount = (Payment_amount*(((1+Rn)**(n-N-1))))
        Interest_amount = (Payment_amount - Principal_amount)
        Outstanding_amount = ((Interest_amount/Rn) - Principal_amount)
        for row in range(n,n+1):
            for column in range(1):
                tempList = [[row], [round(Payment_amount,9)], [round(Principal_amount,9)],
                                [round(Interest_amount,9)],[abs(round(Outstanding_amount,9))]]
                listBox.insert("", "end", values=(tempList))
    screen1.mainloop()      
      
def main_screen():
  global screen
  screen = tk.Tk()
  screen.geometry("400x250")
  screen.title("Loan Amortization Schedule")
  screen.iconbitmap("F:/python coding/python exe files/calculator/dist/financeicon.ico")
  screen.resizable(height='False',width='False')
  global loan_amount
  global annual_interest
  global loan_amount_entry
  global annual_interest_entry
  global loan_period
  global loan_period_entry
  
  loan_amount = tk.StringVar()
  annual_interest = tk.StringVar()
  loan_period= tk.StringVar()
  
  tk.Label(screen, text = "Please enter details below",font=("times new roman",15,"bold")).pack()
  
  tk.Label(screen, text = "Total amount of loan :",font=("verdana italic",10,"bold")).pack()
  loan_amount_entry = tk.Entry(screen, textvariable = loan_amount,bd=5,relief="raised",bg="white",fg="black")
  loan_amount_entry.pack()
  
  tk.Label(screen, text = "Annual interest rate :",font=("verdana italic",10,"bold")).pack()
  annual_interest_entry =  tk.Entry(screen, textvariable = annual_interest,bd=5,relief="raised",bg="white",fg="black")
  annual_interest_entry.pack()
  
  tk.Label(screen, text = " Number of loan period(years):",font=("verdana italic",10,"bold")).pack()
  loan_period_entry =  tk.Entry(screen, textvariable = loan_period,bd=5,relief="raised",bg="white",fg="black")
  loan_period_entry.pack()
  tk.Label(screen, text = "").pack()  
  ttk.Button(text = "submit", width = "15", command = amortization_schedule).pack()
  ttk.Style().configure("TButton", padding=6, relief="flat", background="#000",font=("verdana italic",10,"bold"))
  screen.mainloop()
main_screen()