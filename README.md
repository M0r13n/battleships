# Battleships
A simple battleship game implemented in less than 500 lines of Python.

![alt text](https://github.com/M0r13n/battleships/blob/master/img/a.png "demo picture")

# Installation
Just clone this repo and you are ready to rumble. There are no additional dependencies (besides Python3 itself).
```sh
~ git clone https://github.com/M0r13n/battleships.git
```

# Usage
You can now start the game by running:
```sh
~ python client.py
```
You can then decide to either start the game as a server or as a client. 

There are two boards displayed. 
The left displays your ships and their hits. 
The right shows your past shots, which can either be hits or misses.


| Color            | Meaning        |
|------------------|----------------|
| Black/ white     | Empty Field    |
| Green            | Own Ship       |
| Green with red X | Own Ship Hit   |
| RED              | Enemy Ship Hit |
| Yellow           | Miss           |


# Technical details
The game uses a TCP/IP socket to enable point to point communication between two players.
It uses a simple protocol which consists of only two bytes.
```
+-------+-------+-------+---------+
|   X   |   Y   |  Hit  | Padding |
+-------+-------+-------+---------+
| 4 Bit | 4 Bit | 1 Bit | 7 Bit   |
+-------+-------+-------+---------+
```
In fact the protocol is so simple that is easy to use other kinds of communication, such as ICMP packets. Just replace the Networking class and you are good to go.
