# WinOSparser
Parser for Windows registry that supports current and old installations/upgrades. This could be helpful in digital forensics and investigations. I considered this beta I've tested this on 10+ installations without a problem.

Current operating system information is located in <b>SOFTWARE\Microsoft\Windows NT\CurrentVersion </b> <br/>
The old installations are located <b>SYSTEM\Setup\Source OS (Updated on xx/xx/xxxx xx:xx:xx)</b>
<h2>Usage</h2>
<p>Coded in Python3. <br/>
WinOSparser.py SYSTEM SOFTWARE <br/>
  or<br/>
python3 WinOSparser.py SYSTEM SOFTWARE<br/>
</p>
<h2>Screenshots</h2>
<a href="Screenshot WinOSparser"><img src="https://github.com/dfirdoctor/WinOSparser/blob/master/image/WinOSparser.png?raw=true" width="732" height="495" style="max-width:100%;"></a>

<h2>Research</h2>
I've done some minor research on when and how the keys are updated. Coming soon.

<h2>Credits</h2>
Willi Ballenthin (Windows Registry library) <br/>
Glenn P. Edwards Jr (reused code)
