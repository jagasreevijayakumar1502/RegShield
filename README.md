RegShield

RegShield is an intelligent financial fraud detection system designed to identify suspicious transactions and potential mule accounts in real time. It combines rule-based detection, risk scoring, and live monitoring to help financial institutions prevent fraudulent activities efficiently.
---
Features

🔹 Real-Time Transaction Monitoring  
🔹 Mule Account Detection  
🔹 Risk Scoring System  
🔹 Live Dashboard with Alerts  
🔹 Rule-Based Fraud Detection Engine  
🔹 CIBIL Score Integration (Mock Dataset Supported)  
🔹 Scalable Architecture (Kafka / Queue Ready)
---
Problem Statement

Financial fraud and mule account activities are increasing rapidly, causing major losses to banks and users. Traditional systems are slow, reactive, and often fail to detect suspicious patterns in real time.

---
Solution

RegShield provides a proactive fraud detection system that:

- Continuously monitors transactions  
- Assigns risk scores based on behavior  
- Detects anomalies using predefined rules  
- Flags mule accounts instantly  
- Displays alerts on a live dashboard  
---
System Architecture

1. Transaction Generator
   - Simulates real-time transactions using Python
   - Sends data continuously

2. Processing Layer
   - Uses queue/Kafka (optional)
   - Processes transactions instantly

3. Detection Engine
   - Applies fraud rules
   - Calculates risk score

4. Dashboard
   - Displays transactions
   - Shows alerts and flagged accounts
   - Visualizes risk levels
---
Risk Parameters

- Transaction Frequency  
- Amount Deviation  
- Suspicious Patterns  
- Account Behavior  
- CIBIL Score (optional integration)  
---
Tech Stack

- Frontend: HTML, CSS, JavaScript  
- Backend: Flask (Python)  
- Data Processing: Python Scripts  
- Messaging (Optional): Kafka / Queue  
- Visualization: Charts / Dashboard UI  
