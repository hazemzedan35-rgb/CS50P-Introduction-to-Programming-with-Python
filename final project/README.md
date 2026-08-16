# Hive Health Checker: Environmental Monitoring System for Honeybee Hives

#### Video Demo: <https://youtu.be/DLuwbsdSh9g>

#### Description
The **Hive Health Checker** is an automated CLI utility built in Python to assist beekeepers in monitoring, diagnosing, and maintaining optimal environmental conditions inside honeybee (*Apis mellifera*) hives. 

Maintaining internal hive homeostasis—specifically surrounding the brood nest—is crucial for colony survival, larval development, and disease prevention. This tool evaluates real-time temperature and relative humidity metrics against scientifically established biological thresholds, offering immediate status diagnostics to prevent thermal stress or humidity-induced colony collapse.

---

### Key Features
* **Strict Input Validation:** Uses robust exception handling (`try-except` blocks) to parse float values and reject non-numerical entries without crashing.
* **Biological Threshold Analysis:** Compares inputs against ideal brood nest microclimate ranges:
  * **Temperature:** 33.0°C to 36.0°C (Optimal target: ~34.5°C)
  * **Relative Humidity:** 50.0% to 70.0% (Optimal target: ~60.0%)
* **Tri-Tier Status Evaluation:** Categorizes hive health into clear operational states:
  * **Optimal:** Both parameters are strictly within normal biological bounds.
  * **Warning:** One parameter has deviated, signaling potential stress or environmental drift.
  * **Critical:** Both parameters are out of range, signaling severe risk of brood damage or disease susceptibility.
* **Automated Unit Testing Suite:** Fully testable architecture via `pytest` to guarantee deterministic state evaluations.

---

### Project Architecture & File Structure

The project relies on a modular architecture designed to separate I/O operations from pure decision logic, ensuring seamless testing.

* **`project.py`**: The core application module. Contains data collection functions (`get_temprature`, `get_humidity`), validation logic (`check_temprature`, `check_humidity`), and the primary state processor (`check_hive_status`).
* **`test_project.py`**: Test suite written for `pytest`. Verifies nominal range boundaries, edge cases, and string formatting outputs across all boolean and evaluation functions.
* **`requirements.txt`**: Declares external third-party dependencies required for execution and testing (`pytest`).
* **`README.md`**: Technical documentation and system overview.

---

### Setup & Usage Instructions

1. **Clone the Repository & Install Dependencies:**
   ```bash
   pip install -r requirements.txt