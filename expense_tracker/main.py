import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

# Initializing variables ( like C )

# set page config
st.set_page_config(page_title="Simple Finance App",page_icon="💸", layout="wide")

# Our category file
category_file = "categories.json"

# Like useState()
if "categories" not in st.session_state:
    st.session_state.categories = {
        "Uncategorized": []
    }

# Create our json file if it doesn't exist
if os.path.exists("categories.json"):
    with open("categories.json", "r") as f:
        st.session_state.categories = json.load(f)
        
# save our categories
def save_categories():
    with open("categories.json", "w") as f:
        json.dump(st.session_state.categories, f)

# Keyword or transaction details associated with the categories
def add_keyword_to_category(category, keyword):
    keyword = keyword.strip()
    # If keyword is not inside of there, then we store it.
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    return False


# This function recives a df as an input and sets our new category and detail info.
def categorize_transactions(df):
    # Creates a new category column and set a default value
    df["Category"] = "Uncategorized"
    # Iterando sobre el diccionario key : value => category : keyword
    for category, keywords in st.session_state.categories.items():
        # Si la categoria es Uncategorized o no hay detalles, continua
        if category == "Uncategorized" or not keywords:
            continue
        # Cambia a minusculas  y elimina los espacios  para cada una de las keywords en el diccionario y las almacena en una lista
        lowered_keywords = [keyword.lower().strip() for keyword in keywords]
        # Iterate over each row in our df 
        for idx, row in df.iterrows():
            # Individual details of each row, lowercase and no spaces 
            details = row["Details"].lower().strip()
            # If details in lowered_keywords match with a particular category, we set the same category
            if details in lowered_keywords:
                # Update the category of that particular row in our df
                df.at[idx, "Category"] = category
                
    return df  


# Load a file
def load_csv_file(file):
    try:
        # Render csv data
        df = pd.read_csv(file)
        # Remove spaces from our columns
        df.columns = [col.strip() for col in df.columns]
        # Remove , and chage it´s value to "", and set float type.
        df['Amount'] = df['Amount'].str.replace("," , "").astype(float)
        # Change our csv date to a valid datetime
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")

        return categorize_transactions(df)
    
    except Exception as e:  
        st.error(f"Error processing file: {str(e)}")
        return None
    
    
# Our main function
def main():
    st.title("Simple Finance Dashboard")
    
    # Loads our cdv file
    upload_file = st.file_uploader("Upload your transaction CSV file", type=["csv"])
    if upload_file is not None:
        df = load_csv_file(upload_file)    
        
        # Create a separate columns for credit and debit
        if df is not None:
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()
            # add a copy to our session_state
            st.session_state.debits_df = debits_df.copy()
            
            # Create two additional tables
            tab1, tab2 = st.tabs(["Expeses (Debits)", "Payments (Credits)"])
            with tab1:
                # Create a text input, setting a placeholder.
                new_category = st.text_input("New Category Name")
                # Add a button, sets a label
                add_button = st.button("Add Category")
                # si el boton asta activo y se añadio una categoria...
                if add_button and new_category:
                    # Si la categoria añadida no esta en la session actual lo añade a la liesta y la guarda en el json file.
                    if new_category not in st.session_state.categories:
                        # Adds our new category to our session state
                        st.session_state.categories[new_category] = []
                        # Saves our categories to our JSON file
                        save_categories()
                        # Going to force to refresh the page
                        st.rerun()
                        
                st.subheader("Your Expenses")
                edited_df = st.data_editor(
                    # Put a list of the columns the we want to display
                    st.session_state.debits_df[["Date","Details","Amount","Category"]],
                    # How to display our columns
                    column_config={
                        "Date": st.column_config.DateColumn("Date", format="DD.MM.YYYY"),
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED"),
                        "Category": st.column_config.SelectboxColumn(
                            "Category",
                            # We can select from our categories
                            options=list(st.session_state.categories.keys())
                        )
                    },
                    # Use the entire width of the page
                    use_container_width=True,
                    hide_index=True,
                    # JUst to identify our df
                    key="category_editor"
                )
                
                # A new button, wen is triggered it update our categories
                save_button = st.button("Apply Changes", type="primary")
                # if button is triggered...
                if save_button:
                    # Itera en cada fila
                    for idx, row in edited_df.iterrows():
                        # Extrae la categoria de cada fila
                        new_category = row["Category"]
                        # If our new_category exist in our session state do nothing, else add the new category 
                        if new_category == st.session_state.debits_df.at[idx, "Category"]:
                            continue
                        details = row["Details"]
                        st.session_state.debits_df.at[idx, "Category"] = new_category
                        # save a category and it's associated details
                        add_keyword_to_category(new_category,details)
                # A new section using plotly
                st.subheader("Expense summary") 
                # From our debit_df, group by category and sum all the amount values in those groupings, then we reset the index
                category_totals = st.session_state.debits_df.groupby("Category")["Amount"].sum().reset_index()      
                # Sort it in descending order by the Amount
                category_totals = category_totals.sort_values("Amount", ascending=False)
                
                # A new Dataframe to show the category totals
                st.dataframe(
                    # Our DataFrame
                    category_totals,
                    # Setting a custom config
                    column_config={
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED")
                    },
                    use_container_width=True,
                    # Don't show our undex column
                    hide_index=True
                )
                
                # Plotly 
                
                fig = px.pie(
                    category_totals,
                    values="Amount",
                    names="Category",
                    title="Expenses by category"
                )
                
                st.plotly_chart(
                    fig,
                    use_container_width= True,
                )
                
            with tab2:
                st.subheader("Payments Summary")
                total_payments = credits_df["Amount"].sum()
                st.metric("Total Payments", f"{total_payments:,.2f} AED")
                st.write(credits_df)
                
            

main()   