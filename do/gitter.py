# -*- coding: utf-8 -*-

import os
import git
from git import Repo
from do import GITHUB_SITE, GIT_EXT, GITHUB_RAPYDO_COMPANY, PROJECT_DIR
from do.utils.logs import get_logger

log = get_logger(__name__)


def clone(repo, path, do=False):

    local_path = os.path.join(PROJECT_DIR, path)
    online_url = f"{GITHUB_SITE}/{GITHUB_RAPYDO_COMPANY}/{repo}.{GIT_EXT}"

    # check if directory exist
    if os.path.exists(local_path):
        gitobj = Repo(local_path)
        log.debug(f"(CHECKED)\tPath {local_path} already exists")
    elif do:
        gitobj = Repo.clone_from(url=online_url, to_path=local_path)
        log.info(f"Cloned repo {repo} as {path}")
    else:
        log.critical_error(
            "Repo {GITHUB_RAPYDO_COMPANY}/{repo} is missing in {path}")

    return comparing(gitobj, online_url=online_url)


def comparing(gitobj, online_url):

    # TODO: get one file
    # gitobj.blame(rev='HEAD', file='docker-compose.yml')

    # and check against online version
    # tmp = obj.commit(rev='177e454ea10713975888b638faab2593e2e393b2')
    # tmp.committed_datetime

    raise NotImplementedError("MISSING COMPARE")
