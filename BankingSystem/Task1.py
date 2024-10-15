def check_loan_eligibility(credit_score, annual_income):

    if credit_score > 700 and annual_income >= 50000:
        print("Congratulations! You are eligible for a loan.")
    elif credit_score <= 700 and annual_income < 50000:
        print("You are not eligible for a loan. Both your credit score and annual income are below the required thresholds.")
    elif credit_score <= 700:
        print("You are not eligible for a loan. Your credit score is below the required threshold of 700.")
    else:
        print("You are not eligible for a loan. Your annual income is below the required threshold of $50,000.")

# Taking input from the user
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: $"))

# Check eligibility
check_loan_eligibility(credit_score, annual_income)
