import pandas as pd
import re 

class ChatBot:
    def __init__(self, file_path): 
        try:
            # Load CSV file into the pandas DataFrame
            self.df = pd.read_csv(file_path)
            self.file_path = file_path
            # Take the unique companies names and year from the CSV file and store into a list
            self.companies = self.df["Company"].unique().tolist()
            self.years = self.df["Year"].unique().tolist()
            # Set it to "none" so the chatbot doesn't crash and print an error message
        except FileNotFoundError:
            self.df = None
            self.file_path = None
            print(f"Error: File not found at {file_path}")

        # Ask the use for an input 
    def start(self):
        user_input = input("Ask me a question: ")
        result = self.process_user_input(user_input)
        # print(result) - use this for debbuging

        # Take the user input, proccess it, and extract relevant information (company, year, metric)
    def extract_company(self, user_input):
        # Convert user input to lowercase, and remove any extra spaces
        self.user_input = user_input.lower().strip() 

        # Check if company's name appears in the user's input
        for company in self.companies:
            match = re.search(company.lower(), self.user_input)
            if match:
                return str(match.group()).upper()
        return None # Return None if the company is not found

    def extract_year(self, user_input):
        self.user_input = user_input.lower().strip()
        # Use "re" formula to find a 4-digit year in the user input
        match = re.search(r'\d{4}', self.user_input)
        if match:
            return int(match.group()) # Convert the string to an integer and return it
        return None # Return None if the year is not found

    def extract_metric(self, user_input):
        self.user_input = user_input.lower().strip()
        # Dictionary mapping the metric names to column names in the CSV
        metrics = {
            "revenue": "Total Revenue",
            "net income": "Net Income",
            "total assets": "Total Assets",
            "total liabilities": "Total Liabilities",
            "cash flow from operating activities": "Cash Flow from Operating Activities"
        }

        # Check if metric is mentioned in the user's input
        for key, value in metrics.items():
            match = re.search(key.lower(), self.user_input)
            if match:
                return value
        return None

    def process_user_input(self, user_input):
        self.user_input = user_input.lower().strip()
        
        # Look for this information is in the user input
        company = self.extract_company(user_input)
        year = self.extract_year(user_input)
        metric = self.extract_metric(user_input)

        # Debugging print statements
        print(f"Extracted Company: {company}")
        print(f"Extracted Year: {year}")
        print(f"Extracted Metric: {metric}")

        # Handle cases of there is no match in the user input
        if not company:
            print("Sorry, I couldn't identify the company in your question.")
            return
        if not year:
            print("Sorry, I couldn't identify the year in your question.")
            return
        if not metric:
            print("Sorry, I couldn't identify the financial metric in your question.")
            return

        try:
            # Convert Year column to integer in case it's stored as a string
            self.df["Year"] = self.df["Year"].astype(int)

            # Get the value for the requested year
            current_value = self.df[(self.df["Company"] == company) & (self.df["Year"] == year)][metric].values

            # Get the value for the previous year
            previous_value = self.df[(self.df["Company"] == company) & (self.df["Year"] == (year - 1))][metric].values
           
            # Check if the data is available
            if current_value.size > 0:
                current_value = current_value[0]
                if previous_value.size > 0:
                    previous_value = previous_value[0]
                    change = current_value - previous_value
                    change_percentage = (change / previous_value) * 100 if previous_value != 0 else "N/A"

             # Print the  data and change details
                    print(f"In {year}, {metric} for {company} was {current_value}.")
                    print(f"In {year-1}, it was {previous_value}.")
                    print(f"The change is {change} ({change_percentage:.2f}% change).")
                else:
                    print(f"The {metric} for {company} in {year} is {current_value}, but no data is available for {year-1}.")
            else:
                print("Sorry, I couldn't find that data. Please check your query.")
            # Handle any errors that occur while retrieving the data
        except IndexError:
            print("An error occurred while retrieving the data. Please try again.")


# Create an instance of the ChatBot with a specified CSV file path
bot = ChatBot("/Users/agathasantos/data.csv")
bot.start()


# Examples of questions that the chatbot can answer: 

# 1. What was Apple's total revenue in 2022?
# 2. What is Microsoft's net income for 2023?
# 3. What is the cash flow from operating activities for Microsoft in 2022?
# 4. How did Microsoft's revenue change from 2023 to 2024?
# 5. What is the year-over-year change in Apple's net income for 2022 to 2023?
# 6. Tesla, Total Assets, 2024
  