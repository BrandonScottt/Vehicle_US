import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv("vehicles_us.csv")

df = df.dropna()

df = df.astype({'model_year': int, 'odometer': int, 'cylinders': int, 'is_4wd': int})
st.write(df)

st.header("""
   Vehicle US
""")
st.write("""
    #### <font color=red> testing st.write function
""", unsafe_allow_html=True)

#Filter
st.sidebar.header("Filter data")
selected_category = st.sidebar.selectbox("Select category", df["model"].unique())

filtered_df = df[df["model"] == selected_category]

fig = px.scatter(filtered_df, x="model_year", y="price", color="type")
fig.update_layout(title="Price vs Model_year Graph")
st.plotly_chart(fig)

st.markdown('<font color=red>Write descrption here</font>', unsafe_allow_html=True)

#Histogram
hist_list =['transmission', 'condition', 'fuel', 'type', 'paint_color']
hist_choice = st.selectbox('Split for price distribution', hist_list)

hist = px.histogram(df, x="price", color=hist_choice, nbins=20)
hist.update_layout(title="<b> Split of price by {}</b>".format(hist_choice))
st.plotly_chart(hist)

#scatter

#defining age categoty per car
df['age']=2022-df['model_year']

def age_category(x):

    if x<5: return '<5'

    elif x>=5 and x<10: return '5-10'

    elif x>=10 and x<20: return '10-20'

    else: return '>20'

df['age_category']= df['age'].apply(age_category) 

#scatter plot 
list_for_scatter=['odometer','days_listed']

choice_for_scatter = st.selectbox('Price dependency on ', list_for_scatter)

fig = px.scatter(df, x="price", y=choice_for_scatter, color="age_category", hover_data=['model_year'])

fig.update_layout(

title="<b> price vs {}</b>".format(choice_for_scatter))

st.plotly_chart(fig)

#Scatter plot with checkbox
x = "model_year"
y = "price"
color_type = "type"

def update_scatter_plot(x, y, color_type):
    scatter = px.scatter(df, x=x, y=y, color=color_type)
    scatter.update_layout(title="{} vs {}".format(y.capitalize(), x.capitalize()))
    st.plotly_chart(scatter)

checkbox = st.checkbox("Show data table")
if checkbox:
    y = st.selectbox("Select y axis column", df.columns)
    x = st.selectbox("Select x axis column", df.columns)
    color_type = st.selectbox("Select Category", df.columns)

update_scatter_plot(x, y, color_type)