# 🐶 YOLOv8 + Streamlit: Детекция щенков на видео

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Powered by Ultralytics YOLOv8](https://img.shields.io/badge/Powered%20by-YOLOv8-blue?logo=github)](https://github.com/ultralytics/ultralytics)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

> Этот проект показывает, как с помощью **YOLOv8** и **Streamlit** можно удобно обрабатывать видео локально: находить щенков на кадрах и визуализировать результат через простой и красивый интерфейс.

---

## 📸 Превью

<p align="center">
  <img src="data/images/Untitled_V1-0001.gif" alt="Demo" width="640"/>
</p>

---

## 📦 Технологии проекта

- **[YOLOv8](https://docs.ultralytics.com/)** — детекция и трекинг объектов на видео
- **[Streamlit](https://streamlit.io/)** — быстрый веб-интерфейс для взаимодействия с пользователем

---

## 🚀 Как запустить проект

### 1. Установите зависимости

```bash
pip install -r requirements.txt
```

### 2. Запустите приложение Streamlit

```bash
streamlit run app.py
```

---

## 🗂 Структура проекта

```bash
project-root/
├── app.py                      # Основной код приложения Streamlit
├── notebooks/                  # Все ноутбуки с исследованиями и обучением
│   ├── 1_Research.ipynb   
│   ├── 2_Model_Training.ipynb  
│   └── 3_Inference.ipynb       # Проверка инференса стрима и футажей
├── configs/                    # Конфигурационные файлы, например трекер
│   └── puppy_tracker.yaml  
├── requirements.txt            # Список зависимостей
├── README.md                   # Документация проекта
├── LICENSE                     # Лицензия MIT
├── data/                       # Папки с ресурсами проекта
│   ├── examples/               # Футажи для инференса
│   ├── images/                 # Гифки и иллюстрации
└──weights/                    # Веса модели
```

---

## 📹 Как это работает

1. Пользователь выбирает демо-видео, трансляцию или загружает своё.
2. Модель **YOLOv8** выполняет инференс.
3. Полученное аннотированное видео отображается в интерфейсе Streamlit.
4. Готовый результат можно скачать одним кликом.

---

## ⚡ Особенности проекта

- Детекция и трекинг щенков в реальном времени
- Возможность скачать аннотированное видео
- Красивая визуализация результатов через гифки

---

## ❤️ Автор

Милые щеночки — [Explore Dogs](https://www.youtube.com/watch?v=bYlEgU2tU5w)

Библиотека YOLOv8 — [Ultralytics](https://github.com/ultralytics)

Разработка — [@magewade](https://github.com/magewade)

---

## 📄 Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).
