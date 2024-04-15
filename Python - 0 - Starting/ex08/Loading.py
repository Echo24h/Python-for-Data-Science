import time
# import shutil


def format_time(seconds):
    """
    Convert seconds to a human readable format.

    Args:
        seconds (int): The number of seconds.

    Returns:
        str: The time in the format MM:SS.
    """
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"


def ft_tqdm(lst: range) -> None:
    """
    Display a progress bar.

    Args:
        lst (range): A range of elements.

    Returns:
        None
    """
    start_time = time.time()
    total = len(lst)
    for i, item in enumerate(lst, 1):
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = elapsed_time / i * (total - i)

        # average_speed = i / elapsed_time
        # iteration_speed = f"{average_speed:.2f}it/s"

        progress = int(i / total * 100)

        if progress < 10:
            bar = f"  {progress}%|{'█' * progress}{' ' * (100 - progress)}\
| {i}/{total} [{format_time(elapsed_time)}\
<{format_time(remaining_time)}]"
        elif progress < 100:
            bar = f" {progress}%|{'█' * progress}{' ' * (100 - progress)}\
| {i}/{total} [{format_time(elapsed_time)}\
<{format_time(remaining_time)}]"
        else:
            bar = f"{progress}%|{'█' * progress}{' ' * (100 - progress)}\
| {i}/{total} [{format_time(elapsed_time)}\
<{format_time(remaining_time)}]"

        print("\r" + bar, end="")
        yield bar
    print()


if __name__ == "__main__":
    for _ in ft_tqdm(range(100)):
        time.sleep(0.1)
    # shutil.rmtree("test")
