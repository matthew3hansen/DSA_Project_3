# Safest Path Finder

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/release/python-370/)

<br />
<p align="center">
  <a href="https://github.com/matthew3hansen/DSA_Project_3">
    <img src="Background%20images/better_visual.png" alt="Logo" width="500">
  </a>
  <br />


### Demo/Intro Link (https://www.youtube.com/watch?v=2Z9Ud5UKPZs&feature=youtu.be)

 

### Motivation

In the wake of Covid-19 and social unrest, crime rates are steadily increasing, especially in urban areas. Walking somewhere could be especially dangerous if the person isn't aware of the current crime rates in the area. As UF students, we have seen how walking home can be very dangerous, especially when there are UF alerts that notify us when there is a current crime such as a robbery, shooting or sexual assualt in the area. Safest Path Finder is meant to be a guardian angel that can help those get home safely.

### Features

- The safest path finder maps out the safest and shortest path using Dijstra's Shortest Path algorithm
- A crime rate generator that assigns specific areas with the current crime rate on a scale of 1-10
- A single / multiple visual path finder, that allows for the user to find single or multiple safe paths visual on the GUI
- Readable directions in the console, alternate way of getting directions instead of visually.
- Configurable Options for a user to get generated street names instead of coordiates on grid.


---

## Table of Contents
- [Demo/Intro Link](#Demo/Intro-Link)
- [Motivation](#Motivation)
- [Features](#Features)
- [Getting Started](#Getting-Started)
  - [Prerequisites](#Prerequisites)
  - [Software/Libraries](#Software/Libraries)
  - [Python 3.8 Installation tips](#Python-3.8-Installation-tips)
  - [Pygame Library Installion tips](#Pygame-Library-Installion-tips)
 - [Running the Program](#Running-the-Program)
   - [Getting Visual or Readable Directions](#Getting-Visual-or-Readable-Directions)
 - [Visualization and Console Output](#Visualization-and-Console-Output)
   - [Visual of Multiple Paths with Crime](#Visual-of-Multiple-Paths-with-Crime)
   - [Visual of Single Path with Crime](#Visual-of-Single-Path-with-Crime)
   - [Visual of Single Path without Crime](#Visual-of-Single-Path-without-Crime)
   - [Getting Readable Directions in the Console](#Getting-Readable-Directions-in-the-Console)
   - [Configuring Options](#Configuring-Options)
 - [What's next for Safest Path Finder?](#What's-next-for-Safest-Path-Finder?)
 - [References](#References)




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

**Step 1:**
You should recieve this text in the command window after starting the program with the previous command

```
Enter "1" to begin a shortest-path search, enter "2" to configure options, enter "exit" to exit:

```

**Step 2:**
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



**Step 3:**
Entering 1 into the terminal will display the main menu of the visual. It should look like


<br />
<p align="center">
  <a href="https://github.com/matthew3hansen/DSA_Project_3">
    <img src="Background%20images/home_screen.png" alt="Logo" width="500">
  </a>
  <br />


Follow the directions accordingly on the main screen to play the game!
(Note the visual map shows a sub-graph of the original map so it is easier to visualize!)

# Visualization and Console Output

## Visual of Multiple Paths with Crime

<br />
<p align="center">
  <a href="https://github.com/matthew3hansen/DSA_Project_3">
    <img src="Background%20images/MultiplePaths.png" alt="Logo" width="500">
  </a>
  <br />

## Visual of Single Path with Crime

<br />
<p align="center">
  <a href="https://github.com/matthew3hansen/DSA_Project_3">
    <img src="Background%20images/better_visual.png" alt="Logo" width="500">
  </a>
  <br />

## Visual of Single Path without Crime
<br />
<p align="center">
  <a href="https://github.com/matthew3hansen/DSA_Project_3">
    <img src="Background%20images/SinglePathWithoutCrime.png" alt="Logo" width="500">
  </a>
  <br />
	
	
## Getting Readable Directions in the Console

<br />
<p align="center">
  <a href="https://github.com/matthew3hansen/DSA_Project_3">
    <img src="Background%20images/ConsoleOutput.png" alt="Logo" width="500">
  </a>
  <br />
	
To get readable directions, you can input 2 or 3 in step 2. You must enter the correct coordinate or stree intersection to be able to find directions to your destination.


## Configuring Options

To configure options you can enter 2 at **Step 1** and enter your preferred specifications:

```
Enter "1" to begin a shortest-path search, enter "2" to configure options, enter "exit" to exit: 2

Enter	"1" to enable street-names (e.g. "Chevrolet / Wilson"),
	"2" to enable index numbers as street names (e.g. "0 / 0"),
	"cancel" to cancel
(type in here): 1
```



---

### What's next for Safest Path Finder?

This program isn't suited for the real world yet, rather it is just a simple visualization or outline of what could be made if further time was allocated. If we had more time to do the project, we probably would implement this as an IOS/Andriod app and using Google's map API to enhance the user's experience and further simulate the real world enviroment. We could probably pitch the idea for a company that would want to implement a project like this.




## References

[Python] (https://www.python.org/downloads/release/python-370/)

[Pygame] (https://www.pygame.org/) 

