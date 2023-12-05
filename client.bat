@echo off

title Serve the snips through localhost

call env\Scripts\activate > nul
call python client.py 
call deactivate > nul