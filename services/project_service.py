class ProjectService:
    def __init__(self, project_config):
        self.project_config = project_config

    def is_valid_project(self, project):
        return project in self.project_config

    def get_project_config(self, project):
        return self.project_config.get(project, {})