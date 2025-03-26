# Python script containing SQL queries

queries = [
    'Query 1: -- To evaluate sales performance by store location CREATE VIEW Analysis.Performance_by_location AS SELECT     Store_Location,     COUNT(Transaction_ID) AS Number_of_Transactions,     SUM(Final_Amount) AS Total_Sales,     AVG(Final_Amount) AS Average_Sale_Amount FROM     Retail_Sales GROUP BY     Store_Location ORDER BY     Total_Sales DESC',
    'Query 2: -- Best-performing sales representatives. CREATE VIEW Analysis.Best_performing_Rep AS SELECT     Sales_Representative,     COUNT(Transaction_ID) AS Number_of_Transactions,     SUM(Final_Amount) AS Total_Sales,     AVG(Final_Amount) AS Average_Sale_Amount FROM     Retail_Sales GROUP BY     Sales_Representative ORDER BY     Total_Sales DESC',
    'Query 3: --lets PErform Some Time Base Series Analysis 	--- Sales by day of the week. 	CREATE VIEW Analysis.Sales_by_weekdays AS SELECT     DATENAME(weekday, Date) AS DayOfWeek,     COUNT(Transaction_ID) AS Number_of_Transactions,     SUM(Final_Amount) AS Total_Sales,     AVG(Final_Amount) AS Average_Sale_Amount FROM     Retail_Sales GROUP BY     DATENAME(weekday, Date),     DATEPART(weekday, Date) ORDER BY     DATEPART(weekday, Date)',
    'Query 4: -- Monthly Sales trends SELECT     YEAR(Date) AS Year,     MONTH(Date) AS Month,     SUM(Final_Amount) AS Total_Sales FROM     Retail_Sales GROUP BY     YEAR(Date),     MONTH(Date) ORDER BY 	Total_sales desc  --impact Of Discount on revenuw CREATE VIEW Analysis.impact_of_discount AS SELECT     CASE         WHEN Discount_Applied > 0 THEN \'Discounted Sales\'         ELSE \'Non-Discounted Sales\'     END AS Sale_Type,     COUNT(Transaction_ID) AS Number_of_Transactions,     SUM(Total_Amount) AS Gross_Revenue,     SUM(Final_Amount) AS Net_Revenue,     SUM(Total_Amount) - SUM(Final_Amount) AS Total_Discount_Amount,     AVG(Discount_Applied) AS Average_Discount_Percentage FROM     Retail_Sales GROUP BY     CASE         WHEN Discount_Applied > 0 THEN \'Discounted Sales\'         ELSE \'Non-Discounted Sales\'     END',
]

