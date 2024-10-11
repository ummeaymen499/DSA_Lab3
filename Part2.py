import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Train.csv')
test_data = pd.read_csv('Test.csv')
# Part 1 and 2
# df['TYPE'] = df['TYPE'].apply(lambda x: 1 if x == 'ALLERGY' else 0)

# symptoms = df.columns[:-1]  
# plt.figure(figsize=(15, 12))

# for i, symptom in enumerate(symptoms):
#     plt.subplot(5, 4, i + 1)
#     plt.scatter(df[symptom], df['TYPE'], alpha=0.5)
#     plt.title(symptom)
#     plt.xlabel(symptom)
#     plt.ylabel('Label (ALLERGY)')
#     plt.yticks([0, 1], ['No Allergy', 'Allergy'])
#     plt.xticks([0, 1])

# plt.tight_layout()
# plt.show()

# Part 3
symptoms = df.columns[:-1] 
def euclidean_distance(row1, row2):
    return np.sqrt(np.sum((row1 - row2) ** 2))

distances = []

for _, test_row in test_data.iterrows():
    row_distances = []
    for _, main_row in df.iterrows():
        distance = euclidean_distance(test_row[symptoms], main_row[symptoms])
        row_distances.append(distance)
    distances.append(row_distances)
distance_df = pd.DataFrame(distances, columns=df.index)
print(distance_df)

# Part 4
labels = df.columns[-1]
assigned_labels = []
   
    
closest_match_index = np.argmin(row_distances)
closest_label = df.iloc[closest_match_index][labels]
assigned_labels.append(closest_label)
test_data['Assigned_Label'] = assigned_labels
print(test_data)

#Part 6

symptoms = df.columns[:-1]
label_column = df.columns[-1]
part1 = df.copy()
part2 = df[symptoms]
print("Part 1 (with labels):")
print(part1.head())

print("\nPart 2 (without labels):")
print(part2.head())

part1.to_csv('part1_with_labels.csv', index=False)
part2.to_csv('part2_without_labels.csv', index=False)

# Part 7
part1 = pd.read_csv('part1_with_labels.csv')  
part2 = pd.read_csv('part2_without_labels.csv')  

features = part1.columns[:-1]  
labels = part1.columns[-1]  

assigned_labels = []

for index2, row2 in part2.iterrows():
    min_distance = float('inf')
    closest_label = None
    
    for index1, row1 in part1.iterrows():
        distance = np.sqrt(np.sum((row1[features] - row2[features]) ** 2))  
        
        if distance < min_distance:
            min_distance = distance
            closest_label = row1[labels]
    
    assigned_labels.append(closest_label)

true_labels = part1[labels].values  
correct_count = np.sum(true_labels == assigned_labels)
accuracy_percentage = (correct_count / len(part2)) * 100

print(f"Accuracy: {accuracy_percentage:.2f}% of correctly classified instances")

