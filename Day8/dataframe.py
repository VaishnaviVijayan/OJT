#import pandas as pd

# Convert file into dataframe
#df = pd.read_csv('air-pollution.csv')
#print(df.head())

# create filters based on country

#africa_df = df[df['Entity'] == 'Africa']
#print(africa_df)





# Mean, Median, Mode, SD and transfer into new columns
import pandas as pd

# Load your data into a DataFrame (replace 'your_file.csv' with your actual file path)
df = pd.read_csv('air-pollution.csv')

# Function to calculate and display statistics
def calculate_statistics(df):
    statistics = {}
    
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df['Nitrogen oxide (NOx)']):
            mean_value = df['Nitrogen oxide (NOx)'].mean()
            median_value = df['Nitrogen oxide (NOx)'].median()
            mode_value = df['Nitrogen oxide (NOx)'].mode()[0] if not df['Nitrogen oxide (NOx)'].mode().empty else None
            std_value = df['Nitrogen oxide (NOx)'].std()
            
            statistics['Nitrogen oxide (NOx)'] = {
                'mean': mean_value,
                'median': median_value,
                'mode': mode_value,
                'std': std_value
            }
    
      
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df['Sulphur dioxide (SO₂) emissions']):
            mean_value = df['Sulphur dioxide (SO₂) emissions'].mean()
            median_value = df['Sulphur dioxide (SO₂) emissions'].median()
            mode_value = df['Sulphur dioxide (SO₂) emissions'].mode()[0] if not df['Sulphur dioxide (SO₂) emissions'].mode().empty else None
            std_value = df['Sulphur dioxide (SO₂) emissions'].std()
            
            statistics['Sulphur dioxide (SO₂) emissions'] = {
                'mean': mean_value,
                'median': median_value,
                'mode': mode_value,
                'std': std_value
            }
              
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df['Carbon monoxide (CO) emissions']):
            mean_value = df['Carbon monoxide (CO) emissions'].mean()
            median_value = df['Carbon monoxide (CO) emissions'].median()
            mode_value = df['Carbon monoxide (CO) emissions'].mode()[0] if not df['Carbon monoxide (CO) emissions'].mode().empty else None
            std_value = df['Carbon monoxide (CO) emissions'].std()
            
            statistics['Carbon monoxide (CO) emissions'] = {
                'mean': mean_value,
                'median': median_value,
                'mode': mode_value,
                'std': std_value
            }
              
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df['Organic carbon (OC) emissions']):
            mean_value = df['Organic carbon (OC) emissions'].mean()
            median_value = df['Organic carbon (OC) emissions'].median()
            mode_value = df['Organic carbon (OC) emissions'].mode()[0] if not df['Organic carbon (OC) emissions'].mode().empty else None
            std_value = df['Organic carbon (OC) emissions'].std()
            
            statistics['Organic carbon (OC) emissions'] = {
                'mean': mean_value,
                'median': median_value,
                'mode': mode_value,
                'std': std_value
            }
              
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df['Non-methane volatile organic compounds emissions']):
            mean_value = df['Non-methane volatile organic compounds emissions'].mean()
            median_value = df['Non-methane volatile organic compounds emissions'].median()
            mode_value = df['Non-methane volatile organic compounds emissions'].mode()[0] if not df['Non-methane volatile organic compounds emissions'].mode().empty else None
            std_value = df['Non-methane volatile organic compounds emissions'].std()
            
            statistics['Non-methane volatile organic compounds emissions'] = {
                'mean': mean_value,
                'median': median_value,
                'mode': mode_value,
                'std': std_value
            }
            
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df['Black carbon (BC) emissions']):
            mean_value = df['Black carbon (BC) emissions'].mean()
            median_value = df['Black carbon (BC) emissions'].median()
            mode_value = df['Black carbon (BC) emissions'].mode()[0] if not df['Black carbon (BC) emissions'].mode().empty else None
            std_value = df['Black carbon (BC) emissions'].std()
            
            statistics['Black carbon (BC) emissions'] = {
                'mean': mean_value,
                'median': median_value,
                'mode': mode_value,
                'std': std_value
            }
                 
                  
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df['Ammonia (NH₃) emissions']):
            mean_value = df['Ammonia (NH₃) emissions'].mean()
            median_value = df['Ammonia (NH₃) emissions'].median()
            mode_value = df['Ammonia (NH₃) emissions'].mode()[0] if not df['Ammonia (NH₃) emissions'].mode().empty else None
            std_value = df['Ammonia (NH₃) emissions'].std()
            
            statistics['Ammonia (NH₃) emissions'] = {
                'mean': mean_value,
                'median': median_value,
                'mode': mode_value,
                'std': std_value
            }       
            
    # Convert statistics dictionary to DataFrame for better visualization
    stats_df = pd.DataFrame(statistics).T

    print(stats_df)

# Call the function
calculate_statistics(df)


 

