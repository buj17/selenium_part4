# ИНСТРУКЦИЯ ДЛЯ ЗАПУСКА

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

## ⚠️ Предупреждение ⚠️

Для выполнения условий задания и совместимости со стандартным python venv есть файл `requirements.txt`,
но вместо него настоятельно рекомендуется использовать uv.

### Для запуска понадобится:

- git
- uv. Инструкция по его установке [здесь](https://docs.astral.sh/uv/getting-started/installation/)

### Шаги для запуска:

#### Склонировать репозиторий

```bash
git clone https://github.com/buj17/selenium_part4
```

#### Перейти в директорию с проектом

```bash
cd selenium_part4
```

#### Запустить тесты

```bash
uv run pytest -v --tb=line --language=en -m need_review
```
