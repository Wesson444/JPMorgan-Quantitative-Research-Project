# JPMorgan-Quantitative-Research-Project
一个量化研究项目合集，包含时间序列预测、合约定价、信用风险建模和动态规划应用

## Table of Contents
- [Task 1: Natural Gas Price Prediction](#task-1-natural-gas-price-prediction)
- [Task 2: Gas Storage Contract Pricing](#task-2-gas-storage-contract-pricing)
- [Task 3: Credit Risk Analysis](#task-3-credit-risk-analysis)
- [Task 4: Optimal FICO Score Binning](#task-4-optimal-fico-score-binning)
- [How to Use](#how-to-use)

---

### **Task 1: Natural Gas Price Prediction**

**Objective:** To analyze historical monthly natural gas prices, identify seasonal patterns, and develop a model to forecast future prices. The end goal is to create a function that can estimate the price of natural gas for any given date.

**Methodology:**
* **Time Series Analysis:** The historical price data was visualized to identify seasonal trends. A `seasonal_decompose` function was used to separate the time series into trend, seasonal, and residual components.
* **SARIMA Model:** A Seasonal Autoregressive Integrated Moving Average (SARIMA) model was chosen to capture the seasonality in the data. A grid search was performed to find the optimal model parameters that minimized the Akaike Information Criterion (AIC).
* **Forecasting and Interpolation:** The best SARIMA model was used to forecast prices for the next 12 months. Both historical and forecasted monthly data were then interpolated to create a continuous daily price series.

**Outcome:** A Python function, `estimate_price(date)`, that returns the estimated price of natural gas for any date within the interpolated range.

---

### **Task 2: Gas Storage Contract Pricing**

**Objective:** To develop a pricing model for a natural gas storage contract, which allows a client to buy gas, store it, and sell it at a later date.

**Methodology:**
The valuation of the contract is based on the principle of discounted cash flows. The model calculates the net value of the contract by considering:
* **Price Differential:** The difference between the selling price at the withdrawal date and the purchasing price at the injection date.
* **Costs:**
    * **Injection/Withdrawal Costs:** A fee charged for injecting and withdrawing gas.
    * **Storage Costs:** A monthly fee for storing the gas.

**Outcome:** A function `contract_pricing()` that takes injection/withdrawal dates, volume, rates, and storage costs as inputs and returns the net value of the contract.

---

### **Task 3: Credit Risk Analysis**

**Objective:** To build a predictive model that estimates the probability of default (PD) for personal loan borrowers based on their financial characteristics. The ultimate goal is to calculate the Expected Loss (EL) for each loan.

**Methodology:**
* **Feature Engineering:** New features were created from the existing data to better capture the borrower's financial health, such as `education` (income/years_employed) and `payment_pressure` (loan_amt_outstanding/income).
* **Model Comparison:** Several classification models were trained and evaluated on their ability to predict default, including:
    * Logistic Regression
    * Decision Tree
    * LightGBM
    * XGBoost
    * A stacking ensemble of all models.
* **Model Selection:** The logistic regression model was chosen for its strong performance and interpretability.

**Outcome:** A function `predict_expected_loss(borrowers_list, trained_model)` that takes a list of new borrowers and a trained model as input and returns a DataFrame with the predicted probability of default and the expected loss for each borrower, assuming a 10% recovery rate.

---

### **Task 4: Optimal FICO Score Binning**

**Objective:** To categorize a range of FICO scores into a predefined number of buckets. This is a common preprocessing step for machine learning models that require categorical inputs.

**Methodology:**
Two dynamic programming approaches were implemented to find the optimal bin boundaries:
1.  **Unsupervised Binning (Minimize MSE):** This method groups FICO scores to minimize the Mean Squared Error (MSE) within each bucket. It aims to create buckets where the scores are as close to the bucket's mean as possible.
2.  **Supervised Binning (Maximize Log-Likelihood):** This method uses the default information to create buckets that best separate defaulters from non-defaulters. It maximizes a log-likelihood function, which rewards creating "purer" buckets (i.e., buckets with a high concentration of either defaulters or non-defaulters).

**Outcome:** Two functions, `find_optimal_binning_mse()` and `find_optimal_binning_supervised()`, that take a DataFrame and the desired number of bins as input and return the optimal FICO score boundaries for each method.

---

### **How to Use**

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/JPMorgan-Quantitative-Research-Project.git](https://github.com/your-username/JPMorgan-Quantitative-Research-Project.git)
    ```
2.  **Install dependencies:** Make sure you have the necessary Python libraries installed.
    ```bash
    pip install pandas numpy scipy matplotlib seaborn statsmodels scikit-learn lightgbm xgboost
    ```
3.  **Run the scripts:** Each task is contained in its own Python script. You can run them individually to see the analysis and results.
