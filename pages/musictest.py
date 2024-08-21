import streamlit as st

def music_app_layout():
    # Title of the app
    st.title("My Music App")

    # Example music albums and songs
    albums = [
        {"title": "Song 1", "album": "Album 1", "artist": "Artist 1"},
        {"title": "Song 2", "album": "Album 2", "artist": "Artist 2"},
        {"title": "Song 3", "album": "Album 3", "artist": "Artist 3"},
        {"title": "Song 4", "album": "Album 4", "artist": "Artist 4"},
        {"title": "Song 5", "album": "Album 5", "artist": "Artist 5"},
    ]

    # Displaying each song with album image and audio player
    for i, album in enumerate(albums):
        st.subheader(f"{album['title']} - {album['artist']}")
        col1, col2 = st.columns([1, 3])
        
        # Placeholder for album image
        with col1:
            st.image("https://via.placeholder.com/150", caption=album["album"])

        # Audio player with a random tone (placeholder)
        with col2:
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

        # Separator between songs
        st.write("---")
