# import streamlit as st
# from ultralytics import YOLO
# from pathlib import Path
# import tempfile
# import shutil
# import uuid
# import yt_dlp
# import subprocess
# import numpy as np
# import time


# model = YOLO("data/weights/best.pt")

# st.title("Трекинг щенков с YOLOv8 🐶")

# option = st.radio(
#     "Выберите, что вы хотите сделать:",
#     (
#         "Как это работает 🔎",
#         "Инференсим видео 🐾",
#         "Инференсим трансляцию с YouTube 🐕‍🦺",
#     ),
# )


# if option == "Инференсим трансляцию с YouTube 🐕‍🦺":
#     st.subheader("Инференс YouTube трансляции 🎥")

#     st.info(
#         "Это прямая трансляция, щенки могут устраивать совсем уж инфернальный хаос, спать или быть не в кадре :)"
#     )

#     st.video("https://www.youtube.com/watch?v=bYlEgU2tU5w")

#     def get_stream_info(youtube_url):
#         ydl_opts = {
#             "quiet": True,
#             "format": "best[ext=mp4]/best",
#         }
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(youtube_url, download=False)
#             return info["url"]

#     st.info("Инференс трансляции происходит с задержкой, так как YOLO обрабатывает каждый кадр")

#     youtube_url = "https://www.youtube.com/watch?v=bYlEgU2tU5w"
#     start_button = st.button("▶️ Начать инференс")

#     if start_button:
#         stream_url = get_stream_info(youtube_url)

#         # 🔧 Фиксированный размер
#         frame_width, frame_height = 1280, 720
#         st.success(f"Стрим подключен: {frame_width}x{frame_height}")

#         ffmpeg_cmd = [
#             "ffmpeg",
#             "-i",
#             stream_url,
#             "-vf",
#             f"scale={frame_width}:{frame_height}",
#             "-f",
#             "image2pipe",
#             "-pix_fmt",
#             "bgr24",
#             "-vcodec",
#             "rawvideo",
#             "-loglevel",
#             "quiet",
#             "-",
#         ]
#         pipe = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE)

#         frame_size = frame_width * frame_height * 3
#         placeholder = st.empty()
#         stop_button = st.button("⛔ Остановить")

#         while not stop_button:
#             raw_frame = pipe.stdout.read(frame_size)
#             if not raw_frame:
#                 st.warning("🚫 Поток завершён или прерван")
#                 break

#             frame = np.frombuffer(raw_frame, dtype=np.uint8)
#             if frame.size != frame_size:
#                 continue

#             frame = frame.reshape((frame_height, frame_width, 3))
#             results = model.track(
#                 source=frame, persist=True, tracker="configs/puppy_tracker.yaml", verbose=False, conf=0.4
#             )

#             annotated = results[0].plot() if results else frame
#             placeholder.image(annotated, channels="BGR", use_container_width=True)

#             time.sleep(0.1)

#         pipe.terminate()


# elif option == "Как это работает 🔎":
#     st.subheader("Как работает модель 🚀")

#     st.markdown(
#         """
#     **YOLOv8** — нейросетевая модель для детекции и трекинга объектов на видео.
#     Она способна быстро и точно находить собачек на кадрах и отслеживать их перемещение в реальном времени.

#     Для обучения модели я вручную разметила около пятисот кадров с изображениями щенков, указав точные позиции каждого животного.
#     Благодаря этому модель научилась самостоятельно выявлять и отслеживать собак на новых видео. Однако стоит помнить, что модели семейства YOLO чувствительны к изменениям формы отслеживаемых объектов.
#     Если объект сильно меняет позу или форму (например, щенок кувыркается или прячется), точность трекинга может снижаться.

#     Несмотря на это, даже на небольшом кастомном датасете можно добиться неплохих результатов!
#     """
#     )

#     st.markdown("Вот как это выглядит в действии:")

#     st.image(
#         "data/images/Untitled_V1-0001.gif",
#         caption="Беготня и обычные щеночьи дела 🐶",
#         use_container_width=True,
#     )

#     st.image(
#         "data/images/animation_V1-0003.gif",
#         caption="Куча-мала, быстрые изменения и хаос 🐕",
#         use_container_width=True,
#     )

#     st.image(
#         "data/images/animation_V1-0004.gif",
#         caption="Выход из кадра, движение и появление новых объектов 🐾",
#         use_container_width=True,
#     )

#     st.info("Модель: YOLOv8, трекер: BoT-SORT, обучение на кастомной выборке")


# elif option == "Инференсим видео 🐾":

#     output_dir = Path("inferenced_videos")
#     output_dir.mkdir(parents=True, exist_ok=True)

#     def clear_folder(folder: Path):
#         if folder.exists() and folder.is_dir():
#             for f in folder.iterdir():
#                 if f.is_file():
#                     f.unlink()
#                 elif f.is_dir():
#                     shutil.rmtree(f)

#     # Очищаем папку один раз при первом заходе на этот экран
#     if "cleared_output_dir" not in st.session_state:
#         clear_folder(output_dir)
#         st.session_state["cleared_output_dir"] = True

#     st.subheader("1. Выберите видео из галереи и запустите инференс")

#     demo_folder = Path("data/examples")
#     demo_videos = list(demo_folder.glob("*.mov")) + list(demo_folder.glob("*.mp4"))

#     output_dir = Path("inferenced_videos")
#     output_dir.mkdir(parents=True, exist_ok=True)

#     # Создаем отдельные папки для демо и загруженных видео
#     demo_output_dir = output_dir / "demo_detect"
#     demo_output_dir.mkdir(exist_ok=True)

#     uploaded_output_dir = output_dir / "uploaded_detect"
#     uploaded_output_dir.mkdir(exist_ok=True)

#     cols = st.columns(3)
#     for idx, video_path in enumerate(demo_videos):
#         thumb_path = video_path.with_suffix(".png")
#         if thumb_path.exists():
#             with cols[idx % 3]:
#                 st.image(str(thumb_path), use_container_width=True)
#                 if st.button(f"Выбрать", key=f"demo_select_{video_path}"):
#                     st.session_state["chosen_demo"] = str(video_path)
#                     # Очищаем остальные сессии
#                     st.session_state.pop("uploaded_video_path", None)
#                     st.session_state.pop("demo_output_path", None)
#                     st.session_state.pop("uploaded_output_path", None)

#     # Инференс для демо-видео
#     if "chosen_demo" in st.session_state:
#         demo_video_path = st.session_state["chosen_demo"]
#         st.video(demo_video_path)

#         if st.button("🚀 Запустить инференс", key="run_demo_inference"):
#             with st.spinner("Считаем щеночков..."):
#                 # Уникальное имя для новой папки результатов
#                 unique_name = f"annotated_demo_{uuid.uuid4().hex}"
#                 save_dir = demo_output_dir / unique_name
#                 save_dir.mkdir(parents=True, exist_ok=True)

#                 # Запуск модели
#                 results = model.track(
#                     source=demo_video_path,
#                     tracker="configs/puppy_tracker.yaml",
#                     save=True,
#                     save_txt=False,
#                     project=str(demo_output_dir),
#                     name=unique_name,
#                     exist_ok=True,
#                     conf=0.4
#                 )

#                 # После инференса находим новое видео
#                 mp4_files = sorted(save_dir.glob("*.mp4"))
#                 if mp4_files:
#                     latest = mp4_files[-1]
#                     output_path = save_dir / latest.name

#                     # Сохраняем путь к выведенному видео
#                     st.session_state["demo_output_path"] = str(output_path)
#                     st.success("Готово! 🎉")
#                 else:
#                     st.error("Ошибка: не найдено видео после инференса.")

#     # Показ результата инференса для демо-видео
#     if "demo_output_path" in st.session_state:
#         output_path = st.session_state["demo_output_path"]
#         st.video(output_path)

#         with open(output_path, "rb") as f:
#             st.download_button(
#                 label="📥 Скачать видео (демо)",
#                 data=f,
#                 file_name=Path(output_path).name,
#                 mime="video/mp4",
#                 key="download_demo_video",
#             )

#     # Загрузка собственного видео
#     st.subheader("2. Или загрузите своё видео")
#     uploaded_file = st.file_uploader(
#         "Загрузите видео (.mp4 или .mov)", type=["mp4", "mov"], key="upload_own_video"
#     )

#     if uploaded_file:
#         suffix = Path(uploaded_file.name).suffix
#         with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
#             temp_file.write(uploaded_file.read())
#             uploaded_video_path = temp_file.name
#             st.session_state["uploaded_video_path"] = uploaded_video_path
#             # Очищаем остальные сессии
#             st.session_state.pop("chosen_demo", None)
#             st.session_state.pop("demo_output_path", None)
#             st.session_state.pop("uploaded_output_path", None)

#         st.video(uploaded_video_path)

#     # Инференс для загруженного видео
#     if "uploaded_video_path" in st.session_state:
#         uploaded_video_path = st.session_state["uploaded_video_path"]

#         if st.button(
#             "🚀 Запустить инференс", key="run_uploaded_inference"
#         ):
#             with st.spinner("Считаем щеночков..."):
#                 results = model.track(
#                     source=uploaded_video_path,
#                     tracker="configs/puppy_tracker.yaml",
#                     save=True,
#                     save_txt=False,
#                     project=uploaded_output_dir,
#                     name="detect",
#                     exist_ok=True,
#                     conf=0.4
#                 )
#                 latest = sorted((uploaded_output_dir / "detect").glob("*.mp4"))[-1]
#                 output_path = output_dir / f"annotated_uploaded_{uuid.uuid4().hex}.mp4"
#                 shutil.copy(latest, output_path)
#                 st.session_state["uploaded_output_path"] = str(output_path)
#                 st.success("Готово! 🎉")

#     # Показ результата инференса для загруженного видео
#     if "uploaded_output_path" in st.session_state:
#         output_path = st.session_state["uploaded_output_path"]
#         st.video(output_path)
#         with open(output_path, "rb") as f:
#             st.download_button(
#                 label="📥 Скачать видео (загруженное)",
#                 data=f,
#                 file_name=Path(output_path).name,
#                 mime="video/mp4",
#                 key="download_uploaded_video",
#             )


import streamlit as st
from ultralytics import YOLO
from pathlib import Path
import tempfile
import shutil
import uuid
import yt_dlp
import subprocess
import numpy as np
import time


# Загрузка модели — путь к твоим весам
model = YOLO("data/weights/best.pt")

st.title("Трекинг щенков с YOLOv8 🐶")

option = st.radio(
    "Выберите, что вы хотите сделать:",
    (
        "Как это работает 🔎",
        "Инференсим видео 🐾",
        "Инференсим трансляцию с YouTube 🐕‍🦺",
    ),
)

if option == "Инференсим трансляцию с YouTube 🐕‍🦺":
    st.subheader("Инференс YouTube трансляции 🎥")

    st.info(
        "Это прямая трансляция, щенки могут устраивать совсем уж инфернальный хаос, спать или быть не в кадре :)"
    )

    st.video("https://www.youtube.com/watch?v=bYlEgU2tU5w")

    def get_stream_info(youtube_url):
        ydl_opts = {
            "quiet": True,
            "format": "best[ext=mp4]/best",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            return info["url"]

    st.info(
        "Инференс трансляции происходит с задержкой, так как YOLO обрабатывает каждый кадр"
    )

    youtube_url = "https://www.youtube.com/watch?v=bYlEgU2tU5w"
    start_button = st.button("▶️ Начать инференс")

    if start_button:
        stream_url = get_stream_info(youtube_url)

        frame_width, frame_height = 1280, 720
        st.success(f"Стрим подключен: {frame_width}x{frame_height}")

        ffmpeg_cmd = [
            "ffmpeg",
            "-i",
            stream_url,
            "-vf",
            f"scale={frame_width}:{frame_height}",
            "-f",
            "image2pipe",
            "-pix_fmt",
            "bgr24",
            "-vcodec",
            "rawvideo",
            "-loglevel",
            "quiet",
            "-",
        ]
        pipe = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE)

        frame_size = frame_width * frame_height * 3
        placeholder = st.empty()
        stop_button = st.button("⛔ Остановить")

        while not stop_button:
            raw_frame = pipe.stdout.read(frame_size)
            if not raw_frame:
                st.warning("🚫 Поток завершён или прерван")
                break

            frame = np.frombuffer(raw_frame, dtype=np.uint8)
            if frame.size != frame_size:
                continue

            frame = frame.reshape((frame_height, frame_width, 3))
            results = model.track(
                source=frame,
                persist=True,
                tracker="configs/puppy_tracker.yaml",
                verbose=False,
                conf=0.4,
            )

            annotated = results[0].plot() if results else frame
            placeholder.image(annotated, channels="BGR", use_container_width=True)

            time.sleep(0.1)

        pipe.terminate()

elif option == "Как это работает 🔎":
    st.subheader("Как работает модель 🚀")

    st.markdown(
        """
    **YOLOv8** — нейросетевая модель для детекции и трекинга объектов на видео.  
    Она способна быстро и точно находить собачек на кадрах и отслеживать их перемещение в реальном времени.  

    Для обучения модели я вручную разметила около пятисот кадров с изображениями щенков, указав точные позиции каждого животного.  
    Благодаря этому модель научилась самостоятельно выявлять и отслеживать собак на новых видео. Однако стоит помнить, что модели семейства YOLO чувствительны к изменениям формы отслеживаемых объектов.  
    Если объект сильно меняет позу или форму (например, щенок кувыркается или прячется), точность трекинга может снижаться.  

    Несмотря на это, даже на небольшом кастомном датасете можно добиться неплохих результатов! 
    """
    )

    st.markdown("Вот как это выглядит в действии:")

    st.image(
        "data/images/Untitled_V1-0001.gif",
        caption="Беготня и обычные щеночьи дела 🐶",
        use_container_width=True,
    )

    st.image(
        "data/images/animation_V1-0003.gif",
        caption="Куча-мала, быстрые изменения и хаос 🐕",
        use_container_width=True,
    )

    st.image(
        "data/images/animation_V1-0004.gif",
        caption="Выход из кадра, движение и появление новых объектов 🐾",
        use_container_width=True,
    )

    st.info("Модель: YOLOv8, трекер: BoT-SORT, обучение на кастомной выборке")

elif option == "Инференсим видео 🐾":

    output_dir = Path("inferenced_videos")
    output_dir.mkdir(parents=True, exist_ok=True)

    def clear_folder(folder: Path):
        if folder.exists() and folder.is_dir():
            for f in folder.iterdir():
                if f.is_file():
                    f.unlink()
                elif f.is_dir():
                    shutil.rmtree(f)

    if "cleared_output_dir" not in st.session_state:
        clear_folder(output_dir)
        st.session_state["cleared_output_dir"] = True

    st.subheader("1. Выберите видео из галереи и запустите инференс")

    demo_folder = Path("data/examples")
    demo_videos = list(demo_folder.glob("*.mov")) + list(demo_folder.glob("*.mp4"))

    demo_output_dir = output_dir / "demo_detect"
    demo_output_dir.mkdir(exist_ok=True)

    uploaded_output_dir = output_dir / "uploaded_detect"
    uploaded_output_dir.mkdir(exist_ok=True)

    cols = st.columns(3)
    for idx, video_path in enumerate(demo_videos):
        thumb_path = video_path.with_suffix(".png")
        if thumb_path.exists():
            with cols[idx % 3]:
                st.image(str(thumb_path), use_container_width=True)
                if st.button(f"Выбрать", key=f"demo_select_{video_path.name}"):
                    st.session_state["chosen_demo"] = str(video_path)
                    st.session_state.pop("uploaded_video_path", None)
                    st.session_state.pop("demo_output_path", None)
                    st.session_state.pop("uploaded_output_path", None)

    if "chosen_demo" in st.session_state:
        demo_video_path = st.session_state["chosen_demo"]
        st.video(demo_video_path)

        if st.button("🚀 Запустить инференс", key="run_demo_inference"):
            with st.spinner("Считаем щеночков..."):
                unique_name = f"annotated_demo_{uuid.uuid4().hex}"
                save_dir = demo_output_dir / unique_name
                save_dir.mkdir(parents=True, exist_ok=True)

                results = model.track(
                    source=demo_video_path,
                    tracker="configs/puppy_tracker.yaml",
                    save=True,
                    save_txt=False,
                    project=str(demo_output_dir),
                    name=unique_name,
                    exist_ok=True,
                    conf=0.4,
                )

                mp4_files = sorted(save_dir.glob("*.mp4"))
                print(mp4_files)
                if mp4_files:
                    latest = mp4_files[-1]
                    print(latest)
                    output_path = save_dir / latest.name
                    print(output_path)
                    st.session_state["demo_output_path"] = str(output_path)
                    st.success("Готово! 🎉")
                else:
                    st.error("Ошибка: не найдено видео после инференса.")

    if "demo_output_path" in st.session_state:
        output_path = st.session_state["demo_output_path"]
        st.video(output_path)
        with open(output_path, "rb") as f:
            st.download_button(
                label="📥 Скачать видео (демо)",
                data=f,
                file_name=Path(output_path).name,
                mime="video/mp4",
                key="download_demo_video",
            )

    st.subheader("2. Или загрузите своё видео")
    uploaded_file = st.file_uploader(
        "Загрузите видео (.mp4 или .mov)", type=["mp4", "mov"], key="upload_own_video"
    )

    if uploaded_file:
        suffix = Path(uploaded_file.name).suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            temp_file.write(uploaded_file.read())
            uploaded_video_path = temp_file.name
            st.session_state["uploaded_video_path"] = uploaded_video_path
            st.session_state.pop("chosen_demo", None)
            st.session_state.pop("demo_output_path", None)
            st.session_state.pop("uploaded_output_path", None)

        st.video(uploaded_video_path)

    if "uploaded_video_path" in st.session_state:
        uploaded_video_path = st.session_state["uploaded_video_path"]

        if st.button("🚀 Запустить инференс", key="run_uploaded_inference"):
            with st.spinner("Считаем щеночков..."):
                results = model.track(
                    source=uploaded_video_path,
                    tracker="configs/puppy_tracker.yaml",
                    save=True,
                    save_txt=False,
                    project=str(uploaded_output_dir),
                    name="detect",
                    exist_ok=True,
                    conf=0.4,
                )
                latest = sorted((uploaded_output_dir / "detect").glob("*.mp4"))[-1]
                output_path = output_dir / f"annotated_uploaded_{uuid.uuid4().hex}.mp4"
                shutil.copy(latest, output_path)
                st.session_state["uploaded_output_path"] = str(output_path)
                st.success("Готово! 🎉")

    if "uploaded_output_path" in st.session_state:
        output_path = st.session_state["uploaded_output_path"]
        st.video(output_path)
        with open(output_path, "rb") as f:
            st.download_button(
                label="📥 Скачать видео (загруженное)",
                data=f,
                file_name=Path(output_path).name,
                mime="video/mp4",
                key="download_uploaded_video",
            )
