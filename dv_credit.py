from pydantic import BaseModel

class credit(BaseModel):
    person_age : int	
    person_income : int	
    person_emp_length : float	
    loan_amnt : int	
    loan_int_rate : float	
    loan_percent_income	: int 
    cb_person_cred_hist_length : float