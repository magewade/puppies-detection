import streamlit as st
from ultralytics import YOLO
from pathlib import Path
import tempfile
import shutil
import glob

model = YOLO("weights/best.pt")

st.title("YOLOv8 через Colab API 🚀")

option = st.radio(
    "Выберите, что вы хотите сделать:",
    (
        "Как это работает 🔎",
        "Инференсим трансляцию с YouTube 🐕‍🦺",
        "Загрузить видео для инференса 🐾",
    ),
)

if option == "Инференсим трансляцию с YouTube 🐕‍🦺":
    st.subheader("Трансляция с YouTube 🎥")
    st.video("https://www.youtube.com/watch?v=bYlEgU2tU5w")

elif option == "Как это работает 🔎":
    st.subheader("Посмотреть как работает модель")

elif option == "Загрузить видео для инференса 🐾":
    st.subheader("1. Выберите видео из галереи")

    demo_folder = Path("examples")
    demo_videos = list(demo_folder.glob("*.mov"))

    chosen_video = None
    cols = st.columns(3)
    for idx, video_path in enumerate(demo_videos):
        thumb_path = video_path.with_suffix(".png")
        if thumb_path.exists():
            with cols[idx % 3]:
                st.image(str(thumb_path), use_container_width=True)
                if st.button(f"Выбрать", key=str(video_path)):
                    st.session_state["chosen_demo"] = str(video_path)

    st.markdown("или")

    st.subheader("2. Загрузите своё видео")
    uploaded_video = st.file_uploader("Загрузите видео (.mp4)", type=["mp4"])
    input_video_path = None

    if uploaded_video:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(uploaded_video.read())
            input_video_path = temp_file.name
            st.session_state["chosen_demo"] = None
            st.video(input_video_path)

    elif "chosen_demo" in st.session_state:
        input_video_path = st.session_state["chosen_demo"]
        st.video(input_video_path)

    if input_video_path and st.button("🚀 Запустить инференс"):
        with st.spinner("Инференс..."):
            results = model.track(
                source=input_video_path,
                tracker="puppy_tracker.yaml",
                save=True,
                save_txt=False,
                project="runs",
                name="detect",
                exist_ok=True,
            )

            latest = sorted(glob.glob("runs/detect/*.mp4"))[-1]
            output_path = f"annotated_{Path(input_video_path).stem}.mp4"
            shutil.copy(latest, output_path)

            st.video(output_path)
            st.success("Готово! 🎉")
