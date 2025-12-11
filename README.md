# 🚗 Real-Time Traffic Object Counter (YOLOv8)

A computer vision application that detects, tracks, and counts vehicles and pedestrians in video footage using the **YOLOv8** model. The application features a continuous counting system (cumulative totals) utilizing object tracking technology to ensure accurate data collection.

## 🌟 Features

* **Advanced Detection:** Uses **YOLOv8** for high accuracy and real-time performance.
* **Object Tracking:** Implements **ByteTrack** (`tracker="bytetrack.yaml"`) to maintain unique IDs for objects across frames.
* **Continuous Counting:** Counts unique objects (Car #1, Car #2) rather than just frame-by-frame instances.
* **Visual Overlay:** Visualizes the video processing in real-time with a dynamic count board overlay.
* **Classes Tracked:**
    * 🟢 Person
    * 🔵 Car
    * 🔴 Truck
    * 🟡 Bicycle
    * 🟣 Motorcycle

## 🛠️ Tech Stack

* **Python 3.11**
* **Ultralytics (YOLOv8)** - For object detection and tracking.
* **OpenCV (cv2)** - For image processing, video manipulation, and drawing overlays.

## ⚙️ Installation

1.  **Clone the repository** (or navigate to your project folder):
    ```bash
    cd Traffic_control_detection
    ```

2.  **Install the required dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install ultralytics opencv-python
    ```

    *Note: If you have slow internet and the download fails, use:*
    ```bash
    pip install --default-timeout=1000 ultralytics
    ```

---

**Francis Afful Gyan** 📧 Email: francisaffulgyan@gmail.com  
🔗 LinkedIn: [Francis Afful Gyan](https://www.linkedin.com/in/francis-afful-gyan-2b27a5153/)  
📅 Date: December 2025

---

**📊 Project Status**: Active Development

**⭐ If you find this project useful, please consider giving it a star!**

## Thank You
![Thank You](Thankyou1.png)