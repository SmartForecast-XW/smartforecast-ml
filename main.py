from statistics import mean

sales = [120, 135, 150, 145, 170, 180]

def forecast(data):
    prediction = mean(data)
    return round(prediction, 2)

print("Next Month Forecast:", forecast(sales))
