# 🚗 Real-Time Traffic Object Counter (YOLO11 & Streamlit)

A computer vision application that detects, tracks, and counts vehicles and pedestrians in video footage using the **YOLO11 Medium** model. The application features a continuous counting system (cumulative totals) and displays the video feed on a responsive web dashboard using **Streamlit**.

## 🌟 Features

* **Advanced Detection:** Uses **YOLO11m (Medium)** for high accuracy on fast-moving objects.
* **Object Tracking:** Implements **ByteTrack** (`tracker="bytetrack.yaml"`) to maintain unique IDs for objects across frames.
* **Continuous Counting:** Counts unique objects (Car #1, Car #2) rather than just frame-by-frame instances.
* **Live Dashboard:** Visualizes the video processing in real-time with a dynamic count board overlay.
* **Wide Mode Support:** Automatically adjusts to full-screen width for better visibility.
* **Classes Tracked:**
    * 🟢 Person
    * 🔵 Car
    * 🔴 Truck
    * 🟡 Bicycle
    * 🟣 Motorcycle

## 🛠️ Tech Stack

* **Python 3.11**
* **Ultralytics (YOLO11)** - For object detection and tracking.
* **Streamlit** - For the web interface and video display.
* **OpenCV (cv2)** - For image processing and drawing overlays.

## ⚙️ Installation

1.  **Clone the repository** (or navigate to your project folder):
    ```bash
    cd Traffic_control_detection
    ```

2.  **Install the required dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install ultralytics streamlit opencv-python
    ```

    *Note: If you have slow internet and the download fails, use:*
    ```bash
    pip install --default-timeout=1000 ultralytics
    ```

**Francis Afful Gyan**    
📧 Email: francisaffulgyan@gmail.com  
🔗 LinkedIn: [https://www.linkedin.com/in/francis-afful-gyan-2b27a5153/]  
📅 Date: December 2025

---

**🌐 Live Demo**: [https://medoptix-analytics.streamlit.app/](https://medoptix-analytics.streamlit.app/)

**📊 Project Status**: Active Development

**⭐ If you find this project useful, please consider giving it a star!**

## Thank You
![Thank You](Thankyou1.png)
