# IBM Inventory Demand Forecasting

This project aims to predict future product demand to optimize inventory levels using machine learning techniques. Accurate demand forecasting helps businesses maintain optimal stock levels, reduce holding costs, and improve customer satisfaction.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Modeling](#modeling)
- [Results](#results)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Effective inventory management is crucial for businesses to meet customer demand without overstocking. This project utilizes historical sales data to forecast future demand, enabling better inventory planning and management.

## Dataset

The dataset used in this project includes historical inventory data with the following features:

- `Date`: The date of the inventory record.
- `Product_ID`: Unique identifier for each product.
- `Warehouse`: Location of the product.
- `Quantity`: Number of units available.
- `Sales`: Number of units sold.

## Data Preprocessing

Data preprocessing steps include:

1. **Data Cleaning**: Handling missing values and correcting inconsistencies.
2. **Feature Engineering**: Creating new features such as moving averages and lag variables to capture trends and seasonality.
3. **Normalization**: Scaling numerical features to ensure model stability.

## Modeling

The project explores various machine learning models to forecast demand:

- **Linear Regression**: A baseline model to understand linear relationships.
- **Decision Trees**: To capture non-linear patterns in the data.
- **Random Forest**: An ensemble method to improve prediction accuracy.
- **XGBoost**: A gradient boosting technique for enhanced performance.

## Results

Model performance is evaluated using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). The results indicate that the [best-performing model] provides accurate demand forecasts, which can be utilized for effective inventory management.

## Usage

To replicate the analysis:

1. Clone the repository:
   bash
   git clone https://github.com/Sujalsurve/IBM-inventory-demand-forecasting.git
   cd IBM-inventory-demand-forecasting
   

2. Install the required dependencies:
   bash
   pip install -r requirements.txt
   

3. Run the Jupyter Notebook:
   bash
   jupyter notebook finalel.ipynb
   

Ensure you have the necessary data files (`inventory.csv` and `cleaned_inventory.csv`) in the project directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License

This project is licensed under the [MIT License](LICENSE).
