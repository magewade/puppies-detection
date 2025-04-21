
# 🐶 YOLOv8 + FastAPI + Streamlit: Детекция щенков на видео

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Powered by Ultralytics YOLOv8](https://img.shields.io/badge/Powered%20by-YOLOv8-blue?logo=github)](https://github.com/ultralytics/ultralytics)
[![Run in Colab](https://img.shields.io/badge/Run%20in-Google%20Colab-yellow?logo=googlecolab)](https://colab.research.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

> Этот проект демонстрирует, как с помощью YOLOv8 и FastAPI на Google Colab обрабатывать видео и отображать результаты через интерфейс Streamlit — быстро, удобно и красиво.

---

## 📸 Превью

<p align="center">
  <img src="preview.gif" alt="Demo" width="640"/>
</p>

*(анимация или скриншот аннотированного видео, можно заменить на свой `preview.gif`)*

---

## 📦 Стек технологий

- **[YOLOv8](https://docs.ultralytics.com/)** — детекция объектов на видео
- **[FastAPI](https://fastapi.tiangolo.com/)** — API-сервер на Colab
- **[ngrok](https://ngrok.com/)** — проброс сервера из Colab наружу
- **[Streamlit](https://streamlit.io/)** — лёгкий фронтенд для пользователей

---

## 🚀 Быстрый старт

### 1. 🧠 Обучите или возьмите свою YOLOv8 модель

> Файл `best.pt` должен находиться в директории проекта или загружаться в Colab.

---

### 2. 📡 Запустите FastAPI сервер на Colab

- Открой [Colab Notebook](colab_yolo_api.ipynb)
- Загрузите туда свою модель YOLO
- Запустите сервер и получите ссылку ngrok

---

### 3. 🌐 Запустите Streamlit-клиент

Установи зависимости и запусти интерфейс:

```bash
pip install -r requirements.txt
streamlit run app.py
```


## 🗂 Структура проекта

```bash
project-root/
├── app.py                 # Streamlit клиент
├── requirements.txt       # Зависимости
├── README.md              # Документация (этот файл)
└── colab_yolo_api.ipynb   # FastAPI сервер на Colab
```



## 📹 Как работает

1. Пользователь загружает видео через Streamlit
2. Видео отправляется на FastAPI сервер в Colab
3. YOLOv8 выполняет инференс и сохраняет аннотированное видео
4. Streamlit получает результат и отображает его

## ⚠️ Ограничения

- Colab "засыпает" через ~90 минут
- Ngrok URL временный (можно автоматизировать)
- Обработка длинных видео может занимать значительное время

---

## 💡 Идеи для развития

- Прогресс-бар инференса
- Поддержка изображений и batch-инференса
- Загрузка модели из интерфейса
- Постобработка результатов YOLO (например, фильтрация по классам)

---

## ❤️ Автор

Разработка и милашки — [@you](https://github.com/yourusername)
YOLOv8 — [Ultralytics](https://github.com/ultralytics)

---

## 📄 Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).
