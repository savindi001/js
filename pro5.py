import streamlit as st
import pandas as pd

st.title("Job Salary Bonas Calculator",width="stretch")

#Create columns to control layout
col1,col2=st.columns([3,2])

with col1:

    #input logic
    jobp=st.text_input("Enter the job position",key="jp")
    bsalary=st.number_input("Enter the Basic Salary",key='bs',min_value=0,format="%d")

    if jobp and bsalary:
        jobp=str(jobp)
        bsalary=int(bsalary)


    if st.button("Calculate"):
        row = []

        if jobp == "Manager":
            bonus = bsalary * 20 / 100
        elif jobp == "Clark":
            bonus = bsalary * 10 / 100
        else:  # Other
            bonus = bsalary * 5 / 100

        total_salary = bsalary + bonus

        row.append([jobp, bsalary, bonus, total_salary])
                
            
            

    Total_salary=round(bsalary+bonus,2)
            

    st.info(f"Total Salary: Rs.{Total_salary:.2f}")

             #convert to dataframe and show table
    df=pd.DataFrame(row,columns=["Description","Basic Salary","Bonus","Total Salary"])

                #format the rate and cost columns
    df["Bonus"] = df["Bonus"].apply(lambda x: f"{x:.2f}" if isinstance(x,(int,float))else x)
    df["Total Salary"] = df["Total Salary"].apply(lambda x: f"{x:.2f}" if isinstance(x,(int,float))else x)
    st.table(df)


with col2:
    	st.text_input("Options\nManager\nClark\nOther")
    




            