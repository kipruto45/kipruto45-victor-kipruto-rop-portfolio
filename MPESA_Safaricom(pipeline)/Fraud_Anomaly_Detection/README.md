# 3. M-Pesa Fraud & Anomaly Detection System

## Difficulty: Advanced | Impact: High

### Overview
Build a sub-200ms fraud scoring pipeline for M-Pesa transactions using velocity checks (>5 sends in 60s), SIM-swap recency flags, unusual amount spikes, and an XGBoost model. Write flagged transactions to a review queue and auto-generate CBK STR (Suspicious Transaction Reports).

### Tools Required
- Apache Kafka
- Apache Flink
- Redis
- Python (XGBoost, scikit-learn)
- PostgreSQL
- Slack API

### Kenyan Data Sources
- Daraja API webhooks
- CBK AML/CFT guidelines
- Synthetic fraud training data

### Project Structure
```
mpesa-fraud-detection/
ingestion/
  transaction_producer.py # Kafka producer from Daraja webhook
fraud_engine/
  rules/
    velocity_check.py # >5 sends in 60s flag
    sim_swap_check.py # SIM changed in last 48h
    amount_spike.py # Statistical outlier detection
  ml/
    train_model.py # XGBoost training pipeline
    score_transaction.py # Real-time inference
    features.py # Feature engineering
  scorer.py # Combines rules + ML score
alerts/
  slack_alert.py # Notify fraud team on Slack
  str_generator.py # Auto-generate CBK STR report PDF
models/ # Saved MLflow model artifacts
dags/
  retrain_dag.py # Weekly model retraining DAG
tests/
notebooks/
docs/
```

### Key Deliverables
- Sub-200ms fraud scoring pipeline
- Velocity-based transaction checks
- XGBoost ML fraud detector
- STR (Suspicious Transaction Report) generation
- Slack alerting system
- Case management queue

### Next Steps
1. Gather synthetic fraud training data
2. Train XGBoost model
3. Set up Kafka streams for transactions
4. Build Flink fraud detection logic
5. Configure Redis for caching
6. Implement STR generation
7. Set up Slack notifications
