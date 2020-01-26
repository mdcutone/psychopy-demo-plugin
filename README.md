# psychopy-demo-plugin

This project serves as a demonstration of how to make a plugin package for 
PsychoPy (https://www.psychopy.org/). **Note the plugin framework for PsychoPy 
is a WIP and is not currently available.**

Here we create a plugin which adds a method called `getArea` to the 
`psychopy.visual.Rect` class when loaded. 

A PsychoPy plugin is simply a Python package with metadata that advertises entry 
points to objects defined in a module. When a plugin is loaded, PsychoPy 
identifies entry points relevant to itself, and creates or reassigns attributes 
within its namespace to reference these objects. Any Python package can specify 
these entry points to add functionality to PsychoPy, without the need to create 
a separate plugin package.

You can install the package using:

```commandline
python setup.py install
```

You can also build packages and use `pip` to install them or put them up on a 
public repository for others to download. Running the following code will show 
the effect of the plugin package on `Rect`:

```python
from psychopy import visual, core, plugins
plugins.loadPlugin('psychopy-demo-plugin')  # load the plugin

win = visual.Window()  # create a window
rectStim = visual.Rect(win)  # create a Rect stim
print(rectStim.getArea())  # print the area using the method added by the plugin
rectStim.draw()  # draw the rectangle
win.flip()  # flip buffers
core.wait(5)  # Wait for 5 seconds and exit
win.close()
core.quit()
```
