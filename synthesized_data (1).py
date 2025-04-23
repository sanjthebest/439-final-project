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
    num_years = list(range(2014, 2025)) #Aarti
    state_info = {
    "Alabama": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2019 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Alaska": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "Arizona": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Restricted", "Regulation_Level": "High"} if year < 2024 else
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"}
            ) for year in range(2014, 2025)
        }
    },
    "Arkansas": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "California": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "Colorado": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "Connecticut": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "Delaware": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2017 else
                {"Legal_Status": "Legal", "Regulation_Level": "Low"}
            ) for year in range(2014, 2025)
        }
    },
    "Florida": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2023 else
                {"Legal_Status": "Restricted", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Georgia": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2022 else
                {"Legal_Status": "Restricted", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
     "Hawaii": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "Idaho": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Illinois": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "Indiana": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Iowa": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2023 else
                {"Legal_Status": "Restricted", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Kansas": {
        "Political_Affiliation": "Mixed",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} for year in range(2014, 2025)
        }
    },
    "Kentucky": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Louisiana": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Maine": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Low"} if year >= 2023 else
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"}
            ) for year in range(2014, 2025)
        }
    },
    "Maryland": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2022 else
                {"Legal_Status": "Legal", "Regulation_Level": "Low"}
            ) for year in range(2014, 2025)
        }
    },
    "Massachusetts": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Low"} if year >= 2020 else
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"}
            ) for year in range(2014, 2025)
        }
    },
    "Michigan": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2022 else
                {"Legal_Status": "Legal", "Regulation_Level": "Low"}
            ) for year in range(2014, 2025)
        }
    },
    "Minnesota": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "Mississippi": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Missouri": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Banned", "Regulation_Level": "High"} if year < 2024 else
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"}
            ) for year in range(2014, 2025)
        }
    },
     "Montana": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} for year in range(2014, 2025)
        }
    },
    "Nebraska": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2024 else
                {"Legal_Status": "Restricted", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Nevada": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} for year in range(2014, 2025)
        }
    },
    "New Hampshire": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2022 else
                {"Legal_Status": "Restricted", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "New Jersey": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "New Mexico": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "New York": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "North Carolina": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2023 else
                {"Legal_Status": "Restricted", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
     "North Dakota": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Banned", "Regulation_Level": "High"} if year < 2024 else
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"}
            ) for year in range(2014, 2025)
        }
    },
    "Ohio": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year == 2022 else
                {"Legal_Status": "Legal", "Regulation_Level": "Low"}
            ) for year in range(2014, 2025)
        }
    },
    "Oklahoma": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Banned", "Regulation_Level": "High"} for year in range(2014, 2025)
        }
    },
    "Oregon": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "Pennsylvania": {
        "Political_Affiliation": "Mixed",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} for year in range(2014, 2025)
        }
    },
    "Rhode Island": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Low"} if year >= 2019 else
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"}
            ) for year in range(2014, 2025)
        }
    },
    "South Carolina": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2021 else
                {"Legal_Status": "Restricted", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "South Dakota": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Banned", "Regulation_Level": "High"} for year in range(2014, 2025)
        }
    },
    "Tennessee": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Texas": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Restricted", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Utah": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Restricted", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Vermont": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
    "Virginia": {
        "Political_Affiliation": "Mixed",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2020 else
                {"Legal_Status": "Legal", "Regulation_Level": "Low"}
            ) for year in range(2014, 2025)
        }
    },
    "Washington": {
        "Political_Affiliation": "Democratic",
        "Abortion_Laws_By_Year": {
            year: {"Legal_Status": "Legal", "Regulation_Level": "Low"} for year in range(2014, 2025)
        }
    },
     "West Virginia": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    },
    "Wisconsin": {
        "Political_Affiliation": "Mixed",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "High"} if year < 2022 else
                {"Legal_Status": "Banned", "Regulation_Level": "High"} if year < 2023 else
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"}
            ) for year in range(2014, 2025)
        }
    },
    "Wyoming": {
        "Political_Affiliation": "Republican",
        "Abortion_Laws_By_Year": {
            year: (
                {"Legal_Status": "Legal", "Regulation_Level": "Moderate"} if year < 2022 else
                {"Legal_Status": "Restricted", "Regulation_Level": "High"}
            ) for year in range(2014, 2025)
        }
    }    
}

    
    
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
        "Insurance": [],
        "Year": [],
        "State":[],
        "Political_Affiliation_of_State":[],
        "Legal_Status_of_Abortion":[],
        "State_Regulations":[]
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
        
        #Aarti
        state_choice = np.random.choice(list(state_info.keys()))
        year = np.random.choice(num_years)

        state_metadata = state_info[state_choice]
        political_affiliation = state_metadata["Political_Affiliation"]
        legal_status = state_metadata["Abortion_Laws_By_Year"][year]["Legal_Status"]
        regulation_level = state_metadata["Abortion_Laws_By_Year"][year]["Regulation_Level"]
        
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
        data["Year"].append(year) #Aarti
        data["State"].append(state_choice)
        data["Political_Affiliation_of_State"].append(political_affiliation)
        data["Legal_Status_of_Abortion"].append(legal_status)
        data["State_Regulation"].append(regulation_level)

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
