# getHtmlCode
Get the source code (html code) of a website

# Why Edge ?

I have choose the edge browser because it the pre-installed browser in windows 10

# how can I change it ?

If you want use another webbroser, download the driver and, in the main.py change:
```
driver = webdriver.Edge(executable_path="msedgedriver.exe")
```
by:
```
driver = webdriver.Edge(executable_path="pathAndDriverName")
```

# How to run it

"pip install selenium" and run main.py
