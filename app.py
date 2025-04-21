import tkinter as tk
from tkinter import ttk
import pandas as pd
import joblib

# Function for Calling the Model

def predict_exceptions():
    if text_input1.get() == "" or text_input2.get() == "" or text_input3.get() == "" or text_input4.get() == "" or text_input5.get() == "" :
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END,"Kindly Check Your Missing Inputs !!!")
        
    else:
        InputValueForModel = pd.DataFrame({
            'Loading_meter': [float(text_input1.get())],
            'Gross_weight': [float(text_input2.get())],
            'Volume': [float(text_input3.get())],
            'Handling_unit_quantity': [float(text_input4.get())],
            'Billed_freight_weight': [float(text_input5.get())],
            'Consignor_country': [float(dropdown_mapping2[dropdown_var2.get()])],
            'Recipient_country': [float(dropdown_mapping2[dropdown_var3.get()])],
            #'Weeks_after_project_GoLive': [float(text_input6.get())],
            'Exception_happened_1week_ago': [float(dropdown_mapping3[dropdown_var4.get()])],
            'Exception_happened_2weeks_ago': [float(dropdown_mapping3[dropdown_var5.get()])],
            'distance_cluster': [float(dropdown_mapping1[dropdown_var1.get()])],
        })

        model = joblib.load("ML_Model.joblib")      
        prediction=model.predict(InputValueForModel)
        confidence_probability=model.predict_proba(InputValueForModel)
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"Predicted Exceptions Type for This Case is '{prediction[0]}' with {int(confidence_probability.max(axis=1)[0]*100)}% Confidence Level." )

    
# Function for 'Reset' Button

def reset_inputs():
    text_input1.delete(0, tk.END)
    text_input2.delete(0, tk.END)
    text_input3.delete(0, tk.END)
    text_input4.delete(0, tk.END)
    text_input5.delete(0, tk.END)
    #text_input6.delete(0, tk.END)
    
    dropdown_var1.set(dropdown_options1[0])
    dropdown_var2.set(dropdown_options2[0])
    dropdown_var3.set(dropdown_options3[0])
    dropdown_var4.set(dropdown_options4[0])
    dropdown_var5.set(dropdown_options5[0])
        
    results_text.delete(1.0, tk.END)


    
    
# Function for Handling Numeric Values

def validate_number(M):
    if M == "" or M.isdigit() or M == "-" or M.replace(".", "", 1).isdigit():
        return True
    else:
        return False


    
# Options for Dropdown Buttons

dropdown_mapping1 = {"0-50 km":"1", "50-200 km":"2", "200-500 km":"3", "500-800 km":"4", "800-1300 km":"5", "1300-1800 km":"6",">1800 km":"7"}    
    
dropdown_mapping2 = {'AT':'1','BE':'2','BG':'3','CH':'4','CZ':'5','DE':'6','ES':'7','FR':'8','GB':'9','HU':'10','IT':'11','L':'12','LU':'13','MA':'14','MD':'15','MK':'16','NL':'17','PL':'18','PT':'19','RO':'20','RS':'21','RU':'22','SE':'23','SI':'24','SK':'25','TR':'26','UA':'27'}

dropdown_mapping3 = {"False":"0","True":"1"}



# Main Window Section

root = tk.Tk()
root.title("Predictive Modeling of Transport Order Exceptions || Developed by MD A B M Mehedi Hassan ")
root.geometry("1400x750")
root.config(bg="indigo")
header_label = tk.Label(root, text="Data-Driven Insights for Exception Prediction in Transport Order Management", bg="indigo",foreground="white",font=("Bell MT",25,"bold"))
header_label.grid(row=0, columnspan=2, padx=100, pady=10)

vcmd = (root.register(validate_number), '%P')



# User Input Section

label1 = tk.Label(root, text="Loading_meter [ldm] : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
text_input1 = tk.Entry(root, validate="key", validatecommand=vcmd,width=15,font=("Comic Sans MS",15,"bold"),bg="gainsboro",fg="black", borderwidth=3)
text_input1.grid(row=1, column=1, padx=10, pady=5,sticky="w")

label2 = tk.Label(root, text="Gross_weight [kg] : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label2.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
text_input2 = tk.Entry(root, validate="key", validatecommand=vcmd,width=15,font=("Comic Sans MS",15,"bold"),bg="gainsboro",fg="black", borderwidth=3)
text_input2.grid(row=2, column=1, padx=10, pady=5,sticky="w")

label3 = tk.Label(root, text="Volume [m3] : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label3.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
text_input3= tk.Entry(root, validate="key", validatecommand=vcmd,width=15,font=("Comic Sans MS",15,"bold"),bg="gainsboro",fg="black", borderwidth=3)
text_input3.grid(row=3, column=1, padx=10, pady=5,sticky="w")

label4 = tk.Label(root, text="Handling_unit_quantity [qty] : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label4.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
text_input4= tk.Entry(root, validate="key", validatecommand=vcmd,width=15,font=("Comic Sans MS",15,"bold"),bg="gainsboro",fg="black", borderwidth=3)
text_input4.grid(row=4, column=1, padx=10, pady=5,sticky="w")

label5 = tk.Label(root, text="Billed freight weight [kg] : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label5.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
text_input5 = tk.Entry(root, validate="key", validatecommand=vcmd,width=15,font=("Comic Sans MS",15,"bold"),bg="gainsboro",fg="black", borderwidth=3)
text_input5.grid(row=5, column=1, padx=10, pady=5,sticky="w")

label6 = tk.Label(root, text="distance_cluster : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label6.grid(row=10, column=0, padx=10, pady=5, sticky=tk.E)
dropdown_var1 = tk.StringVar()
dropdown_options1 = list(dropdown_mapping1.keys())
dropdown1 = ttk.Combobox(root, textvariable=dropdown_var1, values=dropdown_options1,width=14,font=("Comic Sans MS",15,"bold"))
dropdown1.grid(row=10, column=1, padx=10, pady=5,sticky="w")
dropdown1.current(0) 

label7 = tk.Label(root, text="Consignor_country : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label7.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)
dropdown_var2 = tk.StringVar()
dropdown_options2 = list(dropdown_mapping2.keys()) 
dropdown2 = ttk.Combobox(root, textvariable=dropdown_var2, values=dropdown_options2,width=14,font=("Comic Sans MS",15,"bold"))
dropdown2.grid(row=6, column=1, padx=10, pady=5,sticky="w")
dropdown2.current(0)  

label8 = tk.Label(root, text="Recipient_country : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label8.grid(row=7, column=0, padx=10, pady=5, sticky=tk.E)
dropdown_var3 = tk.StringVar()
dropdown_options3 = list(dropdown_mapping2.keys())  
dropdown3 = ttk.Combobox(root, textvariable=dropdown_var3, values=dropdown_options3,width=14,font=("Comic Sans MS",15,"bold"))
dropdown3.grid(row=7, column=1, padx=10, pady=5,sticky="w")
dropdown3.current(0) 

label9 = tk.Label(root, text="Exception happened 1week ago : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label9.grid(row=8, column=0, padx=10, pady=5, sticky=tk.E)
dropdown_var4 = tk.StringVar()
dropdown_options4 = list(dropdown_mapping3.keys()) 
dropdown4 = ttk.Combobox(root, textvariable=dropdown_var4, values=dropdown_options4,width=14,font=("Comic Sans MS",15,"bold"))
dropdown4.grid(row=8, column=1, padx=10, pady=5,sticky="w")
dropdown4.current(0)  

label10 = tk.Label(root, text="Exception happened 2weeks ago : ",bg="indigo",foreground="white",justify="left",font=("Comic Sans MS",15,"bold"))
label10.grid(row=9, column=0, padx=10, pady=5, sticky=tk.E)
dropdown_var5 = tk.StringVar()
dropdown_options5 =  list(dropdown_mapping3.keys())  
dropdown5 = ttk.Combobox(root, textvariable=dropdown_var5, values=dropdown_options5,width=14,font=("Comic Sans MS",15,"bold"))
dropdown5.grid(row=9, column=1, padx=10, pady=5,sticky="w")
dropdown5.current(0)  


# Buttons Section
submit_button1 = tk.Button(root, text="Predict",width=20,height=1,bg="olive",activebackground="pink",foreground="white",borderwidth=3,font=("Comic Sans MS",15,"bold"), command=predict_exceptions)
submit_button1.grid(row=11, columnspan=1,column=0, padx=20, pady=5,sticky="e")

submit_button2 = tk.Button(root, text="Reset",width=20,height=1,bg="olive",activebackground="pink",foreground="white",borderwidth=3,font=("Comic Sans MS",15,"bold"), command=reset_inputs)
submit_button2.grid(row=11, columnspan=1,column=1, padx=0, pady=5,sticky="w")


# Display Results
results_text = tk.Text(root, height=3, width=67,bg="tan",fg="indigo",font=("Comic Sans MS",15,"bold"))
results_text.grid(row=12, columnspan=2, padx=10, pady=10,sticky="s")


# Run The Application
root.mainloop()
