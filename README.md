# TrafficLightAnalysis
🚦 Excited to share a traffic signal analysis project using computer vision! 🌟

I've created a program to detect and analyze traffic light signals in a video using OpenCV and Python. This project showcases real-time color analysis of traffic lights to determine their status (Red or Green). Here’s a snapshot of how it works:

⚙️ Key Components:

OpenCV: Used for video capture, image processing, and color analysis.
Numpy: Manipulating arrays for pixel-level operations.
Matplotlib: Visualizing results (though not shown here).
📹 Workflow:

Video Capture: Reads frames from a specified video file.
Frame Processing: Masks the region around the traffic light to isolate it.
Color Analysis: Detects either 'Red' or 'Green' based on color intensity thresholds.
Visualization: Displays the processed frame with detected traffic light status.
