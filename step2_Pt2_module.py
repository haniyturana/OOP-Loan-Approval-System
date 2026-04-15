# Step 1: Parent Class
class Customer:
    def __init__(self, name, age, income, monthly_debt):
        self.name = name
        self.age = age
        self.income = income
        self.monthly_debt = monthly_debt

    def calculate_dti(self):
        return self.monthly_debt / self.income if self.income else 0

    def risk_category(self):
        dti = self.calculate_dti()
        if dti < 0.2:
            return "Low Risk"
        elif dti < 0.4:
            return "Medium Risk"
        else:
            return "High Risk"

# Step 2: Child Class
class CreditScoreCustomer(Customer):
    def __init__(self, name, age, income, monthly_debt, credit_score):
        super().__init__(name, age, income, monthly_debt)
        self.credit_score = credit_score

    def credit_risk_category(self):
        # Kita longgarkan sikit threshold supaya Lan & Abu ada peluang
        if self.credit_score >= 700:
            return "Low Risk"
        elif self.credit_score >= 550: 
            return "Medium Risk"
        else:
            return "High Risk"

    # --- Loan Evaluation ---
    def evaluate_loan(self, loan_amount):
        dti = self.calculate_dti()
        dti_risk = self.risk_category()
        credit_risk = self.credit_risk_category()
        
        # 1. HARD REJECT: Skor bawah 450 tetap tidak boleh bincang
        min_score_required = 450
        if self.credit_score < min_score_required:
            return "Rejected", f"Credit score too low ({self.credit_score}). Must be at least {min_score_required}."

        # 2. HARD REJECT: DTI terlalu tinggi (atas 40%)
        if dti_risk == "High Risk":
            return "Rejected", f"DTI ratio is too high ({dti:.2%}). Monthly debt burden is unsafe."

        # 3. COMPENSATING FACTOR (Laluan Khas): 
        # Jika DTI bawah 25%, kita terima pelanggan "High Risk" (Kes Ani)
        if dti <= 0.25 and credit_risk == "High Risk":
            return "Approved", f"Approved! Excellent DTI ({dti:.2%}) compensates for High Risk Credit ({self.credit_score})."

        # 4. COMPENSATING FACTOR: 
        # Jika DTI bawah 15%, kita terima pelanggan "Medium Risk" (Kes Lan)
        if dti < 0.15 and credit_risk == "Medium Risk":
            return "Approved", f"Approved! Exceptional DTI ({dti:.2%}) balance."

        # 5. STANDARD RULE: Jika tidak memenuhi kriteria laluan khas di atas
        if credit_risk == "High Risk":
            return "Rejected", f"Credit score {self.credit_score} is High Risk and debt ratio ({dti:.2%}) is not strong enough to compensate."

        return "Approved", "Customer meets all standard financial criteria."
        
# Step 3: Print Function
def print_customer_risk(customer):
    print(f"Name: {customer.name}")
    print(f"Age: {customer.age}")
    print(f"Income (RM): {customer.income:,}")
    print(f"Monthly Debt (RM): {customer.monthly_debt:,}")
    print(f"DTI: {int(customer.calculate_dti() * 100)}%")
    print(f"DTI Risk Category: {customer.risk_category()}")
    
    if isinstance(customer, CreditScoreCustomer):
        print(f"Credit Score: {customer.credit_score}")
        print(f"Credit Risk Category: {customer.credit_risk_category()}")
        
    print("-" * 40)