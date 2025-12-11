import cv2
import numpy as np
import streamlit as st
from ultralytics import YOLO

# SET PAGE
st.set_page_config(layout="wide", page_title="Traffic Counter")

#Load the Model
model = YOLO('yolov8n.pt')

#Define items to track and their colors
items_to_track = {
    "person":     (0, 255, 0),    # Green
    "car":        (255, 0, 0),    # Blue
    "truck":      (0, 0, 255),    # Red
    "bicycle":    (0, 255, 255),  # Yellow
    "motorcycle": (255, 0, 255),  # Magenta
}

def process_frame(frame, unique_ids_log):
    # TRACKING LOGIC
    results = model.track(frame, persist=True, verbose=False)[0]

    if results.boxes.id is not None:
        boxes = results.boxes.xyxy.cpu().numpy().astype(int)
        track_ids = results.boxes.id.int().cpu().tolist()
        class_indices = results.boxes.cls.int().cpu().tolist()
        
        for box, track_id, class_idx in zip(boxes, track_ids, class_indices):
            class_name = results.names[class_idx]
            
            # Normalize class name
            key_name = "motorcycle" if class_name == "motorbike" else class_name

            if key_name in items_to_track:
                unique_ids_log[key_name].add(track_id)

                # Draw Box & Label
                color = items_to_track.get(key_name, (255, 255, 255))
                x_min, y_min, x_max, y_max = box
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)
                
                label = f"{class_name} #{track_id}"
                cv2.putText(frame, label, (x_min, y_min - 5), 
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, color, 1)

    #LIVE COUNT BOARD
    height, width, _ = frame.shape
    
    # board size
    box_width = 250
    box_height = len(items_to_track) * 40 + 10
    start_x = width - box_width
    start_y = height - box_height
    
    if start_y >= 0 and start_x >= 0:
        sub_img = frame[start_y:height, start_x:width]
        black_rect = np.zeros(sub_img.shape, dtype=np.uint8)
        res = cv2.addWeighted(sub_img, 0.5, black_rect, 0.5, 1.0)
        frame[start_y:height, start_x:width] = res

        y_offset = start_y + 35
        for item_name, color in items_to_track.items():
            total_count = len(unique_ids_log[item_name])
            display_text = f"{item_name.capitalize()}: {total_count}"
            cv2.putText(frame, display_text, (start_x + 10, y_offset), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            y_offset += 40

    return frame

# STREAMLIT APP LAYOUT
st.title("Continuous Traffic Counter")

video_path = "moving_vehicle.mp4"

try:
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        st.error(f"Error: Could not open video file '{video_path}'. Check the path.")
    else:
        
        stframe = st.empty()
        
        unique_ids_log = {name: set() for name in items_to_track}
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break 
            
            processed_frame = process_frame(frame, unique_ids_log)
            frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            
            # use_column_width=True makes it fill the new wide layout
            stframe.image(frame_rgb, channels="RGB", use_column_width=True)
            
        cap.release()
        st.success("Video processing complete.")
        st.write("### Final Counts:")
        st.json({k: len(v) for k, v in unique_ids_log.items()})

except Exception as e:
    st.error(f"An error occurred: {e}")