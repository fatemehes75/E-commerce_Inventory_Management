# AI-Driven Inventory Management System with Demand Forecasting

The system is designed to help businesses optimize their restocking needs based on historical sales data. The platform enables businesses to forecast sales and make informed inventory decisions, thus ensuring stock levels are optimized and reducing both stockouts and overstocking.

# System Components:

1. Data Collection:

The system starts by gathering historical sales and inventory data from various sources, such as RESTful API for inventory and pricing.   
Data is collected from an external API (mockaroo.com), where historical sales and inventory data is fetched via a GET request.

2. Data Preprocessing:

After the data is collected, it undergoes thorough preprocessing to ensure the data is clean and ready for machine learning models.
The key steps in data preprocessing:
* Handling Missing Values
* Removing Duplicate Rows
* Fixing Column Types
* Outlier Detection
* Store the processed data in n to S3 bucket through API.

3. Exploratory Data Analysis (EDA):

The system performs various visualizations and statistical summaries on historical sales data to understand the relationships between sales, stock levels, and other factors. This includes:
* Time series analysis of sales over time.
* Distribution analysis of numerical variables like stock levels and sales.
* Correlation analysis to explore the relationship between stock levels and sales.


4. Model Development:

Machine learning models are used to forecast sales, allowing businesses to predict when and how much to restock.
The model uses historical data to understand patterns in sales and stock levels and provides recommendations for future stock orders.

5. Web Application (Flask):

The Flask-based web application allows users to input key data such as the current inventory levels and date for prediction. It then uses the trained machine learning model to predict sales and provide recommendations for restocking quantity.

**Final Thoughts:**
This system offers a robust solution for e-commerce businesses to predict sales and optimize their inventory management processes, thereby improving operational efficiency and enhancing customer satisfaction.


**Next Step**

Automation and Scheduling
* If you need to regularly fetch data from the API and store it in S3, consider setting up an automation pipeline with AWS Lambda and CloudWatch Events (for periodic triggers) or use AWS Step Functions if the process requires multiple steps.
<img width="798" alt="Screenshot 2025-01-02 at 7 02 42 PM" src="https://github.com/user-attachments/assets/8d880ac9-dbda-426f-811b-ed9c9c3cdb4f" />



## Screenshot
Here is a preview of the application:

<img width="518" alt="Screenshot 2025-01-06 at 4 27 05 PM" src="https://github.com/user-attachments/assets/2b0b2c51-c371-4c6a-9203-25436c6f1f19" />





