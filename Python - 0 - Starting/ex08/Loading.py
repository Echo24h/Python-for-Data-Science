from os import get_terminal_size


def ft_tqdm(lst: range):
    """
    Display a progress bar.

    Args:
        lst (range): A range of elements.

    Returns:
        None
    """

    total = len(lst)
    for i, item in enumerate(lst, 1):

        progress = int(i / total * 100)

        width = get_terminal_size().columns

        prefix = f"{progress:3d}%|"
        suffix = f"| {i}/{total}"

        bar_length = width - len(prefix) - len(suffix) - 1
        progress_length = int(bar_length * progress / 100)

        bar = (
            prefix
            + '█' * progress_length
            + ' ' * (bar_length - progress_length)
            + suffix
            )

        print("\r" + bar, end="")
        yield bar
    print()


if __name__ == "__main__":
    for _ in ft_tqdm(range(100)):
        from time import time
        time.sleep(0.1)
