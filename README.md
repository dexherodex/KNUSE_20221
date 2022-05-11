KNU SE-20221 Team Four: LOC Metrics Counter
============================================

How To Run Program
---------------------
* ### Environment
   1. Check python version
         ```bash
         python --version
         ```
         or
         ```bash
         python3 --version
         ```
   2. If python version lower than 3, then install ***python3***.
  
  + Linux
     + On Debian derivatives such as Ubuntu, use apt.
          ```bash
          sudo apt-get install python3
          ```
     + On Red Hat and derivatives, use yum.
          ```bash
          sudo yum install python3
          ```
     + On SUSE and derivatives, use zypper.
          ```bash
          sudo zypper install python3
          ```
  + Mac OS
  
     Download link: https://www.python.org/downloads/macos/
  
  + Windows
  
     Download link: https://www.python.org/downloads/windows/
---
* ### Clone
    1. Use the ***cd*** to move into the directory where you want to save the clone. For example:
         ```bash
         cd YourDirectoryForClone
         ```
    2. Enter the ***git clone URL*** command.
          ```bash
          git clone https://github.com/dexherodex/KNUSE-20221-4-TeamFour.git
          ```
---
* ### Execute Program
     (***Windows*** needs to install ***Windows Subsystem for Linux*** for running ***Shell Script*** file.)
    * ## metric_counter.py
    1. Use the ***cd*** to move into the cloned directory.
          ```bash
          cd KNUSE-20221-4-TeamFour/metric_counter
          ```
    2. Enter the ***chmod*** command to change the permission of ***metric_counter.sh***.
          ```bash
          chmod 755 ./metric_counter.sh
          ```
    3. Run the program with ***in.file*** and ***out.file***. (The ***in.file*** must be written by ***python***.)
          ```bash
          ./metric_counter.sh in.py out.file
          ```
    
    * ## complexity_counter.py
    1. Use the ***cd*** to move into the cloned directory.
          ```bash
          cd KNUSE-20221-4-TeamFour/complexity_counter
          ```
    2. Enter the ***chmod*** command to change the permission of ***metric_counter.sh***.
          ```bash
          chmod 755 ./complexity_counter.sh
          ```
    3. Run the program with ***in.file*** and ***out.file***. (The ***in.file*** must be written by ***python***.)
          ```bash
          ./complexity_counter.sh complexity.py out.file
          ```
---
Language
--------
+ Implementation Language: Python
+ Target Language:   Python
---

About Sample Files
--------------------
+ The ***in.py*** file in ***metric_counter*** is a clone of https://github.com/kakao/khaiii/blob/master/src/main/python/khaiii/khaiii.py
+ The ***complexity.py*** file in ***complexity_counter*** is a clone of https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/binary_search_tree.py
---
