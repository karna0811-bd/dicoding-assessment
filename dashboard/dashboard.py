import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#get data
most_soldyear = pd.read_csv("most_sold_items_by_year.csv")
dfyear = pd.DataFrame(most_soldyear)
most_soldmonthly = pd.read_csv("most_sold_items_by_month.csv")
dfmonth = pd.DataFrame(most_soldmonthly)
payment = pd.read_csv("payments_type.csv")
payment_type_df = pd.DataFrame(payment) 

st.title('Sales Dashboard')
# Tabs
tabs = st.tabs(["Data Table", "Items Sold Chart", "Payment Methode Used Chart"])



    

# Set page title

with tabs[1]:
    st.subheader("Most sold items by Year")

    plt.figure(figsize=(10, 6))
    plt.bar(dfyear['year'].astype(str) + ' - ' + dfyear['product_category_name_english'], dfyear['total_count'], color='skyblue')
    plt.xlabel('Year - Product Category')
    plt.ylabel('Total Count')
    plt.title('Most Sold Product Category Each Year')
    #plt.show()
    st.pyplot(plt)

    st.subheader("Most sold items by Month-Year")
    
    # Create a bar chart
    plt.figure(figsize=(12, 8))
    bar_plot = plt.bar(dfmonth['month'].astype(str) + ' - ' + dfmonth['product_category_name_english'], dfmonth['total_count'], color='skyblue')

    # Format x-axis ticks and labels for better readability
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Month - Product Category')
    plt.ylabel('Total Count')
    plt.title('Most Sold Product Category Each Month - Year')

    # Add data labels on top of the bars
    for bar in bar_plot:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    plt.tight_layout()
    #plt.show()
    st.pyplot(plt)

# Add a sidebar
st.sidebar.header('Filter Options')
# Add filter widgets to the sidebar (customize as needed)
# selected_year = st.sidebar.selectbox('Select Year', dfyear['year'].unique(), index=0)  # Set default to the first year
# selected_category = st.sidebar.selectbox('Select Category', dfyear['product_category_name_english'].unique(), index=0)  # Set default to the first category

selected_data = st.sidebar.radio('Select Data Type', ['Yearly', 'Monthly'])

if selected_data == 'Yearly':
    df_selected = dfyear
    filter_column = 'year'
else:
    df_selected = dfmonth
    filter_column = 'month'

selected_filter = st.sidebar.selectbox(f'Select {filter_column.capitalize()}', df_selected[filter_column].unique(),index=0) 
selected_category = st.sidebar.selectbox('Select Category', df_selected['product_category_name_english'].unique(), index=0)

# Filter the DataFrame based on user selection
filtered_df = filtered_df = df_selected[(df_selected[filter_column] == selected_filter) &
                           (df_selected['product_category_name_english'] == selected_category)]
# Rename the column for display

if selected_data == 'Yearly':
    filtered_df = df_selected.rename(columns={'product_category_name_english': 'Product Name','year' :'Year','total_count':'Total Items Sold'})
else:
    filtered_df = df_selected.rename(columns={'product_category_name_english': 'Product Name','month':'Month-Year','total_count':'Total Items Sold'})

with tabs[0]:
# Display the filtered data

    if selected_data == 'Yearly':
        st.write(f"## Data for {selected_filter} - {selected_category} Category")
        st.write(filtered_df[['Year','Product Name','Total Items Sold']])
    else:
        st.write(f"## Data for {selected_filter} - {selected_category} Category ")
        st.write(filtered_df[['Month-Year','Product Name','Total Items Sold']])

with tabs[2]:
        # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(payment_type_df['count'], labels=payment_type_df['payment_type'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Payment Methods')

    # Show the plot
    #plt.show()
    st.pyplot(plt)