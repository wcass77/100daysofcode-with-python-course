import webbrowser

import api

BASE_URL = "https://talkpython.fm"


def main():
    print("Talk Python Search:")
    search_terms = input("Search:").split()
    try:
        results = api.search(search_terms)
    except api.NoResultsFound:
        print(f"No results found for {' '.join(search_terms)}")
        return
    for i, episode in enumerate(sorted(results, key=lambda r: r.id)):
        print(f"{i+1}. {episode.id}: {episode.title}")
    id_ = int(input("Choose an episode id:"))
    for episode in results:
        if episode.id == id_:
            webbrowser.open_new_tab(BASE_URL + episode.url)
            break
    else:
        print("Invalid id")


if __name__ == "__main__":  # pragma: no cover
    main()
