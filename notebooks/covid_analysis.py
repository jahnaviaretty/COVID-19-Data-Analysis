
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# 1. PROJECT SETUP
# ==========================================

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "covid_data.csv"
output_folder = project_folder / "reports"

output_folder.mkdir(exist_ok=True)

print("Loading COVID-19 dataset...")

df = pd.read_csv(file_path)
df["date"] = pd.to_datetime(df["date"])

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# ==========================================
# 2. INDIA COVID-19 DATA
# ==========================================

india_data = df[df["country"] == "India"].copy()
india_data = india_data.sort_values("date")

print("\n========== INDIA COVID-19 ANALYSIS ==========")
print("Total records:", len(india_data))

print("\nDate range:")
print(india_data["date"].min(), "to", india_data["date"].max())

print("\nLatest India records:")
print(
    india_data[
        ["date", "total_cases", "new_cases",
         "total_deaths", "new_deaths"]
    ].tail(10)
)


# ==========================================
# 3. GRAPH 1 - TOTAL COVID CASES IN INDIA
# ==========================================

cases_data = india_data.dropna(subset=["total_cases"])

plt.figure(figsize=(12, 6))
plt.plot(
    cases_data["date"],
    cases_data["total_cases"],
    label="Total Cases"
)

plt.title("Total COVID-19 Cases in India")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(output_folder / "india_covid_cases_trend.png", dpi=300)
plt.close()

print("\nGraph 1 completed!")


# ==========================================
# 4. GRAPH 2 - DAILY NEW CASES IN INDIA
# ==========================================

daily_cases = india_data.dropna(subset=["new_cases"])

plt.figure(figsize=(12, 6))
plt.plot(
    daily_cases["date"],
    daily_cases["new_cases"],
    label="Daily New Cases"
)

plt.title("Daily New COVID-19 Cases in India")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(output_folder / "india_daily_new_cases.png", dpi=300)
plt.close()

print("Graph 2 completed!")


# ==========================================
# 5. GRAPH 3 - TOTAL DEATHS IN INDIA
# ==========================================

deaths_data = india_data.dropna(subset=["total_deaths"])

plt.figure(figsize=(12, 6))
plt.plot(
    deaths_data["date"],
    deaths_data["total_deaths"],
    label="Total Deaths"
)

plt.title("Total COVID-19 Deaths in India")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(output_folder / "india_covid_deaths_trend.png", dpi=300)
plt.close()

print("Graph 3 completed!")


# ==========================================
# 6. GRAPH 4 - DAILY NEW DEATHS IN INDIA
# ==========================================

daily_deaths = india_data.dropna(subset=["new_deaths"])

plt.figure(figsize=(12, 6))
plt.plot(
    daily_deaths["date"],
    daily_deaths["new_deaths"],
    label="Daily New Deaths"
)

plt.title("Daily New COVID-19 Deaths in India")
plt.xlabel("Date")
plt.ylabel("New Deaths")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(output_folder / "india_daily_new_deaths.png", dpi=300)
plt.close()

print("Graph 4 completed!")


# ==========================================
# 7. GRAPH 5 - TOP 10 COUNTRIES BY CASES
# ==========================================

latest_data = (
    df.sort_values("date")
    .groupby("country")
    .tail(1)
)

latest_data = latest_data.dropna(subset=["total_cases"])

top_countries = latest_data.nlargest(10, "total_cases")

plt.figure(figsize=(12, 6))
plt.bar(
    top_countries["country"],
    top_countries["total_cases"]
)

plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y")
plt.tight_layout()

plt.savefig(output_folder / "top_10_countries_cases.png", dpi=300)
plt.close()

print("Graph 5 completed!")

print("\nTop 10 Countries:")
print(top_countries[["country", "total_cases"]])


# ==========================================
# 8. FINAL SUMMARY
# ==========================================

print("\n========== PROJECT SUMMARY ==========")

print("India total cases:",
      india_data["total_cases"].max())

print("India total deaths:",
      india_data["total_deaths"].max())

print("\nAll 5 graphs saved successfully!")
print("Check your reports folder.")

print("\nCOVID-19 DATA ANALYSIS COMPLETED!")



