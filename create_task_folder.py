from utils.parser import parser
from utils.task_folder_creation_utils import TemplateCreator


if __name__ == "__main__":
    args = parser.parse_args()
    TemplateCreator.create(args.task_id)
