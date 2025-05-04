import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Load encoded dataset
df_encoded = pd.read_csv('encoded_abortion_data.csv')

# Define relevant predictors (excluding 'Banned')
predictors = [
    'State_Regulations_High',
    'State_Regulations_Moderate',
    'State_Regulations_Low'
]

# Add constant for intercept
X = sm.add_constant(df_encoded[predictors])

# Define all mother complication columns
mother_cols = [
    'Medical_Complications_to_Mother_Anesthesia Reaction',
    'Medical_Complications_to_Mother_Hemorrhage',
    'Medical_Complications_to_Mother_Infection',
    'Medical_Complications_to_Mother_Uterine Perforation'
]

# Define all child complication columns
child_cols = [
    'Medical_Complications_to_Child_Birth asphyxia',
    'Medical_Complications_to_Child_Cleft lip or palate',
    'Medical_Complications_to_Child_Congenital heart defects',
    'Medical_Complications_to_Child_Down syndrome',
    'Medical_Complications_to_Child_Intrauterine growth restriction (IUGR)',
    'Medical_Complications_to_Child_Jaundice',
    'Medical_Complications_to_Child_Other',
    'Medical_Complications_to_Child_Premature birth',
    'Medical_Complications_to_Child_Still Born'
]

# Combine complication columns into binary outcome: 1 if any complication, else 0
y_mother = df_encoded[mother_cols].sum(axis=1).apply(lambda x: 1 if x > 0 else 0)
y_child = df_encoded[child_cols].sum(axis=1).apply(lambda x: 1 if x > 0 else 0)

# Fix data types
X = X.astype(float)
y_mother = y_mother.astype(float)
y_child = y_child.astype(float)

# Fit GLM models
model_mother = sm.GLM(y_mother, X, family=sm.families.Binomial()).fit()
print("=== GLM Results: Complications to Mother ===")
print(model_mother.summary())

model_child = sm.GLM(y_child, X, family=sm.families.Binomial()).fit()
print("\n=== GLM Results: Complications to Child ===")
print(model_child.summary())

# Prepare coefficients for visualization
coef_df = pd.DataFrame({
    'Predictor': predictors,
    'Mother Complications': model_mother.params[predictors],
    'Child Complications': model_child.params[predictors]
})

# Rename predictors for better axis labels
label_mapping = {
    'State_Regulations_High': 'State Reg-High',
    'State_Regulations_Moderate': 'State Reg-Moderate',
    'State_Regulations_Low': 'State Reg-Low'
}
coef_df['Predictor Label'] = coef_df['Predictor'].map(label_mapping)

# Plot
plt.figure(figsize=(10, 6))
bar_plot = coef_df.set_index('Predictor Label')[['Mother Complications', 'Child Complications']].plot(
    kind='bar',
    color=['#FFB347', '#C71585'],  # pastel orange and dark pink
    figsize=(10, 6)
)
plt.title('GLM Coefficients: State Regulations vs. Medical Complications')
plt.ylabel('Coefficient Value')
plt.xlabel('Predictor')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.xticks(rotation=0)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Move legend outside
plt.legend(["Mother Complications", "Child Complications"], title="Outcome", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Predict probabilities
y_mother_pred = model_mother.predict(X)
y_child_pred = model_child.predict(X)

# Plot predicted probabilities vs actual for mother complications
plt.figure(figsize=(10, 5))

# Mother subplot
plt.subplot(1, 2, 1)
sns.scatterplot(x=y_mother_pred, y=y_mother, alpha=0.4)
sns.lineplot(x=[0, 1], y=[0, 1], color='red', linestyle='--')
plt.title("GLM: Predicted vs Actual (Mother)")
plt.xlabel("Predicted Probability")
plt.ylabel("Actual Outcome")
plt.grid(True)

# Child subplot
plt.subplot(1, 2, 2)
sns.scatterplot(x=y_child_pred, y=y_child, alpha=0.4)
sns.lineplot(x=[0, 1], y=[0, 1], color='red', linestyle='--')
plt.title("GLM: Predicted vs Actual (Child)")
plt.xlabel("Predicted Probability")
plt.ylabel("Actual Outcome")
plt.grid(True)

plt.tight_layout()
plt.show()