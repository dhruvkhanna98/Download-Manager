# Downloads Manager

I started to feel like my downloads folder was too cluttered so I wrote this Python script to sort incoming Downloads to Folders Based on 
file extensions for easy removal/access. 

I utilized the Watchdog Python Library, to implement the Observer Pattern and create a custom handler to sort incoming downloads to
Folders named by extensions (Folders are created automatically when needed). Moreover, I use a standard python dictionary to keep a track 
of folders (for extensions) created so far for O(1) access in future. 

Currently working to expand functionality to automatically deleting files which haven't been used in the past 3 months.
