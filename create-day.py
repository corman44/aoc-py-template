
def main() -> None:
    # parse input from command line for day number
    day_number = int(input("Enter the day number: "))

    # copy Template folder to DayXX folder where XX is the day with leading zero
    import shutil
    import os
    day_folder = f"Day{day_number:02d}"
    shutil.copytree("Template", day_folder)
    print(f"Created folder: {day_folder}")

    # replace X in .py filenames with day number
    for filename in os.listdir(day_folder):
        if "X" in filename:
            new_filename = filename.replace("X", f"{day_number:02d}")
            os.rename(os.path.join(day_folder, filename), os.path.join(day_folder, new_filename))
            print(f"Renamed {filename} to {new_filename}")

    # fill input.txt with text from link where XX is the day number
    import requests
    input_url = f"https://adventofcode.com/2024/day/{day_number}/input"

    from dotenv import load_dotenv
    load_dotenv()
    session_cookie = os.getenv("SESSION_COOKIE")
    if not session_cookie:
        print("SESSION_COOKIE not found in environment variables.")
        return

    # add session cookie to request
    cookies = {'session': session_cookie}
    response = requests.get(input_url, cookies=cookies)
    if response.status_code == 200:
        with open(os.path.join(day_folder, "input.txt"), "w") as f:
            f.write(response.text)
            print(f"Fetched input data for Day {day_number}")
    else:
        print(f"No input data found for Day {day_number} with status code {response.status_code}")
    
if __name__ == "__main__":
    main()
