# cluster-service-monitor
Tool to monitor system service statuses across a cluster using Python and MySQL.

# 🔍 Cluster System Status Monitor

A lightweight Python-based monitoring tool that fetches the status of user-defined services across nodes in a cluster. Service names and node IPs are stored in a database, and the system checks their status in real-time or scheduled intervals.

---

## 🚀 Features

- 🔗 Fetches predefined services and nodes from a central database
- 📡 Checks service status using SSH or local checks
- 🧠 Optimized for parallel execution to support large clusters
- 📦 Provides summarized and detailed reports
- 🌐 Ready for integration with APIs/UI dashboards

---

## 🛠️ Tech Stack

- **Python 3.x**
- **MySQL** (for service/node mapping)
- **Paramiko** or native SSH
- Optional: **Flask** for API endpoint

---

## 📚 Architecture

```plaintext
MySQL DB
  └── [Service/Node Mapping Table]
        └── Python Script
              ├── Multi-threaded Status Check
              ├── Output Summary (Success/Failed)
              └── (Optional) API Integration / Logs

