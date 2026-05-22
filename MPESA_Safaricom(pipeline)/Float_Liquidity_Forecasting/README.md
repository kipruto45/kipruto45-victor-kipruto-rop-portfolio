# 5. M-Pesa Float & Liquidity Forecasting Pipeline

## Difficulty: Advanced | Impact: High

### Overview
Model daily M-Pesa float demand at agent level using historical transaction patterns, public holiday calendars, salary cycle data, and regional events. Train a Prophet/LSTM time-series model and schedule 7-day ahead forecasts to optimise float top-up logistics.

### Tools Required
- Python (Prophet, TensorFlow)
- Apache Airflow
- PostgreSQL
- dbt
- MLflow
- Grafana

### Kenyan Data Sources
- CBK M-Pesa statistics
- Safaricom annual reports
- Kenya public holiday API

### Project Structure
```
mpesa-float-forecasting/
ingestion/
  cbk_stats.py # CBK monthly M-Pesa statistics
  calendar_client.py # Kenya public holidays API
features/
  feature_engineering.py # Lag features, rolling averages
  salary_cycle.py # End-of-month demand signal
  event_calendar.py # Elections, holidays, school fees
models/
  prophet_model.py # Facebook Prophet forecasting
  lstm_model.py # TensorFlow LSTM for deep patterns
  ensemble.py # Weighted combination of models
  evaluate.py # MAE, RMSE, MAPE metrics
dags/
  forecast_dag.py # Weekly 7-day forecast run
  retrain_dag.py # Monthly model retraining
outputs/
  forecasts/ # Daily forecast CSVs per agent zone
dbt/
tests/
notebooks/
docs/
```

### Key Deliverables
- Prophet time-series models
- LSTM neural network forecasts
- 7-day ahead float demand predictions
- Agent-level forecasting
- MLflow model registry
- Grafana monitoring dashboards

### Next Steps
1. Collect historical float data
2. Build feature sets (holidays, salary cycles)
3. Train Prophet & LSTM models
4. Create Airflow DAGs for scheduling
5. Set up MLflow tracking
6. Deploy forecasting API
7. Monitor prediction accuracy
