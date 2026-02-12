import pandas as pd
import matplotlib.pyplot as plt

# Sample Student Data with 3 Subjects
data = {
    'Name': ['Shashank', 'Virendra', 'Pavithraerformance ', 'Bhommi', 'Yogesh'],
    'Maths': [78, 92, 65, 88, 70],
    'Science': [82, 95, 60, 85, 75],
    'English': [80, 90, 70, 89, 68],
    'Total': [240,277,195,262,213],
    'Attendance': [90, 85, 75, 95, 80]
}


df = pd.DataFrame(data)

# ---------- Average Marks per Student ----------
df['Average'] = df[['Maths','Science','English']].mean(axis=1)
print("Student-wise Average Marks:\n", df[['Name','Average']], "\n")

# ---------- Overall Average ----------
overall_avg = df['Average'].mean()
print("Overall Average Marks:", overall_avg, "\n")

#-----------line plot of total number-------------------
x= df['Name']
y= df['Total']
plt.plot(x,y)
plt.savefig('stock.png')
plt.show()
#---line plot of maths marks
x= df['Name']
y= df['Maths']
plt.plot(x,y)
plt.savefig('stock.png')
plt.show
#---line plot of science marks
x= df['Name']
y= df['Science']
plt.plot(x,y)
plt.savefig('stock.png')
plt.show
#---line plot of english marks
x= df['Name']
y= df['English']
plt.plot(x,y)
plt.savefig('stock.png')
plt.show
# ---------- Bar Chart for Subject-wise Marks ----------
df.plot(x='Name', y=['Maths','Science','English'], kind='bar', figsize=(10,6))
plt.axhline(overall_avg, color='red', linestyle='--', label=f'Overall Avg = {overall_avg:.2f}')
plt.title("Student Marks in Different Subjects")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.show()

# ---------- Pie Chart for Attendance ----------
plt.figure(figsize=(6,6))
plt.pie(df['Attendance'], 
        labels=df['Name'], 
        autopct='%1.1f%%', 
        startangle=90)
plt.title("Student Attendance Distribution")
plt.show()
