# 🚀 Streamlit Boilerplate

A comprehensive boilerplate template for building Streamlit applications with best practices and common patterns.

## 📋 Features

- **Multi-page Navigation** - Sidebar navigation for multiple pages
- **Data Visualization** - Interactive charts using Plotly
- **Responsive Layout** - Mobile-friendly column layouts
- **Custom Styling** - CSS customization examples
- **Interactive Widgets** - Forms, sliders, file uploaders, and more
- **Performance Optimization** - Built-in caching for data processing
- **Modern UI Components** - Metrics, tabs, expanders, and containers

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/Adarsh-aot/streamlit-boilerplate.git
cd streamlit-boilerplate
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`.

## 📁 Project Structure

```
streamlit-boilerplate/
│
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── .gitignore         # Git ignore file
└── config.toml        # Streamlit configuration (optional)
```

## 🎨 Customization

### Adding New Pages

To add a new page, simply add a new condition in the main content section:

```python
elif page == "Your New Page":
    st.header("Your New Page")
    # Your page content here
```

### Modifying Styles

Custom CSS can be added in the style section at the beginning of `app.py`:

```python
st.markdown("""
<style>
    .your-custom-class {
        /* Your styles here */
    }
</style>
""", unsafe_allow_html=True)
```

### Adding New Visualizations

Use Plotly Express for creating interactive charts:

```python
import plotly.express as px

fig = px.line(df, x='x_column', y='y_column', title='Your Chart Title')
st.plotly_chart(fig, use_container_width=True)
```

## 📦 Dependencies

- **streamlit** - The core framework
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **plotly** - Interactive visualizations
- **python-dotenv** - Environment variable management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🌟 Acknowledgments

- Streamlit team for creating an amazing framework
- The open-source community for continuous inspiration

## 📞 Contact

Adarsh Ajay - [@Adarsh-aot](https://github.com/Adarsh-aot)

Project Link: [https://github.com/Adarsh-aot/streamlit-boilerplate](https://github.com/Adarsh-aot/streamlit-boilerplate)

---

Made with ❤️ by Adarsh Ajay