import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(
    page_title="Streamlit Boilerplate",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #636363;
        text-align: center;
        margin-bottom: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 Streamlit Boilerplate Application</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">A starting template for your Streamlit projects</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Select a page:",
        ["Home", "Data Visualization", "Interactive Demo", "About"]
    )
    
    st.divider()
    
    # Add some sidebar widgets
    st.subheader("Settings")
    theme = st.selectbox("Choose theme:", ["Light", "Dark"])
    show_code = st.checkbox("Show code snippets", value=False)

# Main content based on page selection
if page == "Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Users", "1,234", "+12%")
    with col2:
        st.metric("Revenue", "$45,678", "-2.3%")
    with col3:
        st.metric("Performance", "98.5%", "+5.1%")
    
    st.divider()
    
    # Features section
    st.header("Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Data Visualization")
        st.write("Create beautiful and interactive charts with Plotly integration.")
        
        st.subheader("🔧 Easy Configuration")
        st.write("Simple setup and configuration for quick deployment.")
        
    with col2:
        st.subheader("🎨 Customizable UI")
        st.write("Flexible layout options and custom styling capabilities.")
        
        st.subheader("⚡ Real-time Updates")
        st.write("Automatic updates when data changes without page reload.")
    
    if show_code:
        st.code("""
# Example: Creating metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Users", "1,234", "+12%")
        """, language="python")

elif page == "Data Visualization":
    st.header("📊 Data Visualization Examples")
    
    # Generate sample data
    @st.cache_data
    def generate_data():
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
        data = pd.DataFrame({
            'date': dates,
            'sales': np.random.randn(len(dates)).cumsum() + 100,
            'customers': np.random.randint(50, 200, len(dates)),
            'category': np.random.choice(['A', 'B', 'C'], len(dates))
        })
        return data
    
    df = generate_data()
    
    # Tabs for different chart types
    tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Scatter Plot"])
    
    with tab1:
        fig = px.line(df, x='date', y='sales', title='Sales Over Time')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        monthly_sales = df.groupby(df['date'].dt.month)['sales'].mean().reset_index()
        monthly_sales['month'] = pd.to_datetime(monthly_sales['date'], format='%m').dt.month_name()
        fig = px.bar(monthly_sales, x='month', y='sales', title='Average Monthly Sales')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        fig = px.scatter(df, x='customers', y='sales', color='category', 
                        title='Sales vs Customers by Category')
        st.plotly_chart(fig, use_container_width=True)
    
    if show_code:
        st.code("""
# Generate sample data with caching
@st.cache_data
def generate_data():
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = pd.DataFrame({
        'date': dates,
        'sales': np.random.randn(len(dates)).cumsum() + 100,
        'customers': np.random.randint(50, 200, len(dates))
    })
    return data
        """, language="python")

elif page == "Interactive Demo":
    st.header("🎮 Interactive Demo")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("User Input Form")
        with st.form("user_form"):
            name = st.text_input("Name")
            age = st.slider("Age", 0, 100, 25)
            email = st.text_input("Email")
            interests = st.multiselect(
                "Interests",
                ["Technology", "Sports", "Music", "Art", "Travel", "Food"]
            )
            newsletter = st.checkbox("Subscribe to newsletter")
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                st.success(f"Thank you {name}! Your information has been submitted.")
    
    with col2:
        st.subheader("Live Preview")
        if name:
            st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        if email:
            st.write(f"**Email:** {email}")
        if interests:
            st.write(f"**Interests:** {', '.join(interests)}")
        st.write(f"**Newsletter:** {'Yes' if newsletter else 'No'}")
    
    st.divider()
    
    # File uploader demo
    st.subheader("File Upload Demo")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("File uploaded successfully!")
        st.dataframe(df.head())
        
        # Basic statistics
        st.subheader("Basic Statistics")
        st.write(df.describe())

elif page == "About":
    st.header("ℹ️ About This Application")
    
    st.markdown("""
    ### Welcome to the Streamlit Boilerplate!
    
    This application serves as a starting template for your Streamlit projects. 
    It includes common patterns and components that you might need:
    
    - **Multiple pages** with sidebar navigation
    - **Data visualization** examples using Plotly
    - **Interactive widgets** and forms
    - **Custom styling** with CSS
    - **Caching** for performance optimization
    - **File upload** functionality
    - **Responsive layout** with columns
    
    ### Getting Started
    
    1. Clone this repository
    2. Install dependencies: `pip install -r requirements.txt`
    3. Run the app: `streamlit run app.py`
    4. Start customizing for your needs!
    
    ### Tech Stack
    
    - **Streamlit** - The main framework
    - **Pandas** - Data manipulation
    - **NumPy** - Numerical operations
    - **Plotly** - Interactive visualizations
    
    ### Resources
    
    - [Streamlit Documentation](https://docs.streamlit.io)
    - [Streamlit Gallery](https://streamlit.io/gallery)
    - [Streamlit Components](https://streamlit.io/components)
    """)
    
    # Add some fun elements
    with st.expander("🎈 Fun Fact"):
        st.balloons()
        st.write("You found the hidden balloons! 🎉")

# Footer
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: #888;'>
        Made with ❤️ using Streamlit | 
        <a href='https://github.com/Adarsh-aot/streamlit-boilerplate' target='_blank'>GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)