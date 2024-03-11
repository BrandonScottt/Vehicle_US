import streamlit as st
import pandas as pd
import plotly.express as px

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    
    df['is_4wd'] = df['is_4wd'].astype(bool)
    df['is_4wd'].fillna(False, inplace=True)
    
    df['paint_color'].fillna('unknown', inplace=True)
    
    df['cylinders'] = df.groupby('type')['cylinders'].transform(lambda x: x.fillna(x.median()))
    
    related_columns = ['model', 'type']
    
    df['model_year'] = df.groupby(related_columns)['model_year'].transform(lambda x: x.fillna(x.median()))
    df['odometer'] = df.groupby(related_columns)['odometer'].transform(lambda x: x.fillna(x.median()))
    
    df = df.dropna().reset_index(drop=True)
    
    df = df.astype({'model_year': int, 'odometer': int, 'cylinders': int})

    return df

def age_category(x):
    if x < 5:
        return '<5'
    elif x < 10:
        return '5-10'
    elif x < 20:
        return '10-20'
    else:
        return '>20'

def update_scatter_plot(x, y, color_type, df):
    scatter = px.scatter(df, x=x, y=y, color=color_type)
    scatter.update_layout(title="{} vs {}".format(y.capitalize(), x.capitalize()))
    st.plotly_chart(scatter)

def main():
    st.header("Vehicle US")
    st.write("This dashboard provides an interactive exploration of the Vehicle US dataset. It includes visualizations and insights to help understand key aspects of the dataset.")

    df = load_and_preprocess_data("vehicles_us.csv")

    st.write("Vehicle US - Dataset")
    st.write(df)

    #Filter
    st.sidebar.header("Filter data")
    selected_category = st.sidebar.selectbox("Select category", df["model"].unique())

    filtered_df = df[df["model"] == selected_category]

    fig = px.scatter(filtered_df, x="model_year", y="price", color="type")
    fig.update_layout(title="Price vs Model_year Graph")
    st.markdown("<b>Price vs Model_year Scatter Plot</b>: This scatter plot shows the relationship between the vehicle's model year and its price.", unsafe_allow_html=True)
    st.plotly_chart(fig)


    #Histogram
    hist_list =['transmission', 'condition', 'fuel', 'type', 'paint_color']
    hist_choice = st.selectbox('Split for price distribution', hist_list)

    hist = px.histogram(df, x="price", color=hist_choice, nbins=20)
    hist.update_layout(title="<b> Split of price by {}</b>".format(hist_choice))
    st.markdown("<b>Price Distribution Split by {}</b>: This histogram displays the distribution of prices based on the selected category.".format(hist_choice), unsafe_allow_html=True)
    st.plotly_chart(hist)

    #defining age categoty per car
    df['age']=2022-df['model_year']

    df['age_category']= df['age'].apply(age_category) 

    #scatter plot 
    list_for_scatter=['odometer','days_listed']

    choice_for_scatter = st.selectbox('Price dependency on ', list_for_scatter)

    fig = px.scatter(df, x="price", y=choice_for_scatter, color="age_category", hover_data=['model_year'])

    fig.update_layout(

    title="<b> price vs {}</b>".format(choice_for_scatter))
    st.markdown("<b>Price vs {} Scatter Plot</b>: This scatter plot shows the relationship between the vehicle's price and {}.".format(choice_for_scatter, choice_for_scatter), unsafe_allow_html=True)
    st.plotly_chart(fig)

    #Scatter plot with checkbox
    x = "model_year"
    y = "price"
    color_type = "type"



    checkbox = st.checkbox("Show data table")
    if checkbox:
        y = st.selectbox("Select y axis column", df.columns)
        x = st.selectbox("Select x axis column", df.columns)
        color_type = st.selectbox("Select Category", df.columns)

    update_scatter_plot(x, y, color_type, df)

if __name__ == "__main__":
    main()
