# Instructor's Lesson Plan - Seismology Day 1

**Duration:** 3 hours (180 minutes)  
**Format:** Interactive, hands-on workshop  
**Platform:** Google Colab (recommended) or local Jupyter  
**Prerequisites:** None - absolute beginners welcome!

---

## 📋 Preparation Checklist (Before Class)

### One Week Before
- [ ] Send welcome email with links to SETUP_GUIDE.md
- [ ] Create class Google Colab notebook (or share first_day_tutorial.ipynb link)
- [ ] Test all code examples in notebook
- [ ] Verify IRIS data center is accessible
- [ ] Prepare example earthquake list (recent significant events)
- [ ] Set up NotebookLM with course textbook
- [ ] Create discussion forum/channel (Slack/Discord/etc.)

### One Day Before
- [ ] Verify all students have Google accounts (for Colab)
- [ ] Share Colab notebook link with edit access or view-only
- [ ] Prepare backup activities in case of technical issues
- [ ] Test internet connectivity and projector setup
- [ ] Have ObsPy documentation bookmarked
- [ ] Prepare Q&A slides (optional)

### Morning Of
- [ ] Arrive 15 minutes early
- [ ] Test projector and screen sharing
- [ ] Open all necessary tabs (Colab, IRIS, USGS, NotebookLM)
- [ ] Write WiFi password on board
- [ ] Have backup laptop ready
- [ ] Prepare sign-in sheet (if needed)

---

## ⏰ Detailed Timeline

### Module 1: Welcome & Introduction (0-20 min)

**0-5 min: Welcome**
- Introduce yourself and teaching assistants
- Quick icebreaker: "What brings you to seismology?"
- Overview of the day's agenda
- Housekeeping (bathrooms, breaks, emergency exits)

**5-10 min: What is Seismology?**
- Show recent earthquake video/news
- Explain real-world applications:
  - Earthquake hazard assessment
  - Earth structure studies
  - Nuclear monitoring
  - Exploration geophysics
- Share personal research story (if applicable)

**10-15 min: The "Antigravity" Approach**
- Explain the philosophy: removing barriers to learning
- Demo: Show how easy it is to get real data (30 seconds)
- Highlight AI tools as learning companions
- Set expectations: hands-on, exploratory, supportive

**15-20 min: Setup Check**
- "Everyone open Google Colab now"
- Walk through accessing Colab
- Troubleshoot common issues
- Pair students who are ahead with those struggling

**💡 Teaching Tips:**
- Be enthusiastic and welcoming
- Share your own learning journey
- Acknowledge that coding can be intimidating
- Emphasize: mistakes are learning opportunities

---

### Module 2: AI Tools Introduction (20-35 min)

**20-25 min: Gemini AI Demo**
- Live demo: Ask Gemini to write simple code
- Show debugging example with real error
- Demonstrate code explanation feature
- Have students try: "Write code to import ObsPy"

**25-30 min: NotebookLM Setup**
- Guide students through NotebookLM access
- Demo: Upload sample textbook chapter/notes
- Show example queries and responses
- Students practice: Ask about a seismology concept

**30-35 min: Effective Prompting**
- Share AI_PROMPTS_GUIDE.md highlights
- Show good vs. bad prompts
- Practice together: craft a good prompt
- Emphasize: specific, contextual, iterative

**💡 Teaching Tips:**
- Normalize using AI - it's a tool, not cheating
- Show real examples of when AI helps you
- Demonstrate how to verify AI responses
- Encourage experimentation

---

### Module 3: Python & ObsPy Basics (35-60 min)

**35-40 min: First Code Cells**
```python
# Cell 1: Test Python
print("Hello Seismology!")
x = [1, 2, 3, 4, 5]
print(f"Sum: {sum(x)}")
```
- Everyone runs this together
- Celebrate first success!
- Explain cells, Shift+Enter
- Show output area

**40-45 min: Library Installation**
```python
# Cell 2: Install ObsPy
!pip install obspy -q
print("✅ ObsPy installed!")
```
- Explain what pip does
- Show progress indicators
- Wait for everyone to complete
- Troubleshoot any issues

**45-50 min: Import Libraries**
```python
# Cell 3: Import tools
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import matplotlib.pyplot as plt
import numpy as np
```
- Explain each import
- Discuss what each library does
- Show documentation links
- Check for import errors

**50-55 min: Connect to Data**
```python
# Cell 4: Connect to IRIS
client = Client("IRIS")
print("📡 Connected!")
```
- Explain IRIS and FDSN
- Show IRIS website briefly
- Discuss global seismic networks
- Preview what data we can access

**55-60 min: Quick Break & Questions**
- 5-minute stretch break
- Answer questions
- Check pace - adjust if needed
- Preview next module

**💡 Teaching Tips:**
- Go slowly - many may be coding for first time
- Use "we" language: "Let's try this together"
- Have TAs circulate to help individuals
- Celebrate small wins loudly
- Show your own screen for each step

---

### Module 4: First Earthquake Analysis (60-100 min)

**60-70 min: Download Real Data**
```python
# Cell 5: Get earthquake data
start = UTCDateTime("2024-02-06T01:17:00")
st = client.get_waveforms(
    network="IU",
    station="ANTO", 
    location="00",
    channel="BHZ",
    starttime=start,
    endtime=start+600
)
print(st)
```

**Teaching Points:**
- Use a recent significant earthquake
- Explain each parameter
- Show station on map
- Discuss channel codes (refer to QUICK_REFERENCE.md)
- Troubleshoot download issues

**70-80 min: Visualize Data**
```python
# Cell 6: Plot the earthquake
st.plot()
```

**Interactive Discussion:**
- What do we see?
- Point out P-wave arrival
- Identify S-wave arrival
- Discuss surface waves
- Compare with students' plots

**80-90 min: Process Data**
```python
# Cell 7: Filter the data
st_filtered = st.copy()
st_filtered.filter("bandpass", freqmin=0.1, freqmax=10.0)

# Cell 8: Compare raw vs filtered
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
ax1.plot(st[0].times(), st[0].data)
ax1.set_title('Raw')
ax2.plot(st_filtered[0].times(), st_filtered[0].data)
ax2.set_title('Filtered')
plt.tight_layout()
plt.show()
```

**Teaching Points:**
- Why filter? (remove noise)
- What frequencies to choose?
- Always copy before modifying!
- Discuss differences in plots

**90-100 min: Basic Analysis**
```python
# Cell 9: Calculate statistics
data = st_filtered[0].data
max_amp = np.max(np.abs(data))
peak_idx = np.argmax(np.abs(data))
peak_time = st_filtered[0].times()[peak_idx]

print(f"Maximum amplitude: {max_amp}")
print(f"Peak arrival: {peak_time:.1f} seconds")
```

**Interactive Exercise:**
- Have students find values
- Compare results (should be similar)
- Discuss what values mean
- Relate to earthquake size/distance

**💡 Teaching Tips:**
- Use live, recent earthquakes when possible
- Show enthusiasm when data appears!
- Zoom in on interesting features
- Encourage students to explore their plots
- Be prepared for download failures (backup examples)

---

### Module 5: Hands-On Practice (100-130 min)

**100-105 min: Introduce Challenge**
Present 3 difficulty levels:

**Easy Challenges:**
1. Change station to "ANMO"
2. Download 20 minutes instead of 10
3. Try different filter frequencies

**Medium Challenges:**
4. Download all three components (BH*)
5. Plot all components together
6. Measure P-S time difference

**Advanced Challenges:**
7. Download from multiple stations
8. Create a spectrogram
9. Calculate signal-to-noise ratio

**105-125 min: Student Work Time**
- Students work individually or in pairs
- TAs and instructor circulate
- Provide hints, not solutions
- Encourage using AI when stuck
- Help debug issues

**125-130 min: Share Results**
- Volunteers show their work (2-3 students)
- Discuss different approaches
- Celebrate successes
- Learn from failures

**💡 Teaching Tips:**
- Create supportive environment for sharing
- Highlight creative solutions
- Show how AI helped (or didn't)
- Acknowledge effort, not just results

---

### Module 6: Advanced Topics Teaser (130-145 min)

**Quick demonstrations (5 min each):**

**1. Multiple Stations**
```python
stations = ["ANMO", "ANTO", "COLA"]
streams = []
for sta in stations:
    st = client.get_waveforms("IU", sta, "00", "BHZ", 
                              start, start+600)
    streams.append(st)
```

**2. Spectrogram**
```python
st[0].spectrogram()
```

**3. Map of Stations**
- Show IRIS or USGS map
- Discuss network coverage
- Preview Day 2 topics

**💡 Teaching Tips:**
- Keep it high-level, don't dive deep
- Build excitement for next session
- Show what's possible with more practice

---

### Module 7: Wrap-up & Next Steps (145-165 min)

**145-150 min: Review What We Learned**
- Quick recap of skills gained
- Emphasize progress made
- Address final questions

**150-155 min: Resources & Homework**
- Point to repository files
- Assign practice exercises:
  - Analyze 3 different earthquakes
  - Try each challenge level
  - Document findings (short report)
- Share additional resources

**155-160 min: Preview Day 2**
- Earthquake location methods
- Magnitude calculations
- Machine learning applications
- Real-time data analysis

**160-165 min: Feedback & Closing**
- Quick survey (Google Form)
- Open discussion
- Thank students
- Remind about office hours

---

## 🎯 Learning Objectives Check

By end of session, students should be able to:
- [ ] Access and use Google Colab
- [ ] Install Python libraries
- [ ] Use Gemini AI for coding help
- [ ] Download seismic data from IRIS
- [ ] Create basic plots of seismograms
- [ ] Apply filters to seismic data
- [ ] Calculate simple statistics
- [ ] Use NotebookLM for learning
- [ ] Debug basic errors
- [ ] Work independently on simple tasks

---

## 🎓 Assessment Strategies

### Formative (During Class)
- Observe student screens while circulating
- Ask questions to check understanding
- Quick polls: "Who successfully downloaded data?"
- Code review during exercises

### Summative (After Class)
- Homework completion
- Quality of earthquake analysis
- Ability to use AI tools
- Self-reported confidence survey

---

## 🔧 Troubleshooting Guide

### Common Technical Issues

**Colab Won't Load**
- Solution: Try incognito mode
- Backup: Use local Jupyter
- Alternative: Binder link

**ObsPy Install Fails**
- Solution: Restart runtime
- Alternative: Try `!pip install --upgrade obspy`

**No Data Available**
- Solution: Adjust time window
- Alternative: Use different station
- Backup: Provide pre-downloaded data

**Plot Doesn't Show**
- Solution: Add `%matplotlib inline`
- Alternative: Use `plt.show()`

**Internet Issues**
- Backup: Have local data files
- Activity: Work with provided examples
- Discussion: Conceptual questions

---

## 📊 Classroom Management

### Pacing
- Watch for students falling behind
- Adjust speed based on group
- Have advanced students help others
- Optional sections if ahead of schedule

### Engagement
- Ask questions frequently
- Use think-pair-share
- Cold call gently
- Celebrate discoveries

### Inclusion
- Use varied examples
- Acknowledge different backgrounds
- Provide multiple paths to success
- Create safe space for questions

---

## 💡 Teaching Philosophy

### Core Principles
1. **Mistakes are valuable**: Create safe space to fail
2. **Active learning**: Students do, don't just watch
3. **Scaffolded support**: Start guided, end independent
4. **Real-world context**: Use actual earthquakes
5. **AI as tool**: Normalize and guide its use
6. **Collaborative**: Learn from each other

### Your Role
- **Guide, not lecturer**: Facilitate discovery
- **Debugger-in-chief**: Help solve problems
- **Enthusiasm generator**: Show excitement
- **Safety net**: Ensure no one gets lost
- **Role model**: Show how you learn/work

---

## 📝 Post-Class Actions

### Immediately After
- [ ] Save all notebook outputs
- [ ] Note what worked/didn't
- [ ] Respond to urgent questions
- [ ] Back up any student work

### Within 24 Hours
- [ ] Send follow-up email with resources
- [ ] Post solutions to exercises
- [ ] Review feedback survey
- [ ] Update materials based on feedback

### Before Next Session
- [ ] Revise lesson plan as needed
- [ ] Prepare Day 2 materials
- [ ] Grade homework (if applicable)
- [ ] Send reminder email

---

## 🎯 Success Indicators

### During Class
✅ Most students smiling and engaged  
✅ Questions are about content, not just tech issues  
✅ Students helping each other  
✅ You hear "That's so cool!" or "Wow!"  
✅ Time flies by

### After Class
✅ Students ask when next session is  
✅ They continue working after class  
✅ High survey satisfaction scores  
✅ Students report to colleagues/friends  
✅ You feel energized, not drained

---

## 📚 Additional Resources for Instructors

### Pedagogical Background
- Active Learning in STEM
- Constructivist Teaching Methods
- AI in Education research

### Technical Resources
- ObsPy documentation
- IRIS webinars
- Seismological Society education materials

### Community
- Instructor discussion forum
- ObsPy mailing list
- Seismology education network

---

**Remember: Your goal is not perfection, but progress. Make it fun, make it accessible, and students will thrive!** 🌟

---

## 🔄 Continuous Improvement

After each class:
1. What worked well? Do more of it.
2. What didn't work? Fix or remove it.
3. What surprised you? Investigate why.
4. What questions came up? Add to FAQ.
5. How can AI tools help more? Integrate better.

**Teaching is learning. Each class makes you better!** 🚀

