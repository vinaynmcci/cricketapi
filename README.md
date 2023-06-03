# cricketlib

This is a Python library to control MCCI USB Switches.

### Install Python package
install python package from [python.org](https://www.python.org/ftp/python/3.7.8/python-3.7.8.exe)

### Install pip package
```shell
pip --version
python -m pip install --upgrade pip
```

### Prerequisites for running or building

<strong>On Windows:</strong>

Development environment

* OS - Windows 10 and 11 64 bit
* Python - 3.7.8
* pyserial - 3.5
* pip install wmi
* pip install hidapi

```shell
pip install pyserial
pip install wmi
pip install hidapi == 0.11.2 or pip install hidapi
```

### Installing cricketlib Packages

1.  Clone the repository from [github](https://github.com/mcci-usb/cricketlib)

2.  Open a `cmd terminal` and change directory to  `{path_to_repository}/cricketlib`. using `cd` into the root directory where setup.py is located

3.  To install the library in your local Python setup, enter the command in Windows OS
```bash
python setup.py install
```

### create .egg file.
once install the setup.py, it's created the .egg file succcessfully.
Please navigate to dist/ directory and you will find the files .egg file.
Example: `cricketapi-1.0.0-py3.7.egg`

### RUN main.py function
once install the egg file.
- Go to the `cricketlib` folder
- RUN `main.py` script in cmd prompt uisng cmd line arguments.
### cmd line arguments
- argc 1 : `main.py`
- argc 2 : `switch`
- argc 3 : `vid`
- argc 4 : `pid`
- argc 5 : `delay`
- argc 6 : `repeat`

### Exmaple of cmd for RUN main.py

```shell
# python main.py <switch> <vid> <pid> <delay> <repeat>
python main.py 3141 046D C077 2000 100
```
```python
# import lib for switch3142, switch3201
from cricketlib import switch3141
from cricketlib import switch3201
```
```python
# found a list of available switches.
# using the port number open the switch.
dev_list = searchswitch.get_switches()
print(dev_list)
```

### Connect the USB Switch to particular Switch.
``` python
# Connect the USB Switch
sw1.connect()
```
### port on command.
```python
# port on with port number
sw1.port_on(1) #first port ON
sw1.port_on(2) #second port ON
```
### port off command
```python
sw1.port_off()
```





