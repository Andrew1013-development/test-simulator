---
layout: post
title: Introduction
date: 2023-06-20 14:10:44 +0700
categories: jekyll update
youreded: /assets/images/the-first-post/aaaa.gif
---
Welcome to my first blog post on my own blog!
I'm Andrew1013, the main developer behind the `test-simuluator` project, and this is the test-blog, a blog that I created with the help of Jekyll 
(still trying to figure it out since this is my first foray into blogging and web development as a whole)

### Who is Andrew1013?

### test-simulator's Introduction and Origin of Development
`test-simulator` started out as a sorting script I use for sorting video and image files into folders of dates i shoot them. It is a trivial matter ***if and only if*** it was only a couple files or there was only 1 date of files in the parent folder. 

Now if the same parent folder contains **thousands (and thousands)** of files......*(you see where this is going now?)*

![aaaa](/images/the-first-post/aaaa.gif)

So, I embarked on a journey to automate this *grueling* process....

And here it is, the first piece of code i wrote for this "mini-utility" of mine:
```python
import os
import shutil

#variable
folder_name_list = []
folder_name_prev = ""
total_file_count = 0

#fetch from filenames
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        folder_name_pres = filename[0:8]
        if (folder_name_pres != folder_name_prev):
            folder_name_list.append(f"{folder_name_pres[0:4]}-{folder_name_pres[4:6]}-{folder_name_pres[6:8]}")
            folder_name_prev = folder_name_pres
        total_file_count += 1

#creating folders
for folder_name in folder_name_list:
    if debug_full:
        print(f"Creating {os.path.join(directory,folder_name)}")
    try:
        os.makedirs(os.path.join(directory,folder_name),exist_ok=True)
    except OSError:
        print("Cannot create sorting directories")
        exit(1)

# moving files
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        old_path = os.path.join(directory,filename)
        new_path = os.path.join(directory,f"{filename[0:4]}-{filename[4:6]}-{filename[6:8]}\\{filename}")
        print(f"Moving {old_path} to new_path")
        shutil.move(old_path,new_path)
```

Anything similiar?

> Yes, it's the same core function as the test-simulator's `file_sorter.py`: 

*because it's derived from that mini-utility!*