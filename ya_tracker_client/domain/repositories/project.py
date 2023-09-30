from datetime import date

from ya_tracker_client.domain.entities.project import Project, ProjectCreate, ProjectEdit, ProjectWithQueues
from ya_tracker_client.domain.entities.queue import Queue
from ya_tracker_client.domain.repositories.base import EntityRepository


class ProjectRepository(EntityRepository):
    async def create_project(
        self,
        name: str,
        queues: str,
        description: str | None = None,
        lead: str | int | None = None,
        status: str | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
    ) -> Project:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/projects/create-project
        """
        raw_response = await self._client.request(
            method="POST",
            uri="/projects",
            payload=ProjectCreate(
                name=name,
                queues=queues,
                description=description,
                lead=lead,
                status=status,
                start_date=start_date,
                end_date=end_date,
            ).model_dump(exclude_none=True, by_alias=True),
        )
        return self._decode(raw_response, Project)

    async def get_project(self, project_id: str | int) -> Project:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/projects/get-project
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/projects/{project_id}",
        )
        return self._decode(raw_response, Project)

    async def get_projects_list(self, expand: str | None = None) -> list[Project | ProjectWithQueues]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/projects/get-projects
        """
        raw_response = await self._client.request(
            method="GET",
            uri="/projects",
            params={"expand": expand}  if expand is not None else None,
        )
        return self._decode(raw_response, ProjectWithQueues if expand == "queues" else Project, plural=True)

    async def get_project_queues(self, project_id: str | int) -> list[Queue]:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/projects/get-project-queues
        """
        raw_response = await self._client.request(
            method="GET",
            uri=f"/projects/{project_id}/queues",
        )
        return self._decode(raw_response, Queue, plural=True)

    async def edit_project(
        self,
        project_id: str | int,
        version: int,
        queues: str,
        name: str | None = None,
        description: str | None = None,
        lead: str | int | None = None,
        status: str | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        expand: str | None = None,
    ) -> Project | ProjectWithQueues:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/projects/update-project
        """
        params = {"version": version}
        if expand:
            params["expand"] = expand

        raw_response = await self._client.request(
            method="PATCH",
            uri=f"/projects/{project_id}",
            payload=ProjectEdit(
                name=name,
                queues=queues,
                description=description,
                lead=lead,
                status=status,
                start_date=start_date,
                end_date=end_date,
            ).model_dump(exclude_none=True, by_alias=True),
            params=params,
        )
        return self._decode(raw_response, ProjectWithQueues if expand == "queues" else Project)

    async def delete_project(self, project_id: str | int) -> None:
        """
        YC docs: https://cloud.yandex.com/en/docs/tracker/concepts/projects/delete-project
        """
        await self._client.request(
            method="DELETE",
            uri=f"/projects/{project_id}",
        )
