import pandas as pd
import webbrowser
import time

def open_links_in_chrome(file_path: str, sheet_name: str, column_name: str):
    # Load the Excel file
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    # Check if the column exists
    if column_name not in df.columns:
        print(f"The column '{column_name}' was not found in the Excel sheet.")
        return

    # Filter out any non-string or NaN values
    links = df[column_name].dropna().astype(str)

    # Open each link in a new tab in Chrome
    for link in links:
        if link.startswith("http"):
            webbrowser.open_new_tab(link)
            time.sleep(0.5)  # Small delay to prevent issues with opening too many tabs at once

if __name__ == "__main__":
    # Provide the path to your Excel file
    file_path = "Careers Links.xlsx"  # Replace with your file path
    sheet_name = "Sheet1"  # Replace with the name of your sheet
    column_name = "Careers Page link"  # Replace with the name of your column containing URLs

    open_links_in_chrome(file_path, sheet_name, column_name)
