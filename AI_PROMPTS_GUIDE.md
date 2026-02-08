# AI Prompts Guide for Seismology Learning

This guide provides effective prompts for using Gemini AI and NotebookLM to learn seismology and coding.

## 🤖 Using Gemini AI in Google Colab

### Getting Started with Code Generation

#### Basic Prompts
```
"Write Python code to import ObsPy and NumPy"
"Create a simple plot of a sine wave using matplotlib"
"Show me how to read a miniSEED file"
```

#### Seismology-Specific Prompts
```
"Write code to download seismic data from IRIS for station ANMO"
"Generate Python code to plot a seismogram with time on x-axis"
"Create code to apply a bandpass filter to seismic data"
"Show me how to calculate the envelope of a seismic trace"
```

### Debugging Help

#### Error Understanding
```
"Explain this error: ImportError: No module named 'obspy'"
"Why am I getting 'No data available for request' from FDSN?"
"What does this warning mean: [warning message]"
"Debug this code: [paste your code]"
```

#### Code Improvement
```
"How can I make this plot look better?"
"Is there a more efficient way to write this loop?"
"Why is my code running slowly?"
"How do I add error handling to this function?"
```

### Learning and Explanation

#### Concept Explanation
```
"Explain what P-waves and S-waves are in simple terms"
"What is the difference between magnitude and intensity?"
"How does a seismometer work?"
"Explain the concept of transfer function in seismology"
```

#### Code Explanation
```
"Explain what this ObsPy function does: stream.filter()"
"What are the parameters for UTCDateTime?"
"Break down this code line by line: [paste code]"
"What is the purpose of stream.detrend()?"
```

### Advanced Tasks

#### Data Processing
```
"How do I remove instrument response from seismic data?"
"Write code to pick P-wave arrivals automatically"
"Show me how to rotate components to radial/transverse"
"Create a spectrogram of seismic data"
```

#### Analysis
```
"Calculate earthquake magnitude from amplitude"
"How do I compute particle motion from three-component data?"
"Write code to calculate signal-to-noise ratio"
"Generate code for frequency-wavenumber analysis"
```

---

## 📚 Using NotebookLM for Seismology

### Initial Setup

**Upload Materials:**
1. Seismology textbook PDFs
2. Course lecture notes
3. ObsPy documentation
4. Research papers

### Effective Query Patterns

#### Understanding Concepts

**Basic Questions:**
```
"What are body waves versus surface waves?"
"Explain the difference between Love and Rayleigh waves"
"How do earthquakes generate seismic waves?"
"What is seismic anisotropy?"
```

**Deep Dive:**
```
"Create a detailed explanation of earthquake location methods"
"Compare different magnitude scales (ML, Mw, Mb)"
"Explain tomographic imaging in seismology"
"What are the main challenges in earthquake prediction?"
```

#### Study Guides and Summaries

**Chapter Summaries:**
```
"Summarize Chapter 3 on seismic wave propagation"
"Create bullet points of key concepts from the elasticity chapter"
"What are the main takeaways from the section on ray theory?"
```

**Concept Maps:**
```
"Create a concept map connecting earthquake source, wave propagation, and recording"
"List all the relationships between magnitude, moment, and energy"
"Outline the steps from earthquake occurrence to seismogram"
```

#### Problem Solving

**Homework Help:**
```
"How do I approach calculating travel times?"
"What formula should I use for epicentral distance?"
"Walk me through the process of picking phase arrivals"
```

**Practice Problems:**
```
"Generate practice problems on wave velocity calculations"
"Create example questions about magnitude calculations"
"Give me scenarios to practice earthquake location"
```

---

## 💡 Tips for Effective Prompting

### Be Specific

**❌ Vague:**
```
"Help with seismology"
"Code not working"
"Explain earthquakes"
```

**✅ Specific:**
```
"Explain how to download seismic data from the USGS using ObsPy"
"Why is my bandpass filter code giving an error about frequency limits?"
"What is the physical mechanism of P-wave generation in earthquakes?"
```

### Provide Context

**❌ No Context:**
```
"Fix this"
"What's wrong?"
```

**✅ With Context:**
```
"I'm trying to plot seismic data but getting an empty plot. Here's my code: [code]"
"I'm learning about magnitude scales and confused about the difference between ML and Mw"
```

### Break Down Complex Tasks

**❌ Too Complex:**
```
"Build a complete earthquake analysis program"
```

**✅ Step by Step:**
```
1. "How do I download data from multiple stations?"
2. "How do I synchronize the time windows?"
3. "How do I plot all traces together?"
4. "How do I measure arrival times on each trace?"
```

### Ask Follow-Up Questions

**Progressive Learning:**
```
1. "What is a seismogram?"
2. "How do I read a seismogram in Python?"
3. "How do I filter the seismogram?"
4. "How do I identify different wave phases?"
5. "How do I measure wave amplitudes?"
```

---

## 🎯 Domain-Specific Prompt Templates

### Data Acquisition

```
"How do I download [time period] of data from [station] on the [network] network?"
"What are the available stations near [location]?"
"How do I search for earthquakes in [region] with magnitude > [value]?"
```

### Data Processing

```
"Apply a [filter type] filter with [parameters] to [data type]"
"Remove [artifact type] from [data]"
"Convert [input format] to [output format]"
```

### Visualization

```
"Create a [plot type] showing [data] with [specific features]"
"Plot [multi-component data] in [layout] format"
"Generate a [map type] with [stations/earthquakes]"
```

### Analysis

```
"Calculate [parameter] from [data] using [method]"
"Detect [feature] in [signal] with [algorithm]"
"Compare [data1] and [data2] using [metric]"
```

---

## 🚀 Advanced Prompting Techniques

### Chain of Thought

**Ask AI to think step-by-step:**
```
"Walk me through the logic of calculating earthquake magnitude step by step"
"Explain your reasoning for why this code isn't working"
"Break down the physics behind P-wave velocity variations"
```

### Provide Examples

**Show what you want:**
```
"Generate code similar to this example but for downloading S-waves: [example code]"
"Create a plot like this but with different colors: [description]"
```

### Request Alternatives

**Get multiple options:**
```
"Show me three different ways to filter seismic data"
"What are alternative methods for picking phase arrivals?"
"Compare different approaches to plotting seismograms"
```

### Ask for Explanations

**Understand the why:**
```
"Why do we use this formula for magnitude?"
"Why is this method better than that one?"
"What are the limitations of this approach?"
```

---

## 📊 Example Learning Session

### Session 1: Loading Data

1. **Start with basics:**
   ```
   "How do I connect to the IRIS data center in Python?"
   ```

2. **Build on it:**
   ```
   "How do I specify a time window for data download?"
   ```

3. **Add complexity:**
   ```
   "How do I download data from multiple stations at once?"
   ```

4. **Troubleshoot:**
   ```
   "I'm getting 'No data available' - what could be wrong?"
   ```

5. **Optimize:**
   ```
   "How can I make this code more efficient?"
   ```

### Session 2: Understanding Concepts

1. **Basic understanding:**
   ```
   NotebookLM: "What are seismic phases?"
   ```

2. **Deep dive:**
   ```
   NotebookLM: "Explain the travel time curves for different phases"
   ```

3. **Application:**
   ```
   Gemini: "Write code to calculate theoretical arrival times"
   ```

4. **Verification:**
   ```
   NotebookLM: "How do theoretical times compare to observed times?"
   ```

---

## 🎓 Subject-Specific Prompts

### Wave Propagation

```
"Explain Snell's law in the context of seismic waves"
"How do velocity discontinuities affect wave paths?"
"What causes seismic wave dispersion?"
"Code to simulate wave propagation through layers"
```

### Earthquake Source

```
"What is the focal mechanism of an earthquake?"
"Explain the double-couple source model"
"How is seismic moment related to magnitude?"
"Calculate moment from slip, area, and rigidity"
```

### Signal Processing

```
"What is the purpose of detrending seismic data?"
"Explain the difference between causal and acausal filters"
"How do I choose appropriate filter parameters?"
"Implement a Butterworth filter in Python"
```

### Instrumentation

```
"How does a seismometer differ from an accelerometer?"
"What is instrument response and why remove it?"
"Explain the units in seismic data (counts, velocity, acceleration)"
"Convert between different ground motion units"
```

---

## 🔄 Iterative Prompting Pattern

### The Learning Loop

1. **Ask**: Request information or code
2. **Review**: Read and try to understand the response
3. **Test**: Run code or apply concept
4. **Refine**: Ask follow-up questions
5. **Expand**: Build on what you learned

### Example Loop

```
Round 1: "How do I plot a seismogram?"
[Get code, try it]

Round 2: "The plot is too small, how do I make it bigger?"
[Adjust code]

Round 3: "How do I add axis labels and a title?"
[Enhance plot]

Round 4: "Can I plot multiple seismograms together?"
[Expand capability]

Round 5: "How do I save this plot as a high-resolution image?"
[Polish output]
```

---

## ⚡ Quick Reference Prompts

### Common Tasks

**Data Download:**
```
"Download data: network=[NET], station=[STA], start=[TIME], duration=[MINS]"
```

**Basic Plot:**
```
"Plot seismic trace with time in minutes on x-axis"
```

**Filter:**
```
"Apply bandpass filter [FMIN]-[FMAX] Hz"
```

**Save:**
```
"Save processed data as [FORMAT]"
```

### Troubleshooting

**Import Error:**
```
"How do I install [library]?"
```

**Empty Output:**
```
"Data request returns empty - debug: [query details]"
```

**Plot Issue:**
```
"Plot showing [problem] - code: [code snippet]"
```

**Performance:**
```
"Code slow for [data size] - optimize: [code]"
```

---

## 🌟 Best Practices

### Do's ✅

- Start simple, build complexity
- Provide code samples when relevant
- Specify exact error messages
- Ask for explanations of responses
- Iterate and refine prompts
- Save useful prompts for reuse

### Don'ts ❌

- Don't paste entire error tracebacks (summarize key info)
- Don't ask multiple unrelated questions at once
- Don't assume AI knows your data structure
- Don't skip testing suggested code
- Don't forget to ask "why" things work

---

## 🎯 Goal-Oriented Prompt Frameworks

### For Understanding

```
"I want to understand [CONCEPT]
- Start with a simple explanation
- Give an analogy
- Explain the physics/math
- Show a practical example
- List common misconceptions"
```

### For Coding

```
"I need to [TASK]
- My data format is [FORMAT]
- I want output as [OUTPUT]
- Constraints: [CONSTRAINTS]
- Show the code and explain key parts"
```

### For Debugging

```
"My code isn't working:
- Goal: [WHAT I'M TRYING TO DO]
- Current behavior: [WHAT HAPPENS]
- Expected: [WHAT SHOULD HAPPEN]
- Code: [RELEVANT CODE]
- Error: [ERROR MESSAGE]"
```

---

**Master these prompting techniques and you'll learn faster, code better, and understand deeper!** 🚀

