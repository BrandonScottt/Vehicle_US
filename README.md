# Vehicle_US Dashboard

This interactive dashboard allows users to explore the "Vehicle US" dataset, providing visualizations and insights into key aspects of the dataset related to vehicles being sold in the United States.

## Live Demo

Access the live demo of the Vehicle_US Dashboard hosted on Render: [Vehicle_US Dashboard](https://vehicle-us.onrender.com)

## Local Setup

To run the Vehicle_US Dashboard locally, follow these steps:

1. **Fork the Project:**
   - Fork this repository to your GitHub account.

2. **Clone the Repository:**
   - Clone the forked repository to your local machine:
     ```bash
     git clone https://github.com/your-username/Vehicle_US.git
     ```

3. **Install Dependencies:**
   - Navigate to the project directory:
     ```bash
     cd Vehicle_US
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Streamlit App:**
   - Execute the following command in your terminal:
     ```bash
     streamlit run app.py
     ```

5. **Access the Dashboard:**
   - Open your web browser and visit [http://localhost:10000](http://localhost:10000).

## Features

- **Data Visualizations:** Explore scatter plots, histograms, and other visualizations showcasing various aspects of the "Vehicle US" dataset.
- **Data Filtering:** Utilize the sidebar to filter data based on different vehicle categories.
- **Data Table Display:** Toggle the checkbox to view a data table along with scatter plots.

## Data Preprocessing

The data loading and preprocessing steps are handled in the `load_and_preprocess_data` function within the `app.py` file. The `age_category` function is used to categorize the age of vehicles.

## Usage

- Select different categories in the sidebar to filter data and view corresponding visualizations.
- Enable the checkbox to display a data table along with scatter plots.
