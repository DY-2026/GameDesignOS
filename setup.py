"""Build hooks for shipping canonical GameDesignOS data inside wheels."""

from __future__ import annotations

import shutil
from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py as _build_py


class build_py(_build_py):
    """Copy canonical repo resources into the built Python package.

    The repository copies remain the only editable sources. The wheel receives a
    generated snapshot so an installed runtime does not need a source checkout.
    """

    def run(self) -> None:
        super().run()
        root = Path(__file__).resolve().parent
        data_root = Path(self.build_lib) / "gamedesignos" / "_data"
        for source, relative in (
            (root / "contracts", Path("contracts")),
            (root / "runtime" / "workspace-template", Path("workspace-template")),
            (root / "runtime" / "workspace-template-v1", Path("workspace-template-v1")),
        ):
            target = data_root / relative
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))


setup(cmdclass={"build_py": build_py})
