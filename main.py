import apiCalls
import os
import pandas as pd




def main():
    # num_videos = os.environ.get("NUM_VIDEOS")
    # print(num_videos)
    data = {
        'PostURL': [],
        'Account': [],
        'Views': [],
        'Likes': [],
        'Saved': [],
        'Caption': [],
        'Hashtags': [],
        'Dateposted': [],
        'Datecollected': []
    }
    df = pd.DataFrame(data)

    resultsWritten = 0
    while resultsWritten < 100:
        response = apiCalls.getExploreItemByCategory()
        if response:
            new_video_objects = apiCalls.buildVideoObjects(response)
            for vo in new_video_objects:
                df = vo.write_to_dataframe(df)
                resultsWritten += 1
    df.to_csv('output.csv', index=False)


if __name__ == "__main__":
    main()