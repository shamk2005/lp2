# Expert System - Stock Market Trading

def stock_market_system():
    print("=== Stock Market Trading Expert System ===")

    name = input("Enter Investor Name: ")
    budget = int(input("Enter Investment Amount: "))
    risk = input("Enter Risk Level (low/medium/high): ").lower()

    # Expert Rules
    if risk == "low":
        stock = "TCS / Infosys"
        advice = "Invest in stable blue-chip companies."
        expected = "8% - 12% yearly return"

    elif risk == "medium":
        stock = "Reliance / HDFC Bank"
        advice = "Balanced investment with moderate risk."
        expected = "12% - 18% yearly return"

    elif risk == "high":
        stock = "Startup / Tech Stocks"
        advice = "High risk can give high profit or loss."
        expected = "20%+ yearly return"

    else:
        stock = "No Suggestion"
        advice = "Enter valid risk level."
        expected = "Unknown"

    # Additional Suggestion
    if budget < 5000:
        plan = "Start with SIP or small investments."
    else:
        plan = "You can diversify your portfolio."

    # Display Report
    print("\n=== Investment Report ===")
    print("Investor Name :", name)
    print("Investment Amount :", budget)
    print("Risk Level :", risk)
    print("Suggested Stocks :", stock)
    print("Expected Return :", expected)
    print("Advice :", advice)
    print("Investment Plan :", plan)

if __name__ == "__main__":
    stock_market_system()


#INPUT

#Enter Investor Name: Diya
#Enter Investment Amount: 10000
#Enter Risk Level (low/medium/high): medium
