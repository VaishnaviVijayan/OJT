import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv('sample_dataset.csv')

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Generate summary statistics
summary_stats = df.describe()
mean_sepal_length = summary_stats.loc['mean', 'Sepal Length (cm)']
std_sepal_length = summary_stats.loc['std', 'Sepal Length (cm)']
print("\nSummary statistics:")
print(summary_stats)
print(f"\nMean Sepal Length: {mean_sepal_length}")
print(f"Standard Deviation of Sepal Length: {std_sepal_length}")

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values in the dataset:")
print(missing_values)

# Convert species labels to numerical values
mapping = {'FlowerA': 0, 'FlowerB': 1, 'FlowerC': 2}
df['Species'] = df['Species'].map(mapping)
print("\nDataset with numerical species labels:")
print(df.head())

# Split the dataset into training and testing sets
X = df.drop(columns=['Species'])
y = df['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
print("\nShapes of training and testing sets:")
print(f"X_train: {X_train.shape}, X_test: {X_test.shape}, y_train: {y_train.shape}, y_test: {y_test.shape}")

# Train a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Visualize the trained decision tree using matplotlib
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=X.columns, class_names=['FlowerA', 'FlowerB', 'FlowerC'], filled=True)
plt.savefig('decision_tree.png')
plt.show()
print("\nDecision tree visualization saved as 'decision_tree.png'")

# Predict the species for the testing data and compute the accuracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy}")

# Generate a classification report and a confusion matrix
class_report = classification_report(y_test, y_pred, target_names=['FlowerA', 'FlowerB', 'FlowerC'])
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nClassification report:")
print(class_report)
print("\nConfusion matrix:")
print(conf_matrix)
