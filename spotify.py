from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import spotipy
import re

# Create a Spotify client
sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(
    client_id = '988d05c0b4234fa4bf589b985ec7ac33',
    client_secret = '9f2c0510550e4d8794600b94522b3eb3'
))

# Track URL
track_url = "https://open.spotify.com/track/0tgVpDi06FyKpA1z0VMD4v"

# Extract track ID from the URL
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# Fetch track details
track = sp.track(track_id)
print(track)               # JSON

# Extract metadata
track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000  # Convert milliseconds to minutes
}

# Display metadata
print(f"\nTrack Name: {track_data['Track Name']}")
print(f"Artist: {track_data['Artist']}")
print(f"Album: {track_data['Album']}")
print(f"Popularity: {track_data['Popularity']}")
print(f"Duration: {track_data['Duration (minutes)']:.2f} minutes")   

# Convert metadata to DataFrame
df = pd.DataFrame([track_data])
print("\nTrack data as DataFrame:")
print(df)

# Save DataFrame to CSV
df.to_csv('spotify_track_data.csv', index = False)

# Plotting
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

plt.figure(figsize = (8, 5))
plt.bar(features, values, color = 'skyblue', edgecolor = 'black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('Value')
plt.show()