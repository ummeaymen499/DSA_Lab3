import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dailySteps_merged.csv')
#Part 1
list_1=df['ActivityDay'].values.tolist()
list_2=df['StepTotal'].values.tolist()
plt.plot(list_1,list_2, linewidth=1, color='green')
plt.xlabel('Date')
plt.ylabel('Total Steps')
plt.title('Daily Step Count')
plt.xticks(rotation=45)
plt.show()

# Part 2
steplength = 0.000762
df['Distance'] = df['StepTotal'] * steplength
list_1=df['ActivityDay'].values.tolist()
list_2=df['StepTotal'].values.tolist()
plt.bar(list_1,list_2, linewidth=1,color='blue')
plt.xlabel('Date')
plt.ylabel('Distance Covered (km)')
plt.title('Daily Distance Covered')
plt.xticks(rotation=45)
plt.show()

# Part 3
def estimate_time_in_bed(steps):
    if steps < 10000:
        return 8  
    elif 10000 <= steps <= 12000:
        return 7  
    else:
        return 6  

List_2=df['StepTotal'].apply(estimate_time_in_bed)
List_1=df['ActivityDay'].values.tolist()
plt.scatter(List_1,List_2, color='purple')
plt.xlabel('Date')
plt.ylabel('Time in Bed (hours)')
plt.title('Estimated Total Time in Bed on Daily Basis')
plt.xticks(rotation=45)
plt.show()

# Part 4
hourly_steps = [
    300, 150, 100, 50, 50, 500, 
    1200, 2000, 2500, 3000, 2500, 3000
]
hours = [
    "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM",
    "6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM"
]
plt.figure(figsize=(10, 7))
plt.pie(hourly_steps, labels=hours, autopct='%1.1f%%', startangle=140)
plt.title('Hourly Steps on April 12, 2016')
plt.axis('equal') 
plt.show()
