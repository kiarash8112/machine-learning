import pandas as pd

# Load the dataset
file_path = 'student-dataset.csv'
df = pd.read_csv(file_path)


# Group by 'portfolio.rating' and calculate mean and variance for the relevant grade columns
grouped_df = df.groupby('portfolio.rating')[['english.grade', 'math.grade', 'sciences.grade', 'language.grade']]

# Calculate mean and variance
mean_df = grouped_df.mean().reset_index()
variance_df = grouped_df.var().reset_index()

# Rename the columns for clarity
mean_df.columns = ['portfolio.rating', 'english.mean', 'math.mean', 'sciences.mean', 'language.mean']
variance_df.columns = ['portfolio.rating', 'english.variance', 'math.variance', 'sciences.variance', 'language.variance']

# Merge the mean and variance dataframes
result_df = pd.merge(mean_df, variance_df, on='portfolio.rating')

# Append the mean and variance as rows at the bottom of the dataset
final_df = pd.concat([df, result_df], ignore_index=True)

# Show the final dataframe with mean and variance added
final_df.tail(10) # Display the last 10 rows to include the added statistics
    