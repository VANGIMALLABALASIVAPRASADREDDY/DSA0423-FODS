import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create dataset
data = {
'Name':['Ronaldo','Messi','Neymar','Kane','Mbappe','Modric','Salah','Benzema'],
'Age':[38,36,31,30,25,37,32,35],
'Position':['Forward','Forward','Forward','Forward','Forward','Midfielder','Forward','Forward'],
'Goals':[25,22,18,20,24,10,19,21],
'Salary':[500000,480000,450000,350000,420000,300000,380000,360000]
}

df = pd.DataFrame(data)

# Step 2: Save dataset as CSV
df.to_csv("players.csv", index=False)

# Step 3: Read CSV file
players = pd.read_csv("players.csv")

# Step 4: Top 5 players with highest goals
top_goals = players.sort_values(by='Goals', ascending=False).head(5)

# Step 5: Top 5 players with highest salaries
top_salary = players.sort_values(by='Salary', ascending=False).head(5)

# Step 6: Average age of players
avg_age = players['Age'].mean()

# Step 7: Players above average age
above_avg = players[players['Age'] > avg_age]

# Display results
print("Top 5 Players with Highest Goals")
print(top_goals)

print("\nTop 5 Players with Highest Salaries")
print(top_salary)

print("\nAverage Age of Players:", avg_age)

print("\nPlayers Above Average Age")
print(above_avg[['Name','Age']])

# Step 8: Bar chart for player positions
position_counts = players['Position'].value_counts()

position_counts.plot(kind='bar')

plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")

plt.show()
