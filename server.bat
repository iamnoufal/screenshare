@echo off

title Take snips and save to local

call env\Scripts\activate > nul
call python server.py
call deactivate > nul