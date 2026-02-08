# Setup Guide: Getting Started with Seismology Coding

Welcome to the First-Day Seismology Class! This guide will help you set up your environment and get started with AI-assisted learning.

## Quick Start (Recommended for Beginners)

### Option 1: Google Colab (Zero Installation Required) ⚡

This is the **easiest and recommended** way to get started!

#### Step 1: Access Google Colab
1. Open your web browser
2. Go to: https://colab.research.google.com/
3. Sign in with your Google account
4. Click "New Notebook"

#### Step 2: Test Your Environment
Copy and paste this code into a cell and press `Shift + Enter`:

```python
import sys
print(f"Python version: {sys.version}")
print("✅ Your environment is ready!")
```

#### Step 3: Install Seismology Libraries
Run this in a new cell:

```python
# Install seismology tools
!pip install obspy numpy matplotlib pandas

# Test installation
import obspy
print(f"✅ ObsPy version: {obspy.__version__}")
print("🎉 All libraries installed successfully!")
```

#### Step 4: Enable Gemini AI Assistant
1. Click the "🤖" icon in the left sidebar
2. Or use `Ctrl + Alt + Enter` to open AI chat
3. Try asking: "How do I load seismic data in Python?"

**That's it! You're ready to start coding!** 🚀

---

## AI Learning Tools Setup

### Setting Up NotebookLM

NotebookLM is your AI-powered study companion that can extract knowledge from textbooks.

#### Step 1: Access NotebookLM
1. Visit: https://notebooklm.google.com/
2. Sign in with your Google account
3. Click "New Notebook"

#### Step 2: Upload Course Materials
1. Click "Add Source"
2. Upload options:
   - PDF of seismology textbook
   - Google Drive documents
   - Web pages (course syllabus, readings)
   - YouTube videos (lectures)

#### Step 3: Start Learning
Try these example queries:

**Basic Concepts:**
```
"What are P-waves and S-waves?"
"Explain the difference between magnitude and intensity"
"How do seismometers work?"
```

**Coding Help:**
```
"How do I process seismic data in Python?"
"What is the ObsPy library used for?"
"Show me examples of plotting seismic waveforms"
```

**Study Guides:**
```
"Create a summary of Chapter 3"
"What are the key concepts about earthquake location?"
"Make a study guide for seismic wave propagation"
```

### Using Gemini AI Effectively

#### In Google Colab
Gemini is integrated directly into Colab:

1. **Code Generation:**
   ```
   Prompt: "Write Python code to plot a sine wave"
   Gemini will generate the code for you!
   ```

2. **Error Debugging:**
   ```
   When you get an error, ask:
   "Why am I getting a NameError in this code?"
   ```

3. **Explanation:**
   ```
   Select code and ask:
   "Explain what this code does"
   ```

#### Effective Prompting Tips

**Good Prompts:**
- ✅ "Write Python code to load a seismic file in miniSEED format using ObsPy"
- ✅ "Explain the Richter magnitude scale in simple terms"
- ✅ "Debug this error: ImportError: No module named 'obspy'"

**Less Effective Prompts:**
- ❌ "Code for seismology" (too vague)
- ❌ "Help" (no context)
- ❌ "Fix it" (AI doesn't know what "it" is)

---

## Option 2: Local Installation (Advanced Users)

If you prefer to work on your local machine:

### Prerequisites
- Python 3.8 or higher
- Git (optional)
- Text editor or IDE (VS Code recommended)

### Installation Steps

#### Windows

1. **Install Python:**
   - Download from: https://www.python.org/downloads/
   - Check "Add Python to PATH" during installation
   - Verify: Open Command Prompt and type `python --version`

2. **Install Libraries:**
   ```cmd
   pip install obspy numpy matplotlib pandas jupyter
   ```

3. **Start Jupyter:**
   ```cmd
   jupyter notebook
   ```

#### macOS

1. **Install Python (using Homebrew):**
   ```bash
   brew install python
   ```

2. **Install Libraries:**
   ```bash
   pip3 install obspy numpy matplotlib pandas jupyter
   ```

3. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

#### Linux (Ubuntu/Debian)

1. **Install Python:**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Install Libraries:**
   ```bash
   pip3 install obspy numpy matplotlib pandas jupyter
   ```

3. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

---

## Verification Tests

Run these tests to make sure everything works:

### Test 1: Basic Python
```python
# Test basic Python
x = [1, 2, 3, 4, 5]
print(f"Sum: {sum(x)}")
print("✅ Python works!")
```

### Test 2: NumPy
```python
# Test NumPy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(f"Mean: {np.mean(arr)}")
print("✅ NumPy works!")
```

### Test 3: Matplotlib
```python
# Test Matplotlib
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Test Plot")
plt.show()
print("✅ Matplotlib works!")
```

### Test 4: ObsPy
```python
# Test ObsPy
from obspy import read
from obspy.clients.fdsn import Client

client = Client("IRIS")
print("✅ ObsPy works!")
print("🎉 You can download real seismic data!")
```

---

## Getting Your First Seismic Data

Let's download real earthquake data!

```python
from obspy import UTCDateTime
from obspy.clients.fdsn import Client

# Connect to IRIS data center
client = Client("IRIS")

# Define time window (example: recent earthquake)
starttime = UTCDateTime("2024-01-01T00:00:00")
endtime = starttime + 3600  # 1 hour of data

# Download data
print("📡 Downloading seismic data...")
st = client.get_waveforms(
    network="IU",      # Network code
    station="ANMO",    # Station code
    location="00",     # Location code
    channel="BHZ",     # Channel code (vertical)
    starttime=starttime,
    endtime=endtime
)

print(f"✅ Downloaded {len(st)} trace(s)")
print(st)

# Plot the data
st.plot()
```

---

## Troubleshooting

### Common Issues

**Problem: "pip command not found"**
- **Solution:** Python not in PATH. Reinstall Python and check "Add to PATH"

**Problem: "No module named 'obspy'"**
- **Solution:** Run `pip install obspy` or `pip3 install obspy`

**Problem: "Permission denied" on Linux/Mac**
- **Solution:** Use `pip3 install --user obspy`

**Problem: Can't see plots in Jupyter**
- **Solution:** Add `%matplotlib inline` at the start of your notebook

**Problem: Colab disconnects**
- **Solution:** Click "Reconnect" or refresh the page

**Problem: Slow download speeds**
- **Solution:** Try a different FDSN client (e.g., "USGS" instead of "IRIS")

### Getting Help

1. **Ask Gemini AI:** Describe your problem in the Colab chat
2. **Check Documentation:** https://docs.obspy.org/
3. **Use NotebookLM:** Upload error message and ask for explanation
4. **Ask Instructor:** During office hours or in forum
5. **Community:** ObsPy forum, Stack Overflow

---

## Next Steps

Once your environment is set up:

1. ✅ Complete the verification tests above
2. ✅ Download your first seismic data
3. ✅ Set up NotebookLM with course materials
4. ✅ Practice using Gemini for coding help
5. ✅ Review the [PROPOSAL.md](PROPOSAL.md) for course overview
6. ✅ Open the first tutorial notebook

---

## Quick Reference Card

### Essential Commands

```python
# Import libraries
import obspy
import numpy as np
import matplotlib.pyplot as plt

# Download data
from obspy.clients.fdsn import Client
client = Client("IRIS")

# Read local file
from obspy import read
st = read("path/to/file.mseed")

# Plot
st.plot()

# Get info
print(st)

# Filter data
st.filter("bandpass", freqmin=1.0, freqmax=10.0)
```

### Useful AI Prompts

- "Load seismic data from IRIS"
- "Plot a seismogram with time on x-axis"
- "Calculate earthquake magnitude"
- "Filter seismic noise from data"
- "Explain this error message: [paste error]"

---

## Resources

### Official Documentation
- **ObsPy:** https://docs.obspy.org/
- **NumPy:** https://numpy.org/doc/
- **Matplotlib:** https://matplotlib.org/stable/
- **Python:** https://docs.python.org/3/

### Data Sources
- **IRIS:** https://www.iris.edu/
- **USGS:** https://earthquake.usgs.gov/
- **ORFEUS:** https://www.orfeus-eu.org/

### Learning Resources
- **ObsPy Tutorial:** https://docs.obspy.org/tutorial/
- **Python for Seismology:** https://krischer.github.io/seismo_live/
- **Seismology Datasets:** https://ds.iris.edu/ds/nodes/dmc/

---

**Ready to start your seismology journey? Let's code!** 🌍📊🐍

