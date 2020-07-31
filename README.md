# Safest Path Finder

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/release/python-370/)

<br />
<p align="center">
  <a href="https://github.com/matthew3hansen/DSA_Project_3">
    <img src="Background%20images/better_visual.png" alt="Logo" width="500">
  </a>
  <br />


## Table of Contents

- [Motivation](#Motivation)
- [Features](#Features)
- [Getting Started](#Getting-Started)
  - [Prerequisites](#Prerequisites)
  - [Software/Libraries](#Software/Libraries)
  - [Python 3.8 Installation tips)(#Python-3.8-Installation-tips)
  - [Pygame Library Installion tips](#Pygame-Library-Installion-tips)
 - [Running the Program](#Running-the-Program)
   - [Getting Visual or Readable Directions](#Getting-Visual-or-Readable-Directions)
 - [What's next for Safest Path Finder?](#What's-next-for-Safest-Path-Finder?)
 - [References](#References)
   
 
  

### Motivation

In the wake of Covid-19 and social unrest, crime rates are steadily increasing, especially in urban areas. Walking somewhere could be especially dangerous if the person isn't aware of the current crime rates in the area.

### Features

The safest path finder maps out the safest and shortest path using Dijstra's Shortest Path algorithm. We have implemented a crime rate generator that assigns specific areas with the current crime rate on a scale of 1-10. We also have implemented a simulator that maps out the route to the destination.



## Getting started

To start using our program, you must download this github repo to your preferred directory by either downloading the zip file or cloning our repo by using the command below

``` git clone https://github.com/matthew3hansen/DSA_Project_3/edit/master/README.md	```

If you dont already have python installed you must install a version of python 3.0 or above along with the pygame library.




## Prerequisites
### Software/Libraries

- [Pygame](https://www.pygame.org/) 
- [Python3.8](https://www.python.org/downloads/)


### Python 3.8 Installation tips

Our project requires python 3.0 and above. To check your version of python you can use this command into your terminal window.
``` 
python --version
```

You can download the latest version of python directly from this website [Python3.8](https://www.python.org/downloads/)


### Pygame Library Installion tips
We recomend installing pygame to avoid any conflicts with running the simulator. There has been some issues with runnning pygame on MacOS so this forum might help with the installation (https://stackoverflow.com/questions/52718921/problems-getting-pygame-to-show-anything-but-a-blank-screen-on-macos-mojave)

In order to download the Pygame Library you can use this command in your terminal
```
pip install pygame
```

## Running the Program

Download the zip file, unzip the zipfile and enter to the folders current directory where main.py is found.
Then enter this command to start the program.

```python3
python3 main.py
```

#### Getting Visual or Readable Directions

**Step 1: **
You should recieve this text in the command window after starting the program with the previous command

```
Enter "1" to begin a shortest-path search, enter "2" to configure options, enter "exit" to exit:

```

**Step 2: **
Entering 1 into the command window should give another line of options

```
Enter 	"1" to perform visual GUI shortest-path search (small grid)
	      "2" to perform text-based shortest path search (large grid)
      	"3" to perform text-based multiple shortest paths search (large grid)
      	"cancel" to return to the main menu
(type in here):

```

*Visual Directions: Entering 1 in your command window will allow you to get visual directions of a subset of the full map*


*Readable Directions: Entering 2 or 3 will allow you to get readble directions of the full scale map*



**Step 3: **
Entering 1 into the terminal will display the main menu of the visual. It should look like


<br />
<p align="center">
  <a href="https://github.com/matthew3hansen/DSA_Project_3">
    <img src="Background%20images/home_screen.png" alt="Logo" width="500">
  </a>
  <br />


Follow the directions accordingly on the main screen to play the game!
(Note the visual map shows a sub-graph of the original map so it is easier to visualize!)



### What's next for Safest Path Finder?


## References

*[YouTube Video] ()

