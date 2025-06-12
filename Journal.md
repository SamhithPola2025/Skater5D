## Journal: This is where I post all updates!

# Day 1:
~ 4.5 hrs
I made some CAD stuff in OnShape, I made the rails and the hinge with wheels, this took a while in OnShape and is pretty much the textbook definition of "harder than it looks". I also decided on my parts and full design. I had to measure and look at different screws before coming to a conclusion, I also measured my skateboard dimensions exactly and did a lot of math. ![image](https://github.com/user-attachments/assets/9870e610-06cf-48e0-83f9-0a7853ed46b5) ![image](https://github.com/user-attachments/assets/cdd1107d-787a-4e14-af93-58a5deb9090d) ![image](https://github.com/user-attachments/assets/1db342b4-5084-424b-9297-d9374f8e111f)

# Day 2:
~ 5.25 hrs
I made the entire schematic with a bunch of tweaks and stuff, I also assigned the footprints. The main issue was getting the perfect parts and doing a lot more research on the perfect footprints. I also planned how the PCB is going to look so later I can get work done really fast. ![image](https://github.com/user-attachments/assets/7240da28-e8b1-4c0a-bd36-5b9a4555aee1) ![image](https://github.com/user-attachments/assets/bc527cbe-ecf5-4e82-a7b6-c3124bb8ac4a)
 I also made a lot of edits with the wiring to make sure that I could access all the sensors properly. I looked through a lot of documentation to make sure that everything was in the right place and the wires were meant to be and I had to add pullups and capacitors in the right place or everything would be absolutely fried when I put it together.

# Day 3:
~ 5.75 hrs
A LOT of schematic reworking and error solving. I had to go back into the schematic multiple times to fix wiring issues and voltage logic problems. After that I moved on to the PCB design, but that also went through a bunch of reworks — spacing, trace width, pad clearance issues, component repositioning. It took forever to get it clean and actually manufacturable, and every small fix led to new issues somewhere else. Mentally draining but productive.

# Day 4:
~ 4 hrs
Today was CAD-heavy. I improved the rail design and made the mount for the PCB after exporting the 3D model from the board. Of course, with CAD comes math — and I had to revise a bunch of my earlier measurements because they were slightly off. I added more components to the PCB including LEDs and switches, and started working on the BOM (not completed yet). Overall, it’s starting to feel like a real system now.

To complete:
	•	BOM
	•	Firmware
	•	CAD with math (a little revisions to do since my calculations were off)
    •   Formatting the files to match the normal format

# Day 5:
~ 5 hrs
Today marks the final official day of this sprint, and honestly, it feels both satisfying and slightly open-ended — like there’s more to chase, which I kind of like.

What I Did Today
	•	Switched from mock code to real code for my skateboard motion classifier
	•	Set up the MicroPython script on the ESP32-S3 Mini-1 to stream real-time data from the MPU6050 sensor
	•	Built the full PC-side classifier using fastdtw, NumPy, and matplotlib to detect tricks from motion patterns
	•	Planned out how I’ll record ollie/kickflip patterns for training

Even though I don’t have the physical hardware yet, I now have a fully working pipeline from board → sensor → ESP32 → serial → real-time visualization → classification.

What I Learned
	•	How to structure embedded + host code together in a real hardware project
	•	That real-time classification is way more intuitive when you can visualize the data
	•	That using DTW to match time-series patterns actually works better than I expected
	•	The small details (like loading different .npy files or managing buffer sizes) really matter in signal-based ML

How I Felt

Honestly? Mixed. Hack Club cancelling the event hit my motivation for a bit. It felt like the “why” was gone. But I remembered this wasn’t about a prize — I’m building something that moves between the digital and physical world, and that’s always been fun to me. That feeling came back.

Final Thoughts

This isn’t really the end. I’m still gonna finish the trick recorder, build out more classifiers, and solder the board when it arrives. This log just marks the end of the first version. I finally feel like I’m doing a real hardware/software fusion project — and this time, I didn’t just start it, I stuck with it.

TL;DR:
On Day 5, I wrapped up the core pipeline for my ESP32-based skateboard classifier. Even without hardware, I now have real code working end-to-end — this week taught me way more than just coding. When the PCBA arrives and I 3D print everything ill continue this journal, submitting to highway for now! I also have to tweak the /Users/samhithpola/Documents/GitHub/Skater5D/Production/Firmware/pc_trick_classifier/main.py file because it works for the raspberry pi, not the ESP32 S3 Mini-1, easy fix though!