import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your unencoded CSV data
df = pd.read_csv('synthetic_abortion_data-2.csv')

# Filter data for each legal status
df_legal = df[df['Legal_Status_of_Abortion'] == 'Legal']
df_restricted = df[df['Legal_Status_of_Abortion'] == 'Restricted']
df_banned = df[df['Legal_Status_of_Abortion'] == 'Banned']

# Helper function to plot medical complications
def plot_medical_complications(df, legal_status, title):
    # Group by State Regulations and count occurrences of complications
    df_grouped = df.groupby(['State_Regulations', 'Medical_Complications_to_Mother', 'Medical_Complications_to_Child']).size().reset_index(name='Count')

    # Filter data for state regulation categories (High, Moderate, Low)
    df_grouped = df_grouped[df_grouped['State_Regulations'].isin(['High', 'Moderate', 'Low'])]

    # Plot a stacked bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='State_Regulations', y='Count', hue='Medical_Complications_to_Mother', data=df_grouped, palette='Set2', ci=None)
    plt.title(f'{title} - Medical Complications to Mother')
    plt.xlabel('State Regulations')
    plt.ylabel('Number of Cases')
    plt.legend(title='Complications to Mother', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='State_Regulations', y='Count', hue='Medical_Complications_to_Child', data=df_grouped, palette='Set2', ci=None)
    plt.title(f'{title} - Medical Complications to Child')
    plt.xlabel('State Regulations')
    plt.ylabel('Number of Cases')
    plt.legend(title='Complications to Child', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Plot graphs for Legal status
plot_medical_complications(df_legal, 'Legal', 'Medical Complications for Legal Status')

# Plot graphs for Restricted status
plot_medical_complications(df_restricted, 'Restricted', 'Medical Complications for Restricted Status')

# Plot a pie chart for Banned status, based on "Travel Out of State"
df_banned_grouped = df_banned.groupby(['Travel_Out_of_State', 'Medical_Complications_to_Mother', 'Medical_Complications_to_Child']).size().reset_index(name='Count')

# Pie chart for Travel Out of State when Legal Status is Banned
plt.figure(figsize=(8, 8))
df_banned_grouped_travel = df_banned_grouped.groupby('Travel_Out_of_State').size()
colors = ['#cdb4db', '#b5ead7']  # pastel purple and pastel green
df_banned_grouped_travel.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    labels=["No", "Yes"],
    colors=colors
)
plt.title('Travel Out of State When Abortion is Banned')
plt.ylabel('')  # Remove the y-label to make the pie chart cleaner
plt.show()