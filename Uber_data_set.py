import pandas as pd

df = pd.read_csv(r"C:/Users/admin/OneDrive/Desktop/python/Uber_data_set.csv")

print(df)
df.isnull().sum()
print("check all date befoor clean data set")
print("\n------------------------------")
# Remove rows where Date is missing
df = df.dropna(subset=["Date"])

# Convert Excel serial date to datetime
df["Date"] = pd.to_datetime(
    df["Date"],
    origin="1899-12-30",
    unit="D"
)

#convert to object format into time format 
df["Time"] = pd.to_datetime(df["Time"],format = "%H:%M:%S")

# Handle numreic missing Values using for loop 
numreic_col = ["Avg VTAT", "Avg CTAT" , "Cancelled Rides by Customer", "Cancelled Rides by Driver",
               "Incomplete Rides","Booking Value","Ride Distance","Driver Ratings","Customer Rating"]

for col in numreic_col:
     df[col]= df[col].fillna('null')

#handling string missing values using for loop 
string_col = ["Reason for cancelling by Customer","Driver Cancellation Reason","Incomplete Rides Reason","Payment Method"]

for col in string_col:
    df[col] = df[col].fillna('null')

print(df.isnull().sum())


#check all duplicates value in the data frame
print("Duplicates:", df.duplicated().sum())

# 3.Remove duplicates
df = df.drop_duplicates()

#check empty rows in the dataframe
empty_rows = df.isnull().all(axis=1).sum()
print("Empty Rows:", empty_rows)


# 1. Remove completely empty rows
df = df.dropna(how="all")

# Check data types
print("\nData Types:")
print(df.dtypes)

df.to_csv(r"C:\Users\admin\OneDrive\Documents\Uber_Data_Cleaned.csv",index=False)

