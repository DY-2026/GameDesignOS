"""Runtime-specific exceptions and process exit codes."""

from __future__ import annotations


EXIT_OK = 0
EXIT_VALIDATION = 1
EXIT_USAGE = 2
EXIT_WORKSPACE_NOT_FOUND = 3
EXIT_INCOMPATIBLE_VERSION = 4


class GameDesignOSError(Exception):
    """Base exception for expected runtime failures."""

    exit_code = EXIT_VALIDATION


class UsageError(GameDesignOSError):
    exit_code = EXIT_USAGE


class WorkspaceNotFoundError(GameDesignOSError):
    exit_code = EXIT_WORKSPACE_NOT_FOUND


class VersionCompatibilityError(GameDesignOSError):
    exit_code = EXIT_INCOMPATIBLE_VERSION
