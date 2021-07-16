# django-debugger

A simple plugin to attach a debugger in Django during runserver

## Installation

```bash
pip install django-debugger
```

## Usage

1. Prepend django_debugger to **top** of the **INSTALLED_APPS**

    ```python

    INSTALLED_APPS = [
        "django_debugger",
        ...
    ]

    # Or if you have multiple settings configuration
    INSTALLED_APPS = [ 
        "django_debugger",
        ... # custom development apps
    ] + INSTALLED_APPS
    ```

2. Add `--enable-debugger` argument to runserver command

    ```bash
    python manage.py runserver ---enable-debugger 0.0.0.0:8000
    ```

    **OR**

    Add `DEBUGGER_ENABLE = True` to settings file.

## Settings Variables

- `DEBUGGER_ENABLE = True` : Attaches debugger.
- `DEBUGGER_ADDRESS = "0.0.0.0"` : Address to listen for remote debugging
- `DEBUGGER_PORT = 5678` : Port to listen for remote debugging
- `DEBUGGER_WAIT_FOR_ATTACH = False` : Wait for debugger to attach before continuing.
