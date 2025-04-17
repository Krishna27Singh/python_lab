data = {
    "india": {"capital": "delhi", "language": "hindi"},
    "china": {"capital": "china_capital", "language": "chinese"},
    "america": {"capital": "washington", "language": "english"},
}

country = input("Enter the country name")
print("The capital of and official language of ", country, " is ", data[country])