# Financial Analysis Chatbot

This project is a chatbot that analyzes and provides insights into financial data from a CSV file.  It allows users to ask questions about company financial metrics (revenue, net income, assets, liabilities, and cash flow) for specific years.

**Project Overview**

This project involves two main components:

1.  **Financial Data Analysis:** A preliminary analysis of the financial data was conducted using Python and the `pandas` library.
2.  **Chatbot Application:** A Python-based chatbot that enables users to query the financial data based on company, year, and metric.

**1. Financial Data Analysis**

The financial data analysis, documented in the "Financial_Analysis.pdf" file, involved the following steps:

* **Data Extraction:** Financial figures for Microsoft, Apple, and Tesla were extracted from their 10-K filings on the SEC's EDGAR database for the past three fiscal years. The following metrics were extracted: Total Revenue, Net Income, Total Assets, Total Liabilities, and Cash Flow from Operating Activities.
* **Data Organization:** The extracted data was organized into an Excel spreadsheet and saved as a CSV file ("Financial_Data Analysis.csv").
* **Year-over-Year Percentage Change Calculation:** Python and `pandas` were used to calculate the year-over-year percentage change for each financial metric using the formula: Percentage Change = ((New Value - Old Value) / Old Value) \* 100.
* **Trend Analysis:** The analysis focused on the trends from 2023 to 2024, as 2022 data contained NaN values. Key findings from the analysis include:
    * Microsoft:  Revenue, Net Income, Total Assets, Total Liabilities and Cash Flow from Operating Activities all increased from 2023 to 2024.
    * Apple: Revenue, Total Liabilities, Total  Assets and Cash Flow from Operating Activities increased from 2023 to 2024, while Net Income decreased.
    * Tesla: Revenue, Total Liabilities, Total Assets, and Cash Flow from Operating Activities increased from 2023 to 2024, while Net Income decreased.

**2. Chatbot Application**

The chatbot application, implemented in "ChatBot.py", provides a user-friendly way to interact with the financial data.

## Features

-   **Data Loading:** Loads financial data from a CSV file using pandas.
-   **Natural Language Processing (NLP):** Extracts company names, years, and financial metrics from user input using regular expressions.
-   **Data Retrieval:** Retrieves and displays financial data for a specified company and year.
-   **Year-over-Year Change Calculation:** Calculates and displays the change and percentage change in financial metrics between two consecutive years.
-   **Error Handling:** Handles file not found errors and data retrieval errors.
-   **User-Friendly Interaction:** Interacts with the user via simple command-line prompts.

## Usage

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

2.  **Ensure you have a CSV file named `data.csv` in the same directory as the python file, or change the file path in the code.** The CSV file should have the following columns: `Company`, `Year`, `Total Revenue`, `Net Income`, `Total Assets`, `Total Liabilities`, and `Cash Flow from Operating Activities`.
3.  **Run the script:**

    ```bash
    python chatbot.py
    ```

4.  **Ask questions in natural language:**

- What was Apple's total revenue in 2022?
- What is Microsoft's net income for 2023?
- What is the cash flow from operating activities for Microsoft in 2022?
- How did Microsoft's revenue change from 2023 to 2024?
- What is the year-over-year change in Apple's net income for 2022 to 2023?
- Tesla, Total Assets, 2024

## Requirements

-   Python 3.x
-   pandas
-   re (regular expressions)

## Installation

```bash
pip install pandas
