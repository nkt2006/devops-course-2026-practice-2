"""Минимальное приложение для учебного DevOps-проекта."""


def project_summary() -> str:
    """Вернуть краткое описание проекта."""
    return "DevOps Course 2026: Git, GitHub, автоматизация и инфраструктура"


def main() -> None:
    """Вывести информацию о проекте."""
    print(project_summary())


if __name__ == "__main__":
    main()
