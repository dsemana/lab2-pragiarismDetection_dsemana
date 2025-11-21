import os
import string


STOP_WORDS = {
    "a",
    "an",
    "the",
    "is",
    "in",
    "of",
    "and",
    "to",
    "for",
    "on",
    "with",
    "at",
    "by",
    "from",
}


def read_file_text(path: str) -> str:
    """Read text from a file, returning an empty string if it cannot be read."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: file not found -> {path}")
    except OSError as exc:
        print(f"Error reading file '{path}': {exc}")
    return ""


def _normalize_text(text: str) -> str:
    """
    Lowercase text and remove punctuation.

    This helper is used by both the processing function and the word search
    so that behavior is consistent.
    """
    text = text.lower()
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


def process_text(raw_text: str) -> list[str]:
    """
    Process raw text into a clean list of meaningful words.

    Steps:
    - lowercase
    - remove punctuation
    - split into words
    - filter out stop words
    """
    if not raw_text:
        return []

    normalized = _normalize_text(raw_text)
    words = normalized.split()
    cleaned = [w for w in words if w and w not in STOP_WORDS]
    return cleaned


def count_word_in_text(raw_text: str, search_word: str) -> int:
    """
    Count the occurrences of a word in the original essay text.

    The text is normalized (lowercase, punctuation removed) before counting.
    """
    if not raw_text or not search_word:
        return 0

    normalized_text = _normalize_text(raw_text)
    words = normalized_text.split()
    target = search_word.strip().lower()
    return sum(1 for w in words if w == target)


def jaccard_similarity(words1: list[str], words2: list[str]) -> tuple[float, set[str]]:
    """
    Compute Jaccard similarity between two word lists.

    Returns:
        (similarity_percentage, intersection_set)
    """
    set1 = set(words1)
    set2 = set(words2)

    if not set1 and not set2:
        return 0.0, set()

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    similarity = (len(intersection) / len(union)) * 100 if union else 0.0
    return similarity, intersection


def prompt_yes_no(message: str) -> bool:
    """Prompt the user for a yes/no answer, returning True for 'y'."""
    while True:
        answer = input(message).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter 'y' or 'n'.")


def save_report(common_words: set[str], reports_dir: str = "reports") -> None:
    """Save the list of common words to a report file."""
    if not common_words:
        print("No common words to save.")
        return

    os.makedirs(reports_dir, exist_ok=True)
    report_path = os.path.join(reports_dir, "similarity_report.txt")

    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("Common words between essay1 and essay2:\n")
            for word in sorted(common_words):
                f.write(f"{word}\n")
        print(f"Report saved to '{report_path}'.")
    except OSError as exc:
        print(f"Error writing report file: {exc}")


def main() -> None:
    essays_dir = "essays"
    essay1_path = os.path.join(essays_dir, "essay1.txt")
    essay2_path = os.path.join(essays_dir, "essay2.txt")

    print("=== Plagiarism Detector ===")
    print(f"Reading essays from '{essay1_path}' and '{essay2_path}'...")

    essay1_text = read_file_text(essay1_path)
    essay2_text = read_file_text(essay2_path)

    if not essay1_text or not essay2_text:
        print("Unable to continue: one or both essay files could not be read or are empty.")
        return

    # Process essays into clean word lists
    words_essay1 = process_text(essay1_text)
    words_essay2 = process_text(essay2_text)

    # Word search feature
    search_word = input("Enter a word to search in both essays: ").strip()
    if search_word:
        count1 = count_word_in_text(essay1_text, search_word)
        count2 = count_word_in_text(essay2_text, search_word)
        print(f"'{search_word}' appears {count1} time(s) in essay1 and {count2} time(s) in essay2.")
    else:
        print("No search word provided; skipping word search.")

    # Common words report (based on processed lists)
    common_words = set(words_essay1).intersection(words_essay2)
    print("\nCommon words in both essays (after cleaning and removing stop words):")
    if common_words:
        print(", ".join(sorted(common_words)))
    else:
        print("No common words found.")

    # Plagiarism calculation using Jaccard similarity
    similarity, intersection = jaccard_similarity(words_essay1, words_essay2)
    print("\n=== Plagiarism Report (Jaccard Similarity) ===")
    print(f"Plagiarism percentage: {similarity:.2f}%")

    if similarity >= 50.0:
        print("Similarity is likely (50% or more).")
    else:
        print("Similarity is unlikely (less than 50%).")

    print("\nWords contributing to similarity (intersection set):")
    if intersection:
        print(", ".join(sorted(intersection)))
    else:
        print("Intersection is empty; no overlapping meaningful words.")

    # Optionally save report
    if prompt_yes_no("\nDo you want to save this report? (y/n): "):
        save_report(intersection)
    else:
        print("Report not saved.")


if __name__ == "__main__":
    main()


