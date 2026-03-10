# House Price Prediction Project

A machine learning web application that predicts house prices based on various features using Linear Regression. The project includes data preprocessing, model training, and an interactive Streamlit web interface.

## 📋 Project Overview

This project predicts house sale prices using a Linear Regression model trained on housing data. Users can input house features through an intuitive web interface and receive instant price predictions.

## ✨ Features

- **Interactive Web UI**: Built with Streamlit for easy user interaction
- **Linear Regression Model**: Trained on 8 key housing features
- **Real-time Predictions**: Instant price predictions based on user input
- **Data Preprocessing**: Complete pipeline for cleaning and encoding categorical variables
- **Model Persistence**: Trained model saved using pickle for quick deployment

## 📁 Project Structure

```
Task-1/
│
├── data.csv                    # Processed dataset (generated from notebook)
├── data_preprocessing.ipynb    # Jupyter notebook for data analysis and model training
├── data_description.txt        # Detailed description of all data features
├── prediction_ui.py           # Streamlit web application
├── requirements.txt           # Python dependencies
├── model.pkl                  # Trained Linear Regression model (generated)
└── README.md                  # Project documentation
```

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure you have the trained model file (`model.pkl`) in the project directory
   - If not present, run the `data_preprocessing.ipynb` notebook to generate it

## 🚀 Usage

### Running the Web Application

1. Navigate to the project directory:
```bash
cd path/to/Task-1
```

2. Launch the Streamlit application:
```bash
streamlit run prediction_ui.py
```

3. The application will open in your default web browser (usually at `http://localhost:8501`)

4. Enter house features in the form:
   - **Overall Quality** (1-10): Material and finish rating
   - **Above Grade Living Area** (sq ft): Living space above ground
   - **Garage Size** (0-5): Number of cars the garage can hold
   - **Total Basement Area** (sq ft): Total basement square footage
   - **Year Built**: Original construction year
   - **Neighborhood** (0-24): Encoded neighborhood value
   - **Lot Area** (sq ft): Total lot size
   - **Kitchen Quality**: Select from TA/Gd/Ex/Fa

5. Click "Predict House Price" to see the estimated price

### Training the Model

If you need to retrain the model:

1. Open `data_preprocessing.ipynb` in Jupyter Notebook or JupyterLab
2. Ensure `train.csv` is in the project directory
3. Run all cells sequentially
4. The notebook will:
   - Load and explore the data
   - Preprocess features (label encoding, mapping)
   - Split data into training and test sets
   - Train a Linear Regression model
   - Evaluate model performance
   - Save the model as `model.pkl`
   - Generate `data.csv` for reference

## 📊 Model Information

### Features Used (8 features)
1. **OverallQual**: Overall material and finish quality (1-10)
2. **GrLivArea**: Above grade living area (square feet)
3. **GarageCars**: Garage capacity (number of cars)
4. **TotalBsmtSF**: Total basement area (square feet)
5. **YearBuilt**: Original construction year
6. **Neighborhood**: Location (label encoded, 0-24)
7. **LotArea**: Lot size (square feet)
8. **KitchenQual**: Kitchen quality (encoded: TA=0, Gd=1, Ex=2, Fa=3)

### Target Variable
- **SalePrice**: House sale price in dollars

### Model Algorithm
- **Linear Regression**: Scikit-learn implementation

### Data Preprocessing
- **Neighborhood**: Label Encoding (converts categorical neighborhood names to numeric values 0-24)
- **KitchenQual**: Manual mapping (TA→0, Gd→1, Ex→2, Fa→3)
- **Train-Test Split**: 80% training, 20% testing (random_state=42)

### Model Performance
Model evaluation metrics are displayed in the preprocessing notebook:
- R² Score
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)

## 📦 Dependencies

```
streamlit      # Web application framework
pandas         # Data manipulation
numpy          # Numerical computing
scikit-learn   # Machine learning library
```

## 🔍 Data Description

The `data_description.txt` file contains comprehensive information about:
- MSSubClass, MSZoning, LotFrontage, LotArea
- Street, Alley, LotShape, LandContour
- Utilities, LotConfig, LandSlope
- Neighborhood definitions and codes
- And many more housing features

Refer to this file for detailed explanations of all available features.

## 💡 Usage Tips

1. **Neighborhood Encoding**: Since neighborhoods are label-encoded (0-24), refer to the data preprocessing notebook to see which number corresponds to which neighborhood.

2. **Reasonable Ranges**: 
   - Living Area: 300-10,000 sq ft
   - Lot Area: 1,000-50,000 sq ft
   - Year Built: 1800-2026
   - Garage: 0-5 cars

3. **Kitchen Quality Codes**:
   - TA: Typical/Average
   - Gd: Good
   - Ex: Excellent
   - Fa: Fair

## 🛠️ Future Enhancements

Potential improvements for this project:
- Add more features for improved prediction accuracy
- Implement feature engineering techniques
- Try different regression algorithms (Random Forest, XGBoost, etc.)
- Add data visualization in the UI
- Include confidence intervals for predictions
- Deploy to cloud platforms (Heroku, Streamlit Cloud, etc.)
- Add neighborhood name mapping for better UX
- Implement input validation and error handling

## 📝 Notes

- The model is trained on historical housing data
- Predictions are estimates and should be used as reference only
- Model accuracy depends on the quality and quantity of training data
- Ensure all input values are within reasonable ranges for best results

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available for educational purposes.

---

**Created as part of Tekworks Day-13 Task-1**
