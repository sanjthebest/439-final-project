import pandas as pd
import numpy as np
import random

# Set seeds for reproducibility
np.random.seed(42)
random.seed(42)

def generate_abortion_data(num_records=20000):
    """
    Generate synthetic abortion-related health data.
    """
    methods = ["Medical", "Surgical", "Other"]
    complications = ["None", "Hemorrhage", "Infection", "Uterine Perforation", "Anesthesia Reaction"]
    #ak
    complications_child = ["None", "Cleft lip or palate", "Down syndrome", "Premature birth", "Jaundice", "Birth asphyxia", "Congenital heart defects", "Intrauterine growth restriction (IUGR)", "Still Born", "Other"]
    relationship_status = ["Single", "Married", "Divorced", "Cohabitating", "Widowed"]
    race = ["Non-Hispanic White" , "Non-Hispanic Black", "Hispanic", "Asian", "Native American", "Pacific Islander", "Multiracial"]
    economic_status = ["Low Income", "Middle Income", "High Income", "Unemployed", "Underemployed" , "On government assistance"]
    Insurance = ["Private Insurance", "Public/Federal Insurance", "Uninsured", "Military Insurance", "Short-term Insurance", "Other"]
    
    data = {
        "Gestation_at_Abortion_Weeks": [],
        "Method_of_Abortion": [],
        "Travel_Out_of_State": [],
        "Abortion_Success": [],
        "Medical_Complications_to_Mother": [],
        "Medical_Complications_to_Child": [],
        "Age_of_Mother": [],
        "Relationship_Status": [],
        "Race": [],
        "Economic_Status": [],
        "Insurance": []
    }

    for _ in range(num_records):
        # Gestation: between 4 and 24 weeks, skewed toward earlier weeks
        gestation = round(np.random.normal(loc=10, scale=3), 1)
        gestation = max(4, min(24, gestation))  # Clamp to valid range

        # Method of abortion
        method = np.random.choice(methods, p=[0.6, 0.35, 0.05])

        # Travel out of state: more likely if gestation is later
        travel = np.random.rand() < (0.1 + 0.03 * (gestation - 4))

        # Abortion success: very high, slightly reduced with later gestation
        success_chance = 0.99 - (0.002 * (gestation - 4))
        success = np.random.rand() < success_chance

        # Complications: low overall, higher risk with later gestation and surgical method
        complication_chance = 0.02 + 0.01 * (gestation - 4)
        if method == "Surgical":
            complication_chance += 0.02

        has_complication = np.random.rand() < complication_chance
        complication = np.random.choice(complications[1:]) if has_complication else "None"

        #ak
        # Age of Mother
        mother_age = np.random.randint(12, 47)
        
        #complication of child if born
        complication_chance = 0.01 * (gestation - 4)  # Base chance based on gestation
        if mother_age >= 35:
            complication_chance += 0.03  # Increased risk for older mothers
        if gestation < 37:
            complication_chance += 0.05  # Increased risk for preterm births
        has_complication = np.random.rand() < complication_chance
        complication_child = np.random.choice(complications_child[1:]) if has_complication else "None"
        #complication_child = np.random.choice(complications_child)
        #Relationship staus
        rel_status = np.random.choice(relationship_status)
        #race
        race_choice = np.random.choice(race)
        #Economic Status
        econ_status = np.random.choice(economic_status)
        #Insurance
        insurance_choice = np.random.choice(Insurance)
        
        data["Gestation_at_Abortion_Weeks"].append(gestation)
        data["Method_of_Abortion"].append(method)
        data["Travel_Out_of_State"].append(travel)
        data["Abortion_Success"].append(success)
        data["Medical_Complications_to_Mother"].append(complication)
        data["Medical_Complications_to_Child"].append(complication_child)
        data["Age_of_Mother"].append(mother_age)
        data["Relationship_Status"].append(rel_status)
        data["Race"].append(race_choice)
        data["Economic_Status"].append(econ_status)
        data["Insurance"].append(insurance_choice)

    df = pd.DataFrame(data)
    return df

# Generate and save the data
df = generate_abortion_data(10000)
df.to_csv("synthetic_abortion_data.csv", index=False)

# Show sample and summary
print("Sample Data:")
print(df.head())

print("\nSummary:")
print(df.describe(include='all'))
