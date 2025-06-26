FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# скопируем список требуемых модулей
COPY requirements.txt .

## немедленный выход если любая команда в цепочке вернула не 0
RUN set -e \
## ссылка на список требуемых модулей
&& reqs=requirements.txt \
## средства сборки и библиотеки для приложения
&& tmp_deps="build-base" \
&& apk add --no-cache libstdc++ gcompat libgcc $tmp_deps \
## установка
&& pip install --no-cache-dir -r ${reqs} \
## очистка мусора 
&& apk del --no-cache $tmp_deps \
&& rm -rf ..?* .[!.]* * \
## отключение опции немедленного выхода
&& set +e

# переменные окружения
ENV PYTHONPATH=/app/report-api

# переносим в норм место :)
COPY ./app /app/report-api

# исполним при запуске контейнера
CMD ["fastapi", "run", "/app/report-api/main.py", "--workers", "2"]
