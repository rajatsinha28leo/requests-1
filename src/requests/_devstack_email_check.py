"""Throwaway helper for a devstack email test; this PR is never merged."""


def last_items(items, count):
    """Return the last ``count`` items of ``items``."""
    return items[len(items) - count - 1 :]
