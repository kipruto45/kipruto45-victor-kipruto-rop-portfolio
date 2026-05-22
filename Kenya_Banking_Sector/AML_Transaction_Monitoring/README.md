# 30. AML / Transaction Monitoring Rules Engine

## Difficulty: Advanced | Impact: High

### Overview
Build a rules-based AML transaction monitoring engine using public FATF typologies and CBK AML guidelines. Implement structuring detection, smurfing patterns, unusual cash spikes, and PEP cross-matching on synthetic transaction data with a case management queue.

### Tools Required
- Python
- Apache Kafka
- Redis
- PostgreSQL
- Apache Airflow
- FastAPI (case API)

### Kenyan Data Sources
- CBK AML/CFT Guidelines
- FATF Kenya Mutual Evaluation Report
- FRC Kenya

### Project Structure
```
kenya-aml-monitoring/
ingestion/
  synthetic_transaction_generator.py # Create realistic test txns
src/
  rules_engine/
    structuring_detector.py # SAR: multiple small deposits
    smurfing_detector.py # Multiple actors, one beneficiary
    cash_spike_detector.py # Unusual transaction amounts
    pep_matcher.py # Cross-check FATF, FRC PEP lists
    sanctions_screener.py # OFAC/FCDO/EU sanctions lists
  case_manager/
    alert_generator.py # Create case alerts
    case_queue.py # Prioritize suspicious activities
    api_endpoints.py # FastAPI case management
data/
  pep_lists/
    fatf_typologies.csv
    cbk_aml_guidelines.md
  rules/
    aml_rules.yaml # Configurable thresholds
messaging/
  kafka_producer.py # Send alerts to Kafka
  redis_cache.py # Cache PEP lists in Redis
dags/
tests/
docs/
```

### Key Deliverables
- Rules-based AML monitoring engine
- Structuring detection (SAR patterns)
- Smurfing pattern detection
- Unusual cash spike alerts
- PEP (Politically Exposed Persons) matching
- Transaction monitoring rules
- Case management API
- Alert routing and escalation

### Next Steps
1. Review FATF Kenya typologies
2. Access CBK AML guidelines
3. Get FRC guidance documents
4. Gather PEP databases
5. Design rules engine
6. Implement Kafka pipeline
7. Build FastAPI case management
8. Create synthetic test data
9. Deploy monitoring system
