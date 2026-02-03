# 🚀 Quick Start Guide

Get up and running with your Customer Segmentation ML Pipeline in 5 minutes!

## 1️⃣ Setup (One-time)

```bash
# Clone repo
git clone https://github.com/Selvam-9/Customer-Segmentation.git
cd Customer-Segmentation

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

## 2️⃣ Train Model

```bash
python run_training.py
```

✅ Model saved to `artifact/model.pkl`

## 3️⃣ Evaluate Performance

```bash
python evaluate.py
```

Shows: Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index

## 4️⃣ Run Web App

```bash
streamlit run app.py
```

Open: http://localhost:8501

## 5️⃣ Run Tests

```bash
pytest tests/ -v
```

## 🐳 Docker

```bash
# Build
docker build -t customer-seg .

# Run
docker run -p 8501:8501 customer-seg
```

## 📁 Project Structure

```
artifact/          → Models & data
src/               → Source code
  ├── components/  → Data & model
  └── pipeline/    → Predictions
tests/             → Unit tests
notebook/          → Jupyter notebooks
logs/              → Application logs
config.yaml        → Configuration
```

## ⚙️ Configure

Edit `config.yaml` to customize:
- Data paths
- Number of clusters
- Feature scaling method
- Model parameters

## 📊 Check Status

```bash
# Git status
git status

# Recent logs
Get-Content logs/app_logs.log -Tail 20  # Windows
tail -f logs/app_logs.log              # Linux/Mac
```

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | Run: `pip install -r requirements.txt` |
| Model not found | Run: `python run_training.py` first |
| Port 8501 in use | Change in `streamlit run app.py --server.port 8502` |
| Tests fail | Ensure model is trained: `python run_training.py` |

## 📚 Full Documentation

See [README.md](README.md) for comprehensive documentation.

## 💡 Common Commands

```bash
# Check Python version
python --version

# Verify dependencies
pip list | grep -E "pandas|scikit-learn|streamlit"

# Clean cache
rm -r src/__pycache__ tests/__pycache__

# Push changes
git add . && git commit -m "message" && git push origin master
```

## 📞 Support

Issues? Check the [README.md](README.md) or GitHub Issues.

---
**Ready to predict customer segments? Start with Step 1!** 🎯
