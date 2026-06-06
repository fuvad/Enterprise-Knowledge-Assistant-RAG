import os
import tempfile

from git import Repo

from app.schemas.document import Document


class GithubLoader:

    def load(self, repo_url: str):

        temp_dir = tempfile.mkdtemp()

        Repo.clone_from(
            repo_url,
            temp_dir
        )

        documents = []

        for root, _, files in os.walk(temp_dir):

            for file in files:

                if file.endswith(
                    (
                        ".py",
                        ".md",
                        ".txt"
                    )
                ):

                    path = os.path.join(
                        root,
                        file
                    )

                    try:

                        with open(
                            path,
                            "r",
                            encoding="utf-8",
                            errors="ignore"
                        ) as f:

                            documents.append(
                                Document(
                                    source="github",
                                    filename=file,
                                    text=f.read()
                                )
                            )

                    except Exception:
                        pass

        return documents