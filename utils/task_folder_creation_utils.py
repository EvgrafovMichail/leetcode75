import os
import re

from pathlib import PureWindowsPath


class InvalidTaskIDError(Exception):
    """
    Возбуждается, если передан недействительный task_id.
    """


class TemplateCreator:
    """
    Объект для создания шаблона папки с решением задачи.
    """

    PATH_TO_TASKS_FOLDER: str = "tasks"
    PATH_TO_README: str = "README.md"
    TASK_ID_PATTERN: str = r"^[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]$"

    @staticmethod
    def create(task_id: str) -> None:
        """
        Создает шаблон папки с решением задачи.

        Args:
            task_id: идентификатор задачи.

        Raises:
            InvalidTaskIDError, если был передан неверный task_id,
                или каталог с переданным task_id уже существует.
        """
        path_to_task_folder = TemplateCreator._get_path_to_task_folder(
            task_id=task_id,
        )

        os.makedirs(path_to_task_folder)
        readme_header = TemplateCreator._create_files(task_id, path_to_task_folder)
        TemplateCreator._update_readme(readme_header, path_to_task_folder)

    @staticmethod
    def _get_path_to_task_folder(task_id: str) -> str:
        """
        Формирует путь до папки с решением.

        Args:
            task_id: идентификатор задачи.

        Returns:
            Путь до папки с решением.

        Raises:
            InvalidTaskIDError, если был передан неверный task_id,
                или каталог с переданным task_id уже существует.
        """
        if not re.match(TemplateCreator.TASK_ID_PATTERN, task_id):
            raise InvalidTaskIDError(
                "valid task ID must match next pattern: "
                f"{TemplateCreator.TASK_ID_PATTERN}"
            )

        path_to_task_folder = os.path.join(
            TemplateCreator.PATH_TO_TASKS_FOLDER, task_id
        )

        if os.path.exists(path_to_task_folder):
            raise InvalidTaskIDError(
                f"folder for task ID {task_id} is already exist"
            )
        
        return path_to_task_folder

    @staticmethod
    def _create_files(task_id: str, path_to_folder: str) -> str:
        """
        Создает шаблонный файл с решением и шалонное описание решения.

        Args:
            task_id: идентификатор задачи.
            path_to_folder: путь до папки с решением.
        """
        path_to_script = os.path.join(path_to_folder, f"{task_id}.py")
        indent = " " * 4
        script_content = (
            f"class Solution:\n{indent}pass\n\n\n"
            f"if __name__ == \"__main__\":\n{indent}pass\n"
        )

        with open(path_to_script, "w") as file:
            file.write(script_content)

        path_to_readme = os.path.join(path_to_folder, "README.md")
        readme_header = " ".join(map(str.capitalize, task_id.split("_")))
        readme_content = f"# {readme_header}\n"

        with open(path_to_readme, "w") as file:
            file.write(readme_content)

        return readme_header

    @staticmethod
    def _update_readme(task_id: str, path_to_folder) -> None:
        """
        Добавляет ссылку на созданную папку в README.md.

        Args:
            task_id: идентификатор задачи.
            path_to_folder: путь до папки с решением.
        """
        if os.path.sep == "\\":
            path_normalized = os.path.normpath(path_to_folder)
            path_to_folder = PureWindowsPath(path_normalized).as_posix()

        content_to_add = f"- [{task_id}]({path_to_folder});\n"

        with open(TemplateCreator.PATH_TO_README, "a") as file:
            file.write(content_to_add)
