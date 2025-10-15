# Development Log

In this file, I will document my daily progress, challenges faced, and resources used while working on the project.

---

## [16-09-2025]

**What I did:**  
- Created the initial project structure and set up a GitHub repository.
- Scanned through the instructions and planned what to learn.
- Started researching the `psutil` library to understand its capabilities for system monitoring.

**Directions considered:**  
- Reading through the `psutil` documentation to understand how to fetch CPU and memory usage.

**Bugs encountered:**  
- None so far.

**Resources used:**  
- ChatGPT with the prompt: "what's psutil and how do I use it in python, for what and such".
- used the [psutil documentation](https://psutil.readthedocs.io/en/latest/) to understand how to fetch CPU and memory usage.

---

## [21-09-2025]


**What I did:**
- After finishing reading the psutil documentation, I moved on to the next topic. - I prompted ChatGPT to explain the libraries mentioned in the project description, specifically `psutil`, `rich` and `curses`, to have a better understanding of their functionalities and how they can be integrated into the project.
- ChatGPT recommended starting with `rich` for creating a colored terminal UI, as it is more user-friendly and modern compared to `curses` (which it noted is more low-level, complex, and not cross-platform).
- The AI also recommended looking into `argparse` and `logging` libraries for handling command-line arguments and logging functionalities, respectively.
- As noted - I have never encountered all of the mentioned libraries before, so I will need to spend some time learning them.

---

## [09-10-2025]

**What I did:**
- Started working on the basic functionality of the SysMon tool. I looked online for examples of how to use `psutil` to fetch CPU, memory, and disk usage statistics.
- Implemented a simple script that retrieves and prints the current CPU and memory usage to the console.

---

## [12-10-2025]

**What I did:**
- Added command-line argument parsing using the `argparse` library. This allows users to specify options like update interval and the number of bars for the usage display.
- Added the disk usage monitoring feature 
- Improved the code structure by organizing functions and adding comments for better readability.
- Added logging functionality using something simpler than the `logging` library, just to get started. I created a simple logger that writes CPU, memory, and disk usage data to a CSV file at specified intervals.

## [15-10-2025]

**What I did:**
- Made the main.py a bit more simpler, removed the UI parts and created a separate file for the UI (ui.py).
- Started working on the UI using the `rich` library. Created a basic layout that displays CPU, memory, and disk usage.
- This part was done with a bit of AI help, as I am not familiar with the `rich` library.