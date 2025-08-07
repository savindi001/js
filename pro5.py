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


   #Calculation part
    if st.button("Calculate"):
        try:
            row=[]

            if jobp == "Manager":
                bonus = bsalary * 20 / 100
                row.append(["Manager",bsalary,20.00,bonus])

            if jobp == "Clark":
                bonus = bsalary * 10 / 100
                row.append(["Clark",bsalary,10.00,bonus])

            if jobp == "Other":
                bonus = bsalary * 5 / 100
                row.append(["Other",bsalary,5.00,bonus])
            
            bonus=bonus
            Total_salary=bsalary+bonus

            Total_salary=round(bsalary+bonus,2)
            row.append(["Total Salary","--","--",Total_salary])

            st.info(f"Total Salary: Rs.{Total_salary:.2f}")

             #convert to dataframe and show table
            df=pd.DataFrame(row,columns=["Description","Basic Salary","Bonus","Total Salary"])

                #format the rate and cost columns
           
            st.table(df)

        except Exception as e:
            st.error(f"Error calculating bill:{e}")

with col2:
    	st.text_input("Options\nManager\nClark\nOther")
    




            