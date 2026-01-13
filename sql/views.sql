-- View 1: Counts total complaints for each product
CREATE VIEW v_complaints_by_product AS
SELECT product,COUNT(complaint_id) AS total_complaints
FROM consumer_finance_complaints_cleaned
GROUP BY product
ORDER BY total_complaints DESC;

-- View 2: Counts total complaints for each state
CREATE VIEW v_complaints_by_state AS 
SELECT state,COUNT(complaint_id) AS total_complaints 
FROM consumer_finance_complaints_clean 
GROUP BY state;
-- View 3: Counts total complaints for each year of receiving
CREATE VIEW v_complaints_by_year AS 
SELECT Year_of_receiving,COUNT(complaint_id)AS total_complaints 
FROM consumer_finance_complaints_clean 
GROUP BY Year_of_receiving;

-- View 4: Calculates average days taken to send complaints for each product
CREATE VIEW v_avg_time_to_send_complaint_by_product AS 
SELECT product,AVG(days_to_send) as total_time 
FROM consumer_finance_complaints_clean 
GROUP BY product;

-- View 5: Shows companies with the highest number of complaints
CREATE VIEW v_top_companies_by_complaints AS 
SELECT TRIM(company)AS company_name, COUNT(complaint_id) AS total_complaints
FROM consumer_finance_complaints_clean
GROUP BY TRIM(company)
ORDER BY total_complaints DESC;


