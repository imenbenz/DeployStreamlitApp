import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("graphs with streamlit")

# Slider to adjust the number of bars
num_bars = st.slider("Number of bars", min_value=1, max_value=10, value=4)
values = np.random.randint(1, 10, size=num_bars)
categories = [f'Category {i}' for i in range(1, num_bars + 1)]

# Bar plot with adjustable bars
fig, ax = plt.subplots()
ax.bar(categories, values, color='skyblue')
ax.set_title("Bar Plot with Adjustable Bars")
ax.set_xlabel("Categories")
ax.set_ylabel("Values")

# Display the plot in Streamlit
st.pyplot(fig)


st.title("Bar Plot Example!")
# Example data for bar plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

# Create a bar plot
fig, ax = plt.subplots()
ax.bar(categories, values, color='skyblue')
ax.set_title("Bar Plot")
ax.set_xlabel("Categories")
ax.set_ylabel("Values")

# Display the plot in Streamlit
st.pyplot(fig)



import seaborn as sns
import pandas as pd

# Example data for Seaborn bar plot
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [3, 7, 2, 5]
})

# Create the bar plot with Seaborn
fig, ax = plt.subplots()
sns.barplot(x='Category', y='Value', data=data, palette='pastel', ax=ax)
ax.set_title("Seaborn Bar Plot")

# Display the plot in Streamlit
st.pyplot(fig)



import plotly.graph_objects as go

st.title("Interactive Bar Plot Example!")
# Example data for bar plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

# Create an interactive bar plot with Plotly
fig = go.Figure(data=[
    go.Bar(name="Values", x=categories, y=values, marker_color='skyblue')
])

# Add titles
fig.update_layout(
    title="Interactive Bar Plot",
    xaxis_title="Categories",
    yaxis_title="Values"
)

# Display the interactive plot in Streamlit
st.plotly_chart(fig)




st.title("Line Plot Example")
# Example data for line plot
x = np.linspace(0, 10, 100)  # 100 evenly spaced values from 0 to 10
y = np.sin(x)  # y values are the sine of x values

# Create a line plot
fig, ax = plt.subplots()
ax.plot(x, y, color='blue')
ax.set_title("Line Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Display the plot in Streamlit
st.pyplot(fig)


st.title("Scatter Plot Example")
# Example data for scatter plot
x = np.random.rand(50)
y = np.random.rand(50)

# Create a scatter plot
fig, ax = plt.subplots()
ax.scatter(x, y, color='purple')
ax.set_title("Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Display the plot in Streamlit
st.pyplot(fig)


import plotly.express as px

st.title("Interactive Scatter Plot with Plotly")

# Example data for scatter plot
x = np.random.rand(50)
y = np.random.rand(50)

# Create an interactive scatter plot with Plotly
fig = px.scatter(x=x, y=y, title="Scatter Plot", labels={"x": "X-axis", "y": "Y-axis"})
fig.update_traces(marker=dict(color="purple"))

# Display the interactive plot in Streamlit
st.plotly_chart(fig)

